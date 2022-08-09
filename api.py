# Standard library
import argparse
import os
import json

# Packages
import requests


class Medium:
    def __init__(self):
        self.token = os.environ["MEDIUM_TOKEN"]
        self.user_id = os.environ.get("MEDIUM_USER_ID")

        if not self.user_id:
            self.user_id = self.get_user_id()

    def _request(self, url: str, method: str = "get", data: dict = {}):
        response = requests.request(
            url=url,
            method=method,
            data=json.dumps(data),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.token}",
            }
        )
        response.raise_for_status()
        return response

    def get_user_id(self):
        response = self._request(url="https://api.medium.com/v1/me")

        user_id = response.json()["data"]["id"]

        print(f"Found user ID: {user_id}")

        return user_id

    def post_article(self, title: str, body: str, tags: list = [], canonical_url: str = None):
        return self._request(
            url=f"https://api.medium.com/v1/users/{self.user_id}/posts",
            method="post",
            data={
                "title": title,
                "contentFormat": 'markdown',
                "content": body,
                "canonicalUrl": canonical_url,
                "tags": tags,
                "publishStatus": 'public',
            }
        )
