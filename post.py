import requests

API_ENDPOINT = "https://api.npoint.io/c790b4d5cab58020d391"

class Post:
    
    def __init__(self):

        self.posts = self.get_all_blog_posts()

    def get_all_blog_posts(self) -> dict:

        response = requests.get(API_ENDPOINT)

        data = response.json()

        return data 

    def get_post_by_id(self, post_id) -> dict:
        """
            This method is used for filtering post based on ID
        """

        return [post for post in self.posts if post["id"] == post_id]
