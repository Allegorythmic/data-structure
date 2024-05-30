.PHONY: test clean coverage install lint all

install:
	pip install -r requirements.txt

coverage:
	pytest --cov=src --cov-report=term-missing --cov-report=xml

lint:
	flake8 src src/tests

clean:
	@echo "Cleaning up..."
	@if [ "$(OS)" = "Windows_NT" ]; then \
		echo "Running on Windows"; \
		cmd /C "del /s /q *.pyc"; \
		cmd /C "for /d %%d in (__pycache__ .pytest_cache htmlcov) do if exist %%d rmdir /s /q %%d"; \
	else \
		echo "Running on Unix"; \
		find . -type f -name '*.pyc' -delete; \
		find . -type d -name '__pycache__' -exec rm -rf {} +; \
		find . -type d -name '.pytest_cache' -exec rm -rf {} +; \
		rm -rf htmlcov; \
	fi

all: clean coverage
