# 1.To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for strings.)
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


def strip_punctuation(word):
    new_word = word
    for char in word:
        if char in punctuation_chars:
            new_word = new_word.replace(char, '')
    return new_word


# 2.Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered positive words. Use the list, positive_words to determine what words will count as positive. The function should return a positive integer - how many occurrences there are of positive words in the text. Note that all of the words in positive_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


def strip_punctuation(word):
    new_word = word
    for char in word:
        if char in punctuation_chars:
            new_word = new_word.replace(char, '')
    return new_word
def get_pos(string):
    counter=0
    new_string=strip_punctuation(string)
    for word in new_string.split():
        if word.lower() in positive_words:
            counter=counter+1
    return counter

#3.Next, copy in your strip_punctuation function and define a function called get_neg which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered negative words. Use the list, negative_words to determine what words will count as negative. The function should return a positive integer - how many occurrences there are of negative words in the text. Note that all of the words in negative_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(word):
        new_word=word
        for char in word:
            if char in punctuation_chars:
                new_word=new_word.replace(char,'')
        return new_word
def get_neg(string):
    counter=0
    new_string=strip_punctuation(string)
    for word in new_string.split():
        if word.lower() in  negative_words:
            counter=counter+1
    return counter



#4.Finally, copy in your previous functions and write code that opens the file project_twitter_data.csv which has the fake generated twitter data (the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet). Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. Copy the code from the code windows above, and put that in the top of this code window. Now, you will write code to create a csv file called resulting_data.csv, which contains the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score (how positive or negative the text is overall) for each tweet. The file should have those headers in that order. Remember that there is another component to this project. You will upload the csv file to Excel or Google Sheets and produce a graph of the Net Score vs Number of Retweets. Check Coursera for that portion of the assignment, if you’re accessing this textbook from Coursera.


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
def strip_punctuation(word):
    new_word = word
    for char in word:
        if char in punctuation_chars:
            new_word = new_word.replace(char, '')
    return new_word


def get_pos(string):
    counter = 0
    new_string = strip_punctuation(string)
    for word in new_string.split():
        if word.lower() in positive_words:
            counter = counter + 1
    return counter


def get_neg(string):
    counter = 0
    new_string = strip_punctuation(string)
    for word in new_string.split():
        if word.lower() in negative_words:
            counter = counter + 1
    return counter
#read data
file_ref=open('project_twitter_data.csv','r')
data=file_ref.readlines()
print(data)

#write to the file
outfile=open('resulting_data.csv','w')
outfile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
outfile.write('\n')


for line in data[1:]:
    splt=line.strip().split(",")
    res_row=("{},{},{},{},{}".format(splt[1], splt[2], get_pos(splt[0]), get_neg(splt[0]), (get_pos(splt[0])-get_neg(splt[0]))))
    outfile.write(res_row)
    outfile.write('\n')
outfile.close()


