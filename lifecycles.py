import praw
from datetime import datetime


def get_life_cycle(comments):
    # Get days between first and second to last comments
    if len(comments) >= 3:
        earliest = datetime.fromtimestamp(min(comments))
        comments.remove(max(comments))
        latest = datetime.fromtimestamp(max(comments))
        life_cycle = (latest - earliest).days
    else:
        life_cycle = 1

    return life_cycle


def get_life_cycles(top_posts):
    all_posts_comments = []

    # Store all comments for each post
    for post in top_posts:
        post.comments.replace_more(limit=None)
        posts_comments = []
        for comment in post.comments.list():
            posts_comments.append(comment.created_utc)
        all_posts_comments.append(posts_comments)

    life_cycles = []

    # Get the life cycle for each post
    for post in all_posts_comments:
        post_life = get_life_cycle(post)
        life_cycles.append(post_life)

    return life_cycles


def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


def main():

    # Setup connection to PRAW API
    client_id = '6f7hls-JAIfbtQ'
    client_secret = 'g-G5pPZ_Y6qsGAxJO3kE1wdeT34'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret, user_agent=user_agent)

    # Get the hottest 25 posts on a subreddit
    sub_name = "osu"
    page = reddit.subreddit(sub_name)
    hot_n_posts = page.hot(limit=25)

    # Get the average life cycle across all posts
    all_life_cycles = get_life_cycles(hot_n_posts)
    avg_life = sum(all_life_cycles) / len(all_life_cycles)
    avg_life = truncate(avg_life, 2)
    print("The average lifespan of the hottest 25 posts on "
          "r/", sub_name, " is ", avg_life, " days.")


if __name__ == "__main__":
    main()
