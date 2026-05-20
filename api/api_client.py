import requests
from requests import Response

class APIClient:
    def __init__ (self):
        self.base_url = "https://reqres.in/api"
        
    def create_user(self, name: str, job: str) -> Response:
        payload = {
            "name": name,
            "job": job
        }
        
        response = requests.post(self.base_url + "/users", json=payload)
        return response
    
    
    