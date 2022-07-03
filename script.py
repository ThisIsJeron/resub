import praw

reddit = praw.Reddit(
    client_id="INSERT_CLIENT_ID",
    client_secret="INSERT_CLIENT_SECRET",
    password="INSERT_USER_PASSWORD",
    user_agent="testscript by u/d4rkr4in",
    username="INSERT_USERNAME",
)

subs = open("subs.txt", "r")
counter = 0 
for x in subs:
    sub = x.split(">")
    sub = sub[1][:-3]
    reddit.subreddit(sub).subscribe()
    print("Subscribed to " + sub + "!")
    counter += 1
    
print("Job complete, you have resubscribed to " + counter + "subs!")

