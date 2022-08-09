# Publish markdown

Publish articles written in Markdown files to the following platforms:

- medium.com
<!--
- dev.to
- hashnode.com
- twitter.com
-->

Markdown files should include YAML frontmatter with at least a `title`:

```
---
title: Some title or other
---

{content in Markdown}
```

I wrote this to cross-posting article from [my own Jekyll blog](https://robinwinslow.uk), in a GitHub workflow (which I may yet publish as an action).

## Publishing to medium.com

``` bash
$ pip3 install publish-markdown
$ export MEDIUM_TOKEN={your-integration-token}
$ publish-to-medium _posts/2022-01-01-my-first-post.md --canonical-url="https://my-blog.com/2022/01/02/my-first-post"
Found user ID: {your-user-id}
- Article posted to https://medium.com/@nottrobin/how-to-use-unix-linkchecker-to-thoroughly-check-any-site-50134f3aeba0
- Added 'medium.com' to 'posted_to' metadata
```

### Optimisations

You can avoid the code having to retrieve your user ID every time by setting it as an environment variable as well:

``` bash
export MEDIUM_USER_ID={your-user-id}
```
