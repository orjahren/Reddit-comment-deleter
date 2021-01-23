import praw

reddit = praw.Reddit(client_id='CLIENT_ID',
                     client_secret='CLIENT_SECRET',
                     password='PWD',
                     user_agent='Reddit-comment-deleter',
                     username='USERNAME')

r = reddit.user.me()

print("Starting to delete your comments")
for c in r.comments.new(limit=None):
	if(c.score < THRESHOLD):
		c.delete()
