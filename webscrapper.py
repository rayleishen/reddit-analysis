import praw, json
import pandas as pd
from praw.models import MoreComments

with open('config.json') as config_file:
    data = json.load(config_file)

c_id = data['client_id']
c_s = data['client_s']
u_a = data['user_a']

# Read-only instance
reddit_read_only = praw.Reddit(client_id=c_id,         # your client id
                               client_secret=c_s,      # your client secret
                               user_agent=u_a)        # your user agent

#----------------------------------------------------------------------------------------------

subreddit = reddit_read_only.subreddit("redditdev")
 
# Display the name of the Subreddit
print("Display Name:", subreddit.display_name)
 
# Display the title of the Subreddit
print("Title:", subreddit.title)
 
# Display the description of the Subreddit
print("Description:", subreddit.description)

posts = subreddit.top(time_filter="month", limit=5)
# Scraping the top posts of the current month
 
posts_dict = {"Title": [], "Post Text": [],
              "ID": [], "Score": [],
              "Total Comments": [], "Post URL": []
              }


#----------------------------------------------------------------------------------------------

subreddit = reddit_read_only.subreddit("Python")
 
for post in subreddit.hot(limit=5):
    print(post.title)
    print() 

for post in posts:
    # Title of each post
    posts_dict["Title"].append(post.title)
     
    # Text inside a post
    posts_dict["Post Text"].append(post.selftext)
     
    # Unique ID of each post
    posts_dict["ID"].append(post.id)
     
    # The score of a post
    posts_dict["Score"].append(post.score)
     
    # Total number of comments inside the post
    posts_dict["Total Comments"].append(post.num_comments)
     
    # URL of each post
    posts_dict["Post URL"].append(post.url)
 
# Saving the data in a pandas dataframe
top_posts = pd.DataFrame(posts_dict)
top_posts
 
top_posts.to_csv("Top Posts.csv", index=True)

#----------------------------------------------------------------------------------------------

# URL of the post
url = "https://www.reddit.com/r/IAmA/comments/m8n4vt/im_bill_gates_cochair_of_the_bill_and_melinda/"
 
# Creating a submission object
submission = reddit_read_only.submission(url=url)

post_comments = []
 
for comment in submission.comments:
    if type(comment) == MoreComments:
        continue
 
    post_comments.append(comment.body)
 
# creating a dataframe
comments_df = pd.DataFrame(post_comments, columns=['comment'])
comments_df

comments_df.to_csv("comments_df.csv", index=True)

