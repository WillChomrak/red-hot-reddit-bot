# Nashville Red Hot Bot

import praw
import os
from dotenv import load_dotenv

load_dotenv()
test = os.getenv("TEST")

reddit = praw.Reddit(client_id="", client_secret="", password="", user_agent="", username="")