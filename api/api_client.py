import requests
from requests import Response

class APIClient:
    def __init__ (self, api_key: str) -> None:
        self.base_url = "https://reqres.in/api"
        
        self.headers = {
            "Content-Type": "application/json",
            "x-api-key": api_key
        }
        
    def create_user(self, name: str, job: str) -> Response:
        payload = {
            "name": name,
            "job": job
        }
        
        response = requests.post(
            self.base_url + "/users", 
            json=payload,
            headers=self.headers)
        
        return response
    
    
    