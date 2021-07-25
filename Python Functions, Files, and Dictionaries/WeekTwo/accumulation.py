#print out the occurrence counts for all of the characters, using a for loop to iterate through the keys in x.
f = open('scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
letter_counts = {} # start with an empty dictionary
for c in txt:
    if c not in letter_counts:
        # we have not seen this character before, so initialize a counter for it
        letter_counts[c] = 0

    #whether we've seen it before or not, increment its counter
    letter_counts[c] = letter_counts[c] + 1

for c in letter_counts.keys():
    print(c + ": " + str(letter_counts[c]) + " occurrences")

# Provided is a string saved to the variable name sentence. Split the string into a list of words, then create a dictionary that contains each word and the number of times it occurs. Save this dictionary to the variable name word_counts.
sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
word_counts = {}
for word in sentence.split():
    if word not in word_counts:
        word_counts[word] = 0

    word_counts[word] += 1

#Create a dictionary called char_d from the string stri, so that the key is a character and the value is how many times it occurs.
stri = "what can I do"
char_d={}

for char in stri:
    if char not in char_d:
        char_d[char]=0
    char_d[char]= char_d[char]+1

#The dictionary travel contains the number of countries within each continent that Jackie has traveled to. Find the total number of countries that Jackie has been to, and save this number to the variable name total. Do not hard code this!
travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica": 0, "Australia": 1}

total=0

for country in travel:
    total= total+travel[country]
#schedule is a dictionary where a class name is a key and its value is how many credits it was worth. Go through and accumulate the total number of credits that have been earned so far and assign that to the variable total_credits. Do not hardcode.
schedule = {"UARTS 150": 3, "SPANISH 103": 4, "ENGLISH 125": 4, "SI 110": 4, "ENS 356": 2, "WOMENSTD 240": 4,
            "SI 106": 4, "BIO 118": 3, "SPANISH 231": 4, "PSYCH 111": 4, "LING 111": 3, "SPANISH 232": 4,
            "STATS 250": 4, "SI 206": 4, "COGSCI 200": 4, "AMCULT 202": 4, "ANTHRO 101": 4}
total_credits = 0

for credit in schedule:
    total_credits = total_credits + schedule[credit]
# Create a dictionary called d that keeps track of all the characters in the string placement and notes how many times each character was seen. Then, find the key with the lowest value in this dictionary and assign that key to min_value.
placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."

d = {}
for char in placement:
    if char not in d:
        d[char] = 0
    d[char] = d[char] + 1
key_dic = d.keys()
min_value = list(d.keys())[0]


for key in key_dic:
    if d[key] < d[min_value]:
        min_value = key
print(min_value)

#Create a dictionary called lett_d that keeps track of all of the characters in the string product and notes how many times each character was seen. Then, find the key with the highest value in this dictionary and assign that key to max_value.
product = "iphone and android phones"

lett_d = {}
for char in product:
    if char not in lett_d:
        lett_d[char] = 0
    lett_d[char] = lett_d[char] + 1

dic_keys = lett_d.keys()
max_value = list(lett_d.keys())[0]

for key in dic_keys:
    if lett_d[key] > lett_d[max_value]:
            max_value = key

#ex
d = {'a': 194, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}

ks = d.keys()
best_key_so_far = list(ks)[0]  # Have to turn ks into a real list before using [] to select an item
for k in ks:
    if d[k] > d[best_key_so_far]:
        best_key_so_far = k

print("key " + best_key_so_far + " has the highest value, " + str(d[best_key_so_far]))



