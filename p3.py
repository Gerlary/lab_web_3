import requests

class Http_client:
    def __int__(self,host):
        self.s = requests.Session()
        self.host = host


    def __del__(self):
        self.s.close()

