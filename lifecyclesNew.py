import praw


def get_life_cycle(comments):
    # Get days between first and second to last comments
    if len(comments) >= 3:
        earliest = (min(comments)) / 60 / 60 / 24
        comments.remove(max(comments))
        latest = (max(comments)) / 60 / 60 / 24
        life_cycle = latest - earliest
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


def lifecycles(hot_posts):

    # Get the average life cycle across all posts
    all_life_cycles = get_life_cycles(hot_posts)
    avg_life = sum(all_life_cycles) / len(all_life_cycles)

    print(avg_life)

    return all_life_cycles



