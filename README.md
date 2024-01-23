# Github Action Robot Framework test summary

This Github Action can be used to parse the result of Robot Framework tests into a summary and push these to the Github Action pipeline summary. The summary will contain both a count of the tests (total, succesful, failed), as well as a list of all tests with their individual test result.

## Usage

Add the following action to the steps section of your pipeline:

### Basic usage

```yaml
    - name: Publish test results
      uses: minvws/nl-rdo-github-action-robotframework-test-summary@v0.2.0
      if: always()
      with:
        output_file: 'tests/robot_framework/results/output.xml'
```

### Include component versions in summary

```yaml
    - name: Publish test results
      uses: minvws/nl-rdo-github-action-robotframework-test-summary@v0.2.0
      if: always()
      with:
        output_file: 'tests/robot_framework/results/output.xml'
        endpoints: 'https://example-environment.rdobeheer.nl,https://example-environment2.rdobeheer.nl/static'
        username: '${{ secrets.USERNAME }}'
        password: '${{ secrets.PASSWORD }}'
```

## Parameters

The following parameters are available:

| Option | Required | Default value | Description |
| -- | -- | -- | -- |
| `output_file` | Yes | `tests/robot_framework/results/output.xml` | Location of the output.xml file, containing the Robot Framework test results. |
| `endpoints` | No |  | Provide a comma-separated list of endpoints for which the version number should be included in the summary. The endpoints should serve a /version.json. |
| `username` | No |  | Optional username for basic authentication on the endpoints. |
| `password` | No |  | Optional password for basic authentication on the endpoints. |
