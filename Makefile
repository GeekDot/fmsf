.PHONY: clean

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete
	find . -type f -name '.coverage' -delete
	find . -type d -name 'files' | xargs rm -rf
	find . -type d -name 'htmlcov' | xargs rm -rf
	find . -type d -name '__pycache__' | xargs rm -rf
	find . -type f -name 'demo.xlsx' | xargs rm -rf

test:
	coverage run --source='.' manage.py test
	coverage report
	coverage html

run:
	python manage.py run

docker-clean:
	docker stop vnet.service.sso
	docker rm vnet.service.sso
	docker image rm vnet.service.sso

docker-build:
	docker build -t vnet.service.sso .

docker-push:
	docker tag vnet.service.sso registry-intl.cn-hongkong.aliyuncs.com/paymarket/vnet.service.sso
	docker push registry-intl.cn-hongkong.aliyuncs.com/paymarket/vnet.service.sso

docker-run-dev:
	docker run -d -p 8000:8000 --name account -e RUNTIME_ENV=dev-docker vnet.service.sso

docker-login:
	docker login --username=heiyubaiclub@gmail.com registry-intl.cn-hongkong.aliyuncs.com