# Week one
# 1.Using the file school_prompt2.txt, find the number of characters in the file and assign that value to the variable num_char.
school_file = open('school_prompt2.txt', 'r')
school_line = school_file.read()
num_char = len(school_line)
# 2.Find the number of lines in the file, travel_plans2.txt, and assign it to the variable num_lines.
travel = open('travel_plans2.txt', 'r')
num_lines = len(travel.readlines())

# 3.Create a string called first_forty that is comprised of the first 40 characters of

emotion_file = open('emotion_words2.txt', 'r')
first_forty = emotion_file.read()[:40]

# 4.Write code to find out how many lines are in the file emotion_words.txt as shown above. Save this value to the variable num_lines. Do not use the len method.
count = 0
file = open('emotion_words.txt', 'r')
for line in file:
    count += 1
nume_lines = count
