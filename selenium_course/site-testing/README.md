requirements:
python3
webdriver - geckodriver (for firefox) or/and chromedriver (for google chrome)

pip freeze > requirements.txt:
atomicwrites==1.3.0
attrs==19.3.0
more-itertools==8.2.0
packaging==20.1
pluggy==0.13.1
py==1.8.1
pyparsing==2.4.6
pytest==5.1.1
pytest-rerunfailures==7.0
selenium==3.14.0
six==1.14.0
urllib3==1.25.8
wcwidth==0.1.8

usage:
pytest --browser_name=<name> --language=<lang>
where:
name - chrome or firefox
language - language code, that will be try to use
