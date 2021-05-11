install:
	poetry install

test:
	poetry run pytest tests --cov=page_loader

lint:
	poetry run flake8 page_loader

selfchek:
	poetry check

check: selfchek test lint

build: check
	poetry build

package-install:
	pip install --user dist/*.whl

.PHONY install test lint selfchek check build package-install
