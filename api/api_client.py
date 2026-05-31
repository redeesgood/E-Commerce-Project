import requests
from requests import Response


class APIClient:
    def __init__(self, api_key: str) -> None:
        self.base_url = "https://reqres.in/api"

        self.headers = {"Content-Type": "application/json", "x-api-key": api_key}

    def create_user(self, name: str, job: str) -> Response:
        payload = {"name": name, "job": job}

        response = requests.post(
            self.base_url + "/users", json=payload, headers=self.headers
        )

        return response

    def get_user(self, user_id: int) -> Response:
        response = requests.get(
            self.base_url + f"/users/{user_id}", headers=self.headers
        )

        return response

    def delete_user(self, user_id: int) -> Response:
        response = requests.delete(
            self.base_url + f"/users/{user_id}", headers=self.headers
        )

        return response

    def patch_user(self, user_id: int, name: str, job: str) -> Response:
        payload = {"name": name, "job": job}

        response = requests.patch(
            self.base_url + f"/users/{user_id}", json=payload, headers=self.headers
        )

        return response
