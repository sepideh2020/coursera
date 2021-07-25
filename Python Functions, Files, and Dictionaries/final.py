import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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


# read data
file_ref = open('project_twitter_data.csv', 'r')
data = file_ref.readlines()
print(data)

# write to the file
outfile = open('resulting_data.csv', 'w')
outfile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
outfile.write('\n')

for line in data[1:]:
    split = line.strip().split(",")
    res_row = ("{},{},{},{},{}".format(split[1], split[2], get_pos(split[0]), get_neg(split[0]),
                                       (get_pos(split[0]) - get_neg(split[0]))))
    outfile.write(res_row)
    outfile.write('\n')
outfile.close()



import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("resulting_data.csv")
fig,ax=plt.subplots()
my_scatter_plot=ax.scatter(df[" Net Score"],df["Number of Retweets"])
plt.show()

