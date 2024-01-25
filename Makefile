venv: .venv/touchfile ## Create virtual environment
.venv/touchfile:
	test -d .venv || python3.11 -m venv .venv
	. .venv/bin/activate && pip install --upgrade pip
	. .venv/bin/activate && pip install -r requirements.txt
	touch .venv/touchfile

clean_venv: ## Remove virtual environment
	@echo "Cleaning venv"
	@rm -rf .venv

generate_report:
	python result_report.py example_output.xml report.md
	cat report.md