install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt &&\
			pip install python-dotenv

lint:
	pylint --disable=R,C,W1203,W0702 app.py


all: install lint 
