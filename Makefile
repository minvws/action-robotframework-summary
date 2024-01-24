venv: .venv/touchfile ## Create virtual environment
.venv/touchfile:
	test -d .venv || python3.11 -m venv .venv
	. .venv/bin/activate && pip install robotframework
	. .venv/bin/activate && pip install requests
	touch .venv/touchfile

clean_venv: ## Remove virtual environment
	@echo "Cleaning venv"
	@rm -rf .venv

generate-report:
	python result_report.py example_output.xml report.md
	cat report.md