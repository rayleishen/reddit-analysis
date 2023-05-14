#rayleishen_dev

import praw

# Read-only instance
reddit_read_only = praw.Reddit(client_id="",         # your client id
                               client_secret="",      # your client secret
                               user_agent="")        # your user agent
 
# Authorized instance
#reddit_authorized = praw.Reddit(client_id="",         # your client id
#                                client_secret="",      # your client secret
#                                user_agent="",        # your user agent
#                                username="",        # your reddit username
#                                password="")        # your reddit password

subreddit = reddit_read_only.subreddit("redditdev")
 
# Display the name of the Subreddit
print("Display Name:", subreddit.display_name)
 
# Display the title of the Subreddit
print("Title:", subreddit.title)
 
# Display the description of the Subreddit
print("Description:", subreddit.description)