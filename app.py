from flask import Flask, render_template, request
import csv
import lifecyclesNew

app = Flask(__name__)

import praw

id = 'Ed-ggD3N-UMFZQ'
secret = 'f_TA7tTacndu7o58eSqT0kfQtKM'  # in the picture
agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
reddit = praw.Reddit(client_id=id, client_secret=secret, user_agent=agent)


def getData(name):
    page = reddit.subreddit(name)

    hot_posts = page.hot(limit=25)

    for post in hot_posts:
        with open("posts.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["subreddit"])
            writer.writerow({"subreddit": post.title})



@app.route("/")
def index():
    return render_template("index.html")



@app.route("/data")
def displaydata():
    with open("posts.csv", "r", newline='') as file:
        reader = csv.DictReader(file)
        posts = list(reader)
    return render_template("data.html", posts=posts)






@app.route("/analyze", methods=["POST"])
def register():

    sub = reddit.subreddits.search_by_name(request.form.get("subreddit"))
    if not sub.__len__():
        return render_template("failure.html")

    if not request.form.get("subreddit"):
        return render_template("failure.html")

    page = reddit.subreddit(request.form.get("subreddit"))
    hot_posts = page.hot(limit=25)

    with open("posts.csv", "a") as file:
        for post in hot_posts:
            writer = csv.DictWriter(file, fieldnames=["subreddit"])
            writer.writerow({"subreddit": post.title})




    with open("posts.csv", "r", newline='') as file:
        reader = csv.DictReader(file)
        posts = list(reader)
    return render_template("data.html", posts=posts)







if __name__ == '__main__':
    app.run()
