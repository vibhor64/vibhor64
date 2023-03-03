import praw
import pandas as pd

reddit_read_only = praw.Reddit(client_id="_8nO5QsB95hHFxNstUTWcw",		 # your client id
							client_secret="a6RN-49DdN9r4q5DlNvQn7nbaHHKrQ",	 # your client secret
							user_agent="Vibhor_Sharma")	 # your user agent


# subreddit = reddit_read_only.subreddit("wallstreetbets")

url = "https://www.reddit.com/gallery/u3fpqo"
 
# Creating a submission object
submission = reddit_read_only.submission(url=url)

print(submission.link_flair_text)