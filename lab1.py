import requests

'''virtualenv step4'''
print("The viersion of requests library is %s" % requests.__version__)

'''curl step5'''
homepage = requests.get("http://www.google.com/")
# print("GET Google Homepage\n",homepage)

'''curl step10'''
code_url = "https://raw.githubusercontent.com/XZPshaw/CMPUT404LAB1/main/lab1.py"
code_file = requests.get(code_url, stream=True)
# print script from github
print(code_file.text)
# download and save 
with open("downloaded_lab1_zepeng.py", "wb") as code:
    code.write(code_file.content)
