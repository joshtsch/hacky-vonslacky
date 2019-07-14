from enum import Enum
import os
import requests
from src.lib.csv_helper import Csv


class Fider:
    def __init__(self, url):
        self.url = url

    class PostSorting(Enum):
        MOST_DISCUSSED = 0
        MOST_WANTED = 1
        RECENT = 2
        TRENDING = 3

    def get_posts(self, post_sorting):
        posts = Csv(os.path.join("csv", "posts.csv"))

        switch = {
            self.PostSorting.MOST_DISCUSSED: posts.sort("comments_count", reverse=True),
            self.PostSorting.MOST_WANTED: posts.sort("votes_count", reverse=True),
            self.PostSorting.RECENT: posts.sort("created_at"),
            # @todo: How is trending calculated on fider? Update this.
            self.PostSorting.TRENDING: posts.sort("votes_count", reverse=True),
        }
        return switch.get(post_sorting)

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

