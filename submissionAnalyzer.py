# This program analyzes words and username that appears in top 25 posts (title and body)
import re
import praw

#common words should be taken out of the file
commonWords = ['the', 'in', 'on', 'a', 'an', 'to', 'from', 'for', 'that', 'it', 'as', 'at', 'is', 'are', 'am', 'can',
               'be', 'was', 'were', 'and', 'or', 'he', 'she', 'of', 'by', 'they', 'we','i', 'my', 'have', 'if', 'will']
# garbage is usually is going to be at the end of the word.
garbage =['.',',','?','!']
# This function will get rid of the garbage from the filter
def filter(str, separators):
    j = 0 # increment to 4
    i = -1 # index of garbages if not -1
    while i==-1 and j<4:
        i = str.find(separators[j])
        j += 1
    #At this point, if i != -1, we need to get rid of the garbage
    if i != -1:
        str = str[0:i]
    return str



id = #
secret = # #in the picture
agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'

#look up "what's my user agent" on google
reddit = praw.Reddit(client_id = id, client_secret = secret, user_agent = agent)

#Also create output files to write to
outputFile = open(r'output.txt', 'w+') #this will save all words from top 25 posts and top 3 comments from each post
userOutput = open(r'outputUsers.txt', 'w+') #this will save all user names of top 25 posts and top 3 comments of each

#Code below should ask the user for a subreddit to examine
#then print the headcount of subscribers
subredditName = input("Which subreddit's top25 posts you wanna examine?")
page = reddit.subreddit(subredditName)
headCount = page.subscribers
print('this subreddit has headcount of: ', headCount)

#Code below prints the username of the top 25 post and top 3 comments of each
top_posts = page.top('day',limit = 25)
for posts in top_posts:
    userOutput.write(str(posts.author))
    userOutput.write(',')
#DON'T CHANGE! FURTHER ANALYZE USING R or PYTHON

print('Finished outputting user names')

#Now print words from title, body of top 25 submission and top 3 comments of each posts
top_posts2 = page.top('day',limit = 25)
for post in top_posts2:

    title = post.title
    postBody = post.selftext
    titleWords = title.split()
    bodyWords = postBody.split()

#process the words in the title
    for tword in titleWords:
        newword = filter(tword, garbage)
        if newword.isalnum() and newword not in commonWords:
            outputFile.write(newword.lower())
            outputFile.write(',')
#proces the words in the body
    for bword in bodyWords:
        newword = filter(bword, garbage)
        if newword.isalnum() and newword not in commonWords:
            outputFile.write(newword.lower())
            outputFile.write(',')



#add a ' ' and a new line at the end so the files don't end with comma
outputFile.write(' ')
userOutput.write(' ')
outputFile.write('\n')
userOutput.write('\n')

#close files
outputFile.close() # this should be after I process the file
userOutput.close()

print('Finished writing output file!')
