import praw
import time

reddit = praw.Reddit(
    client_id="CLIENT_ID",
    client_secret="SECRET_KEY",
    user_agent="<USER_AGENT",
    username="USERNAME",
    password="PASSWORD"
)

subreddit = reddit.subreddit("gaming")

for submission in subreddit.new(limit=50):
    ##print("--------------")
    ##print(submission.title)

    reply = "thank you for your service"

    for comment in submission.comments:
        if hasattr(comment, "body"):
            lower_comment = comment.body.lower()
            if "call of duty" in lower_comment:
                print(lower_comment)
                comment.reply(reply)
                time.sleep(660)
