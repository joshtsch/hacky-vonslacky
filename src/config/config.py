"""Load environmental variables into configuration."""
import os

from dotenv import load_dotenv

load_dotenv()

auth0 = {
    "domain": str(os.getenv("AUTH0_DOMAIN")),
    "client_id": str(os.getenv("AUTH0_CLIENT_ID")),
    "client_secret": str(os.getenv("AUTH0_CLIENT_SECRET")),
}
fider = {"url": str(os.getenv("FIDER_URL"))}
slack_api = {"webhook_url": str(os.getenv("SLACK_WEBHOOK_URL"))}
