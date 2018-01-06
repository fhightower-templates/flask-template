all: test

clean:
	rm -rf /tmp/your_application/

test: clean
	cookiecutter . --output-dir /tmp --no-input && \
	cd /tmp/your_application && \
	make test
