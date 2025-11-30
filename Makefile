.PHONY: install run test lint

install:
	python -m pip install -r requirements.txt

run:
	python src/run.py "Analyze ROAS drop in last 7 days" --data data/synthetic_fb_ads_undergarments.csv

test:
	python -m pytest tests

lint:
	flake8 src || echo "flake8 not installed"
