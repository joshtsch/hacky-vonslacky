import json
import requests


class Slack:
    def __init__(self, url):
        self.url = url

    def post(self, message):
        message = self.__format_message(message)

        r = requests.post(
            self.url,
            data=json.dumps(message),
            headers={"Content-Type": "application/json"},
        )

        if r.status_code != 200:
            raise ValueError(
                "Request to slack returned an error %s, the response is:\n%s"
                % (r.status_code, r.text)
            )

        return r.status_code

    def __format_message(self, message):
        return message
