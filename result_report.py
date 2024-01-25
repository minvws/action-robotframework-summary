"""Library that will parse a Robot Framework results file, output.xml."""
import sys
import requests
from robot.api import ExecutionResult, ResultVisitor

class ResultReport(ResultVisitor):
    """Implementation of a Robot Framework ResultVisitor."""

    def __init__(self, markdown_file):
        """Constructor"""
        self.tests = []
        self.markdown_file = markdown_file

    def visit_test(self, test):
        self.tests.append(test)

    def add_component_version_table(self, file):
        if len(endpoints) == 0:
            return None
        
        endpoint_versions = {}

        urls = endpoints.split(',')
        for url in urls:
            if len(username) > 0:
                response = requests.get(url + '/version.json', auth=(username, password))
            else:
                response = requests.get(url + '/version.json')

            if response.status_code == 200:
                version = response.json()['version'] 
            else:
                version = '**ERROR ' + str(response.status_code) + '**'

            endpoint_versions[url.replace('https://','')] = version
        
        file.write("Tested components:\n")
        file.write("| Component | Version |\n")
        file.write("| -- | -- |\n")
        for endpoint, version in endpoint_versions.items():
            file.write("| " + endpoint + " | " + version + " |\n")
        file.write("\n")
        return None

    def end_result(self, result): # pylint: disable=W0621, W0613
        """Implementation of end_result"""
        # Create a new markdown file
        with open(self.markdown_file, "w", encoding="utf-8") as f:
            stats = result.statistics

            self.add_component_version_table(f)

            f.write(f"Total tests: {stats.total.total}\n")
            f.write(f":green_circle: {stats.total.passed} passed\n")
            f.write(f":red_circle: {stats.total.failed} failed\n")
            f.write("\n")
            f.write("|Test|Result|\n")
            f.write("|---|---|\n")
            for test in self.tests:
                f.write("| " + test.name + " | ")
                if test.status == 'FAIL':
                    f.write(":red_circle:|\n")
                elif test.status == 'PASS':
                    f.write(":green_circle:|\n")

if __name__ == '__main__':
    try:
        OUTPUT_FILE = sys.argv[1]
    except IndexError:
        OUTPUT_FILE = "output.xml"
    try:
        MARKDOWN_FILE = sys.argv[2]
    except IndexError:
        MARKDOWN_FILE = "report.md"
    try:
        endpoints = sys.argv[3]
    except IndexError:
        endpoints = ""
    try:
        username = sys.argv[4]
    except IndexError:
        username = ""
    try:
        password = sys.argv[5]
    except IndexError:
        password = ""

    result = ExecutionResult(OUTPUT_FILE)
    result.visit(ResultReport(MARKDOWN_FILE))