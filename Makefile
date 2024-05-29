.PHONY: test clean coverage

install:
    pip install -r requirements.txt

test:
    pytest

coverage:
    pytest --cov=src/tests --cov-report=term-missing

clean:
    find . -type f -name '*.pyc' -delete
    find . -type d -name '__pycache__' -delete

all: clean coverage