#Using the file school_prompt2.txt, find the number of characters in the file and assign that value to the variable num_char

file=open("school_prompt2.txt","r")
st=file.read()
num_char = 0
for ch in st:
    print(len(ch))
    num_char+=len(ch)

file.close()
#Write code to find out how many lines are in the file emotion_words.txt as shown above. Save this value to the variable num_lines. Do not use the len method.

file=open('emotion_words.txt','r')

lines=file.readlines()
num_lines=0
for line in lines:
    num_lines+=1