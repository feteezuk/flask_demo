install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt &&\
			pip install python-dotenv &&\
				pip install hypothesis

lint:
	pylint --disable=R,C,W1203,W0702 app.py
test:
	python -m pytest


all: install lint 
