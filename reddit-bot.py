# Nashville Red Hot Bot

import praw
import os
from dotenv import load_dotenv
import pprint

# Use dotenv to bring env vars from .env file
load_dotenv()
CLIENT_ID = os.getenv("PERSONAL_USE_SCRIPT")
CLIENT_SECRET = os.getenv("SECRET")
USER_AGENT = os.getenv("USER_AGENT")
R_USERNAME = os.getenv("R_USERNAME")
PASSWORD = os.getenv("PASSWORD")

# Create reddit instance
reddit = praw.Reddit(
    client_id=CLIENT_ID, 
    client_secret=CLIENT_SECRET, 
    user_agent=USER_AGENT, 
    username=R_USERNAME, 
    password=PASSWORD,
)

# Validate instance on submission
reddit.validate_on_submit = True

# Post a submission on r/test
# test_subr = reddit.subreddit("test")
# test_subr.submit("Red Hot Test Submission", "Yum") # Posts on test

# Comment on above post
# submission = reddit.submission(url="https://www.reddit.com/r/test/comments/q00bt2/red_hot_test_submission/")
# submission.reply("Yum")



# So what can I do with this now that its working?
# can get instances of subreddits and posts within those subreddits
# instances of authors
# comments on submissions

# pprint.pprint(dir(chicken)) # Used this to better understand the subreddit class

# Maybe I want to make it so the user can dl all the info about whatever subreddit they want.
# Then give them the option to output that as a csv? That could be cool. Then another project could be to
# that that info and do some data analysis on it.
