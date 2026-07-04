from api.base_api import BaseApi

class UsersApi(BaseApi):

    def get_all_users(self):
        return self.get("/users")
    
    def get_user(self, id_user):
        return self.get(f"/users/{id_user}")