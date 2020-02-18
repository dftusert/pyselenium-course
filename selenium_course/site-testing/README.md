requirements:<br />
python3<br />
webdriver - geckodriver (for firefox) or/and chromedriver (for google chrome)<br />
<br />
pip freeze > requirements.txt:<br />
atomicwrites==1.3.0<br />
attrs==19.3.0<br />
more-itertools==8.2.0<br />
packaging==20.1<br />
pluggy==0.13.1<br />
py==1.8.1<br />
pyparsing==2.4.6<br />
pytest==5.1.1<br />
pytest-rerunfailures==7.0<br />
selenium==3.14.0<br />
six==1.14.0<br />
urllib3==1.25.8<br />
wcwidth==0.1.8<br />
<br />
usage:<br />
pytest --browser_name=<name> --language=<lang><br />
where:<br />
name - chrome or firefox<br />
language - language code, that will be try to use
