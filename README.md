# Github Action Robot Framework test summary

This Github Action can be used to parse the result of Robot Framework tests into a summary and push these to the Github Action pipeline summary.

## Usage

Add the following action to the steps section of your pipeline:

```yaml
    - name: Publish test results
      uses: minvws/nl-rdo-github-action-robotframework-test-summary@main
      with:
        output_file: 'tests/robot_framework/results/output.xml'
```

The following parameters are available:

| Option | Default value | Description |
| -- | -- | -- |
| `output_file` | `tests/robot_framework/results/output.xml` | Location of the output.xml file, containing the Robot Framework test results. |
