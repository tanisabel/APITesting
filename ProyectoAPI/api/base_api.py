import requests

class BaseApi:

    BASE_URL = "https://jsonplaceholder.typicode.com"

    def get(self, endpoint):
        return requests.get(f"{self.BASE_URL}{endpoint}")

    def post(self, endpoint, body):
        return requests.post(
            f"{self.BASE_URL}{endpoint}",
            json=body
        )
    
    def put(self, endpoint, body):
        return requests.post(
            f"{self.BASE_URL}{endpoint}",
            json=body
        )
    
    def delete(self, endpoint):
        return requests.delete(f"{self.BASE_URL}{endpoint}")