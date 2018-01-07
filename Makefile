all: test

clean:
	rm -rf /tmp/your_application/ && rm -rf ~/.virtualenvs/your_application/

test: clean
	cookiecutter . --output-dir /tmp --no-input && \
	cd /tmp/your_application && \
	make venv && \
	make test
