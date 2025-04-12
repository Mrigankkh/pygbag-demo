install:
	pip install -r requirements.txt

build:
	pygbag --build .

serve:
	python3 -m http.server

deploy:
	pygbag --build .
	mkdir -p docs
	cp -r build/web/* docs/


run-local:
	python3 -m venv pygame-venv && \
	. pygame-venv/bin/activate && \
	pip install --upgrade pip setuptools wheel && \
	pip install -r requirements.txt && \
	python main.py
