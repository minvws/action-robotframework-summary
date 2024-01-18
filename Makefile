prepare-env:
	python3.11 -m venv env
	env/bin/python -m pip install robotframework
	env/bin/python -m pip install requests

generate-report:
	env/bin/python result_report.py example_output.xml report.md https://proeftuin.uzi-online.rdobeheer.nl,https://max.proeftuin.uzi-online.rdobeheer.nl/static,https://yivi.proeftuin.uzi-online.rdobeheer.nl labs SisteBoegbeeldSymbolenIngegrift
	cat report.md