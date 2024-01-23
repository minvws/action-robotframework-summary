venv:
	python3.11 -m venv .venv
	.venv/bin/python -m pip install robotframework
	.venv/bin/python -m pip install requests
	.venv/bin/python -m pip uninstall robot

clean-venv:
	rm -rf .venv

generate-report:
	.venv/bin/python result_report.py example_output.xml report.md
	cat report.md