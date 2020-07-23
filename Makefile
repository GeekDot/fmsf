.PHONY: clean

run:
	python manage.py run

test:
	coverage run --source='.' manage.py test
	coverage report
	coverage html

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete
	find . -type f -name '.coverage' -delete
	find . -type d -name 'htmlcov' | xargs rm -rf
	find . -type d -name '__pycache__' | xargs rm -rf

del:
	find . -type d -name 'migrations' | xargs rm -rf
