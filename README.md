[![Flask demo - Continuous Deployment Microservice Test](https://github.com/feteezuk/flask_demo/actions/workflows/main.yml/badge.svg)](https://github.com/feteezuk/flask_demo/actions/workflows/main.yml)

# flask_demo
Small Flask Microservice that makes an API call to Open Weather Map, and brings back information about current weather information for Specified City. 

*Coursera Lab:  duke-coursera-ccb-lab2*



## Invoke Endpoint

* Create virtualenv and source it: `python3 -m venv ~/.fcm && source ~/.venv/bin/fcm`
* Install and Test:  `make all`
* Run it:  `python app.py`

# You will get the message :

* Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://[PORT ADDRESS]
 * Restarting with watchdog (fsevents)
 * Debugger is active!
 * Debugger PIN: ****
 * I am inside hello world

# Go to browser, and type in 
* http://[PORT ADDRESS]/change

# Go to name_the_city_to_search_for.py file and type in city name, then refresh browser. You should get city weather information. 







