venv:
	python3.11 -m venv .venv
	python -m pip install robotframework
	python -m pip install requests
	python -m pip uninstall robot

clean-venv:
	deactivate
	rm -rf .venv

generate-report:
	python result_report.py example_output.xml report.md
	cat report.md