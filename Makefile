.PHONY : lock, quality, run

# Target to invoke the poetry lock process
lock:
	@python3 -m pip install -q poetry==1.8.3
	@poetry lock

# Target to invoke the quality process
quality:
	@poetry install --with dev
	@poetry run pre-commit install
	@poetry run pre-commit run --all-files

# Target to invoke the web scrapper
run:
	@poetry install
	@poetry run python src/arxiv_scrapper.py
