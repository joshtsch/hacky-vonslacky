#!/usr/bin/env python3
from src.config import config
from src.lib import datetime_helper
from src.fider import Fider
from src.slack import Slack

CHAR_LIMIT = 250
MESSAGES_SHOWN = 3
kbra_ideas = Fider(config.fider["url"])
slack = Slack(config.slack_api["webhook_url"])


def format_hacky_message(message_data):
    today = datetime_helper.day_of_week(datetime_helper.today())
    salutation = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*@here :salute: Happy %s Hackathoners!*\nCheck out the current trending topics for the upcoming hackathon."
            % (today),
        },
    }
    divider = {"type": "divider"}
    message_block = slack.format_message_block(salutation)
    message_block = slack.format_message_block(divider, message_block)

    for message in message_data[0:MESSAGES_SHOWN]:
        thumbs = []
        for vote in range(0, int(message["votes_count"])):
            thumbs.append("👍")
        thumbs = "".join(thumbs)
        next_message = {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*%s*\n\n%s\n\n%s"
                % (message["title"], thumbs, message["description"]),
            },
        }
        next_message_meta = {
            "type": "context",
            "elements": [
                {"type": "mrkdwn", "text": "*Author:* %s" % (message["created_by"])}
            ],
        }
        message_block = slack.format_message_block(next_message, message_block)
        message_block = slack.format_message_block(next_message_meta, message_block)
        message_block = slack.format_message_block(divider, message_block)

    footer = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*View all Hackathon ideas and more 👉👉 <%s|KBRA AppDev Ideas>*"
            % (kbra_ideas.url),
        },
    }
    message_block = slack.format_message_block(footer, message_block)

    return message_block


data = kbra_ideas.get_posts(Fider.PostsTypes.MOST_WANTED)
slack.post(format_hacky_message(data))

