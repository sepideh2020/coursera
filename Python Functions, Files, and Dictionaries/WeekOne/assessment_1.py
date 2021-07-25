# 1.The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the variable num.
text_file = open('travel_plans.txt', 'r')
num = len(text_file.read())
text_file.close()
# 2.We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words.
text_file = open('emotion_words.txt', 'r')
lines = text_file.readlines()
num_words = 0
for line in lines:
    num_words += len(line.split())

text_file.close()
# second solution
num_words = 0
fileref = "emotion_words.txt"

with open(fileref, 'r') as file:
    for line in file:
        num_words += len(line.split())

# 3.Assign to the variable num_lines the number of lines in the file school_prompt.txt.
with open('school_prompt.txt', 'r') as school_file:
    num_lines = len(school_file.readlines())

# 4.Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
with open('school_prompt.txt', 'r') as school_file:
    beginning_chars = school_file.read()[:30]

# 5. Using the file school_prompt.txt, assign the third word of every line to a list called three.
three = []
with open('school_prompt.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        three.append(line.split()[2])

# 6.Create a list called emotions that contains the first word of every line in emotion_words.txt.

emotions = []
with open('emotion_words.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        emotions.append(line.split()[0])

# 7.Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.

with open('travel_plans.txt', 'r') as file:
    first_chars = file.read()[:33]

# 8.Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
p_words = []
with open('school_prompt.txt', 'r') as file:
    lines = file.read()
    for word in lines.split():
        if 'p' in word:
            p_words.append(word)

#second solution
fileref = open('school_prompt.txt', 'r')
words = fileref.read().split()
p_words = [word for word in words if 'p' in word]