# Github Action Robot Framework test summary

This Github Action can be used to parse the result of Robot Framework tests into a summary and push these to the Github Action pipeline summary. The summary will contain both a count of the tests (total, succesful, failed), as well as a list of all tests with their individual test result.

## Usage

Add the following action to the steps section of your pipeline:

```yaml
    - name: Publish test results
      uses: minvws/nl-rdo-github-action-robotframework-test-summary@v0.1.0
      with:
        output_file: 'tests/robot_framework/results/output.xml'
```

The following parameters are available:

| Option | Default value | Description |
| -- | -- | -- |
| `output_file` | `tests/robot_framework/results/output.xml` | Location of the output.xml file, containing the Robot Framework test results. |
