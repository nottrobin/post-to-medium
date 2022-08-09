# Publish markdown

Publish articles written in Markdown files to the following platforms:

- medium.com
<!--
- dev.to
- hashnode.com
- twitter.com
-->

Markdown files should include YAML frontmatter with at least a `title`. Adding `tags` will help your posts reach a wider audience on the target platforms:

```
---
title: Some title or other
tags: ["webdev", "writing"]
---

{content in Markdown}
```

I wrote this to cross-post article from [my own Jekyll blog](https://robinwinslow.uk), in a GitHub workflow (which I may yet publish as an action).

## Installation

``` bash
$ pip3 install publish-markdown
```

## Publishing to medium.com

``` bash
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

## Is cross-posting allowed / a good idea?

Cross-posting to extra platforms gets your post to be seen by more communities. This is mostly a good thing - people in one community are unlikely to also be in another simultaneously. 

While plainly duplicating content on the internet is not generally a good idea, cross-posting or syndicating is fine where it's done right. Dev.to, Medium and Hashnode all explicitly support cross-posting, by providing the ability to set a `rel=canonical` meta tag inside their posts. And [Google explicitly mention](https://developers.google.com/search/docs/advanced/crawling/consolidate-duplicate-urls) syndication of articles as a legitimate use of the `rel=canonical` tag.

So yes, cross-posting is a good idea.
