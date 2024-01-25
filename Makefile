
setup: requirements.txt
	python3 -m venv .
	bin/pip3 install -r requirements.txt

test:
	bin/pytest -s tests/

install:
	pip3 install .

format:
	bin/black src/ tests/
