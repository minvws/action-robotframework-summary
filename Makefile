prepare:
	python3.11 -m venv env
	env/bin/python -m pip install robotframework

generate-report:
	env/bin/python result_report.py example_output.xml report.md
	cat report.md