import requests

print('The version of requests library is %s'%requests.__version__)

homepage = requests.get("http://www.google.com/")
print("GET Google homepage\n", homepage.text)