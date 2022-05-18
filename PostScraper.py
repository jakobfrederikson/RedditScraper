import praw
import pandas as pd
import os
from dotenv import load_dotenv
from praw.reddit import Subreddit
load_dotenv(dotenv_path=os.path.abspath(os.getcwd()) + "\RedditTokens.env")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
USER_AGENT = os.getenv("USER_AGENT")

reddit_read_only = praw.Reddit(client_id=CLIENT_ID,
                               client_secret=CLIENT_SECRET,
                               user_agent=USER_AGENT)

posts_dict = { "Subreddit": [], "Title": []}

for post in reddit_read_only.subreddit("Showerthoughts+AskReddit").top(time_filter="year"):
    posts_dict["Subreddit"].append(post.subreddit)
    posts_dict["Title"].append(post.title)

top_posts = pd.DataFrame(posts_dict)
top_posts.to_csv("RedditTopPosts.csv", index=True)