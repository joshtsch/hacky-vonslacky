#!/usr/bin/env python3
from src.config import config
from src.fider import Fider
from src.slack import Slack

slack = Slack(config.slack_api["webhook_url"])
kbra_ideas = Fider(config.fider["url"])
data = kbra_ideas.get_posts(Fider.PostsTypes.MOST_WANTED)

slack.post({"text": "Hello, World!"})
