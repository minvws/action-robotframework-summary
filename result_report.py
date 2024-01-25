"""Library that will parse a Robot Framework results file, output.xml."""
import sys
from robot.api import ExecutionResult, ResultVisitor

class ResultReport(ResultVisitor):
    """Implementation of a Robot Framework ResultVisitor."""

    def __init__(self, markdown_file):
        """Constructor"""
        self.failed_tests = []
        self.passed_tests = []
        self.markdown_file = markdown_file

    def visit_test(self, test):
        """Implementation of visit_test"""
        if test.status == 'FAIL':
            self.failed_tests.append(test.name)
        elif test.status == 'PASS':
            self.passed_tests.append(test.name)

    def end_result(self, result): # pylint: disable=W0621, W0613
        """Implementation of end_result"""
        # Create a new markdown file
        with open(self.markdown_file, "w", encoding="utf-8") as f:
            f.write("Total tests: " + str(len(self.passed_tests) + len(self.failed_tests)) + "\n")
            f.write(":green_circle: " + str(len(self.passed_tests)) + " passed\n")
            f.write(":red_circle: " + str(len(self.failed_tests)) + " failed\n")
            f.write("\n")
            f.write("|Test|Result|\n")
            f.write("|---|---|\n")
            for test in self.passed_tests:
                f.write(f"|{test}| :green_circle:|\n")
            for test in self.failed_tests:
                f.write(f"|{test}| :red_circle:|\n")

if __name__ == '__main__':
    try:
        OUTPUT_FILE = sys.argv[1]
    except IndexError:
        OUTPUT_FILE = "output.xml"
    try:
        MARKDOWN_FILE = sys.argv[2]
    except IndexError:
        MARKDOWN_FILE = "report.md"
    result = ExecutionResult(OUTPUT_FILE)
    result.visit(ResultReport(MARKDOWN_FILE))
