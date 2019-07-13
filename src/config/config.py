"""Load environmental variables into configuration."""
import os

from dotenv import load_dotenv
load_dotenv()

slack_api = {
    "webhook_url": str(os.getenv("SLACK_WEBHOOK_URL"))
}