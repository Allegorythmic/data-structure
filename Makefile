.PHONY: test clean coverage install all

install:
    pip install -r requirements.txt

test:
    pytest

coverage:
    pytest --cov=src --cov-report=term-missing

clean:
    find . -type f -name '*.pyc' -delete
    find . -type d -name '__pycache__' -delete
    rm -rf htmlcov

all: clean coverage
