import json
import aiohttp
import ujson

class APIController():
    
    def __init__(self, url:str):
        self.URL = {
            "AUTH": url + "/api/auth",
            "USER": url + "/api/user/",
            "SEARCH": url + "/api/user/search/",
            "POINT": url + "/api/point/user/",
            "POINT_INCREMENT": url + "/api/point/user/increment/"
        }
        
        self.token = ""
        self.__timeout = 10
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer" + self.token
        }
    
        self.clientTimeout = aiohttp.ClientTimeout(total=None, sock_connect=self.__timeout, sock_read=self.__timeout)
        self.sessionClient = aiohttp.ClientSession(json_serialize=ujson.dumps, timeout=self.clientTimeout)
        
    async def authUser(self, data) -> aiohttp.ClientResponse:
        try:
            modifiedHeader = self.headers
            del modifiedHeader["Authorization"]
            
            async with self.sessionClient.post(self.URL["AUTH"], json=data, headers=modifiedHeader) as request:
                if request.status == 200:
                    return await request.json()
                return request
        except aiohttp.client_exceptions.InvalidURL:
            print("URL API INVÁLIDA")
            pass
        
        
    def __updateToken__(self):
        self.headers["Authorization"] = "Bearer " + self.token
        
    
    async def getUsers(self) -> aiohttp.ClientResponse:
        self.__updateToken__()
        try:
            async with self.sessionClient.get(self.URL["USER"], headers=self.headers) as request:
                if request.status == 200:
                    return await request.json()
                return request
        except aiohttp.client_exceptions.InvalidURL:
            print("URL API INVÁLIDA")
            pass
    
    ''' 
    
    def createUser(self, data) -> requests.Request:
        self.__updateToken__()
        request = requests.post(
            self.URL["USER"], timeout=self.__timeout, headers=self.headers, json=data
        )
        return request
    
    
        
    def getPoints(self) -> requests.Request:
        self.__updateToken__()
        request = requests.get(
            self.URL["POINT"], timeout=self.__timeout, headers=self.headers
        )
        return request
    
    def incrementPoints(self, id, data) -> requests.Request:
        self.__updateToken__()
        request = requests.post(
            self.URL["POINT_INCREMENT"] + str(id), timeout=self.__timeout, headers=self.headers, json=data
        )
        return request '''
