# This program should calculate the font size based on
# the count of the words in the dictionaries

# creating a file and list for words and users
wordFile = open("output.txt", "r+")
wordList = wordFile.read().split(',')
idFile = open("outputUsers.txt", "r+")
idList = idFile.read().split(',')

# process wordList and create a dict with counts
wordMap = {}
for word in wordList:
    if word not in wordMap:
        wordMap[word] = 1
    else:
        wordMap[word] += 1

# process userList and create a dict with counts
userMap = {}
for user in idList:
    if user not in userMap:
        userMap[user]=1
    else:
        userMap[user] += 1


# this function should take in a map with word and counts, and return a dictionary with word and font_size
def fontCalc(dict):
    maxFont = 48
    minFont = 11
    maxCount = 0
    minCount = 100
    for keys in dict:
        if dict[keys] > maxCount:
            maxCount = dict[keys]
        if dict[keys] < minCount:
            minCount = dict[keys]
    # At this point, max and min counts are correct values

    resultDict = {}

    for key in dict:
        fontSize = (maxFont-minFont) * (dict[key]-minCount+1)/(maxCount-minCount+1)
        resultDict[key] = int(fontSize+minFont)

    return resultDict

#Call fontCalc to generate a map with words and fontsizes
userFontSizes = fontCalc(userMap)
wordFontSizes = fontCalc(wordMap)


print(nima)
