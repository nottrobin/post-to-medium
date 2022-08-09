# post-to-medium

This package is purely for posting articles to Medium.

I'm using it t cross-post articles from [my blog](https://robinwinslow.uk) to [my Medium account](https://medium.com/@nottrobin) with a GitHub action.

## Installation

``` bash
pip3 install post_to_medium
```

## Permissions

All you really need is an "integration token" from [the Medium settings page](https://medium.com/me/settings), and then provide this with the `MEDIUM_TOKEN` environment variable, e.g.:

``` bash
export MEDIUM_TOKEN=<YOUR_TOKEN_GOES_HERE>
```

## Usage

``` python3
post_to_medium \
  --title="A new post" \
  --body="# A new post\n\nThis is a new post, written in Markdown" \
  --canonical-url="https://my.blog/a-new-post" \
  --tag=technology --tag=writing
```
