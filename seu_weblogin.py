 #!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import httplib
import json
import sys

headers = {
    'Content-Type': "application/json; charset=utf-8",
    'dataType': "json",
    'cache': False
    }
url = "w.seu.edu.cn"
login_url = "/portal/login.php"
logout_url = "/portal/logout.php"

def print_result(content):
    if 'error' in content:
        dresq = eval(content.encode('utf-8'))
        print "Error:" + unicode(dresq["error"]).decode('unicode-escape')
    else:
        dresq = eval(content.replace('null',"'w.seu.edu.cn'").encode('utf-8'))
        # print username & IP address
        print "username: " + username
        print "IP Address: " + dresq['login_ip']

def login(username, password):
    global headers, login_url, url
    params ={'username': username, 'password':password}
    conn = httplib.HTTPSConnection(url)
    conn.request("POST", login_url,  urllib.urlencode(params), headers=headers)
    content = conn.getresponse().read()
    # remove useless header
    content = content[5:]
    print print_result(content)
    conn.close()
    

    # print "Login fail!!!"
def logout():
    global headers, url, logout_url
    conn = httplib.HTTPSConnection(url)
    conn.request("POST",logout_url,headers=headers)
    conn.close()
    print "Logout Sucess!!"

def login_basedon_request(username, password):
    "login code base on requests(lib), which need installation"
    import requests
    URL = 'https://w.seu.edu.cn/portal/login.php'
    # params = {'username': unicode(username).encode('utf-8'), 'password': unicode(password).encode('utf-8')}
    params = {'username': username, 'password': password}
    resq = requests.post(URL, data=urllib.urlencode(params), allow_redirects=True, headers=headers)
    content = resq.text 
    print print_result(content)

if __name__ == '__main__':
    username = 'your_username'
    password = 'your_password'

    # login(username, password)
    # logout()
    # login_basedon_request(username, password)
	
    print sys.argv
    if sys.argv[1] == 'login':
        login(username, password)
    elif sys.argv[1] == 'logout':
        logout()
    else:
        login_basedon_request(username,password)
