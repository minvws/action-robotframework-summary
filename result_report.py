from robot.api import ExecutionResult, ResultVisitor
import sys

class ResultReport(ResultVisitor):
    def __init__(self, markdown_file='report.md'):
        self.failed_tests = []
        self.passed_tests = []
        self.markdown_file = markdown_file

    def visit_test(self, test):
        if test.status == 'FAIL':
            self.failed_tests.append(test.name)
        elif test.status == 'PASS':
            self.passed_tests.append(test.name)

    def end_result(self, result):
        # Create a new markdown file
        with open(self.markdown_file, "w") as f:
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
        output_file = sys.argv[1]
    except IndexError:
        output_file = "output.xml"
    try:
        markdown_file = sys.argv[2]
    except IndexError:
        markdown_file = "report.md"
    result = ExecutionResult(output_file)
    result.visit(ResultReport())