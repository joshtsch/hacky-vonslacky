from enum import Enum
import os
import requests
from src.lib.csv_helper import Csv


class Fider:
    def __init__(self, url):
        self.url = url

    class PostsTypes(Enum):
        MOST_DISCUSSED = 0
        MOST_WANTED = 1
        RECENT = 2
        TRENDING = 3

    def get_posts(self, posts_type):
        posts = Csv(os.path.join("csv", "posts.csv"))

        switch = {
            self.PostsTypes.MOST_DISCUSSED: posts.sort("comments_count", reverse=True),
            self.PostsTypes.MOST_WANTED: posts.sort("votes_count", reverse=True),
            self.PostsTypes.RECENT: posts.sort("created_at"),
            # @todo: How is trending calculated on fider? Update this.
            self.PostsTypes.TRENDING: posts.sort("votes_count", reverse=True),
        }
        return switch.get(posts_type)

    # @todo: make this work
    # https://requests-oauthlib.readthedocs.io/en/latest/oauth2_workflow.html
    def __export_posts(self):
        endpoint = "admin/export/posts.csv"
        r = requests.get(self.url + endpoint)

        if r.status_code != 200:
            raise ValueError(
                "Request to fider returned an error %s, the response is:\n%s"
                % (r.status_code, r.text)
            )

        return r

