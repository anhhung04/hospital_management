.PHONY: setup_env up down log db clean_db test deps redis clean_redis 
setup_env:
	pip3 install virtualenv --break-system-packages
	python3 -m virtualenv .venv

deps:
	pip3 install -r requirements-dev.txt
	pip3 install -r requirements.txt

db:
	docker run -p5432:5432 --name=dev_hospital_management_db -d -e POSTGRES_USER=dev_user -e POSTGRES_PASSWORD=secret -e POSTGRES_DB=dev_hospital_management postgres:13

clean_db:
	docker rm -f dev_hospital_management_db

redis:
	docker run -p6379:6379 --name=dev_hospital_management_redis -d redis:alpine3.19

clean_redis:
	docker rm -f dev_hospital_management_redis

log:
	docker logs -f hospital_management_backend

test:
	cd ./app && PYTHONPATH=./ pytest  --disable-warnings

migrate-all:
	cd ./app && PYTHONPATH=./ alembic upgrade head

migrate-new:
	@echo "Enter migration message: "; \
	read message; \
	cd ./app && alembic revision --autogenerate -m "$$message"

migrate-downgrade:
	cd ./app && alembic downgrade -1

migrate-history:
	cd ./app && alembic history --verbose--verbose

clean: clean_db clean_redis
	rm -rf ./**/__pycache__ .pytest_cache ./**/.mypy_cache ./**/.pytest_cache ./**/.coverage ./**/.coverage.* ./**/**/__pycache__ ./**/**/**/__pycache__
clean-all: clean
	rm -rf ./hostpital_management_backend

up: db redis
	docker build -t hospital_management_backend -f Dockerfile.debug .
	docker run -p 8000:8000 -p8888:8888 --name=hospital_management_backend --link dev_hospital_management_db:database --link dev_hospital_management_redis:redis -d hospital_management_backend

down: clean_db clean_redis
	docker rm -f hospital_management_backend

rebuild: down up

dev: deps db redis

up-migrate: up migrate-all