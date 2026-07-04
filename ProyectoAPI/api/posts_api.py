from api.base_api import BaseApi

class PostsApi(BaseApi):

    def create_post(self, body):
        return self.post("/posts", body)
    
    def delete_post(self, id_post):
        return self.delete(f"/posts/{id_post}")