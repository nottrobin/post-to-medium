# Standard library
import os
import json
from urllib.parse import urlparse

# Packages
import frontmatter
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
        response = self._request(
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

        posted_url = response.json()["data"]["url"]

        print(f"- Article posted to { posted_url }")

        return posted_url

    def post_markdown_file(self, filepath: str):
        with open(filepath) as markdown_file:
            markdown = markdown_file.read()



class MarkdownArticle:
    """
    
    """
    def __init__(self, filepath, canonical_url=None):
        self.filepath = filepath
        self.canonical_url = canonical_url

    def _get_metadata(self, key):
        parsed_article = frontmatter.load(self.filepath)

        return parsed_article.get(key)


    @property
    def title(self):
        return self._get_metadata("title")

    @property
    def tags(self):
        return self._get_metadata("tags")

    @property
    def posted_to(self):
        return self._get_metadata("posted_to")

    @property
    def markdown(self):
        parsed_article = frontmatter.load(self.filepath)

        markdown = parsed_article.content

        # If there's a canonical_url, add a line to the beginning to say so.
        if self.canonical_url:
            scheme = urlparse(self.canonical_url).scheme

            friendly_url = self.canonical_url.removeprefix(f"{scheme}://")

            markdown = (
                "_Originally posted at "
                f"[{ friendly_url }]({ self.canonical_url })_\n\n"
            ) + markdown

        return markdown

    def update_posted_to(self, url):
        """
        Update markdown article to mention where it was posted
        """

        domain = urlparse(url).netloc

        parsed_article = frontmatter.load(self.filepath)

        if "posted_to" in parsed_article:
            parsed_article["posted_to"]["domain"] = url
        else:
            parsed_article["posted_to"] = {domain: url}

        print("- Added 'medium.com' to 'posted_to' metadata")

        frontmatter.dump(parsed_article, self.filepath)



def markdown_to_medium(filepath, canonical_url=None):
    article = MarkdownArticle(filepath, canonical_url)

    if article.posted_to and "medium.com" in article.posted_to:
        print("- Article was already posted to medium.com")
        return

    posted_url = Medium().post_article(
        title = article.title,
        body = f"# {article.title}\n\n{ article.markdown }",
        tags = article.tags,
        canonical_url = article.canonical_url,
    )

    article.update_posted_to(posted_url)

    return posted_url
