import praw


def get_life_cycle(comments):
    # Get days between first and second to last comments
    earliest = (min(comments)) / 60 / 60 / 24
    comments.remove(max(comments))
    latest = (max(comments)) / 60 / 60 / 24
    life_cycle = latest - earliest
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


def main():
    client_id = '6f7hls-JAIfbtQ'
    client_secret = 'g-G5pPZ_Y6qsGAxJO3kE1wdeT34'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret, user_agent=user_agent)

    page = reddit.subreddit('osu')
    top_n_posts = page.top(limit=25)

    # Get the average life cycle across all posts
    all_life_cycles = get_life_cycles(top_n_posts)
    avg_life = sum(all_life_cycles) / len(all_life_cycles)

    print(avg_life)


if __name__ == "__main__":
    main()
