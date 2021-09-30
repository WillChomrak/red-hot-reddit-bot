# Nashville Red Hot Bot

import praw
import os
from dotenv import load_dotenv

load_dotenv()
CLIENT_ID = os.getenv("PERSONAL_USE_SCRIPT")
CLIENT_SECRET = os.getenv("SECRET")
USER_AGENT = os.getenv("USER_AGENT")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=USER_AGENT, username=USERNAME, password=PASSWORD)

print(reddit.read_only)