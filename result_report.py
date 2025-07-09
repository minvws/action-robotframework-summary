"""Library that will parse a Robot Framework results file, output.xml."""
import sys
import requests
from robot.api import ExecutionResult, ResultVisitor

class ResultReport(ResultVisitor):
    """Implementation of a Robot Framework ResultVisitor."""

    def __init__(self, markdown_file, endpoints, username, password):
        """Constructor"""
        self.tests = []
        self.markdown_file = markdown_file
        self.endpoints = endpoints
        self.username = username
        self.password = password

    def start_suite(self, suite):
        """Implementation of start_suite"""
        for test in suite.tests:
            test.message = suite.name
            self.tests.append(test)

    def add_component_version_table(self, file):
        """Requests the versions of the given endpoints and adds them to file as a table"""
        if len(self.endpoints) == 0:
            return None

        endpoint_versions = {}

        urls = self.endpoints.split(',')
        for url in urls:
            if len(self.username) > 0:
                response = requests.get(
                    url + '/version.json',
                    auth=(self.username, self.password),
                    timeout=5
                )
            else:
                response = requests.get(
                    url + '/version.json',
                    timeout=5
                )

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

    def end_result(self, result):
        """Implementation of end_result"""
        # Create a new markdown file
        with open(self.markdown_file, "w", encoding="utf-8") as f:
            stats = result.statistics

            self.add_component_version_table(f)

            f.write(f"Total tests: {stats.total.total}\n")
            f.write(f":green_circle: {stats.total.passed} passed\n")
            f.write(f":red_circle: {stats.total.failed} failed\n")
            f.write("\n")
            f.write("|Testsuite|Testcase|Result|\n")
            f.write("|---|---|---|\n")
            for test in self.tests:
                f.write("| " + test.message + " | " + test.name + " | ")
                if test.status == 'FAIL':
                    f.write(":red_circle:|\n")
                elif test.status == 'PASS':
                    f.write(":green_circle:|\n")
                elif test.status == 'SKIP':
                    f.write(":white_circle:|\n")

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
        ENDPOINTS = sys.argv[3]
    except IndexError:
        ENDPOINTS = ""
    try:
        USERNAME = sys.argv[4]
    except IndexError:
        USERNAME = ""
    try:
        PASSWORD = sys.argv[5]
    except IndexError:
        PASSWORD = ""

    execResult = ExecutionResult(OUTPUT_FILE)
    execResult.visit(ResultReport(MARKDOWN_FILE, ENDPOINTS, USERNAME, PASSWORD))
