.PHONY: setup_env up down log db clean_db test deps redis clean_redis 
setup_env:
	pip3 install virtualenv
	virtualenv hostpital_management_backend

deps:
	pip3 install -r requirements-dev.txt
	pip3 install -r requirements.txt

db:
	docker run -p5432:5432 --name=dev_hospital_management_db -d -e POSTGRES_USER=dev_user -e POSTGRES_PASSWORD=secret -e POSTGRES_DB=dev_hospital_management postgres:13

clean_db:
	docker stop dev_hospital_management_db
	docker rm dev_hospital_management_db

redis:
	docker run -p6379:6379 --name=dev_hospital_management_redis -d redis:alpine3.19

clean_redis:
	docker stop dev_hospital_management_redis
	docker rm dev_hospital_management_redis

up: db redis
	docker build -t hospital_management_backend .
	docker run -p 8000:8000 --name=hospital_management_backend --link dev_hospital_management_db:database --link dev_hospital_management_redis:redis -d hospital_management_backend

down: clean_db clean_redis
	docker stop hospital_management_backend
	docker rm hospital_management_backend

log:
	docker logs -f hospital_management_backend

test:
	cd ./src && PYTHONPATH=./ pytest  --disable-warnings