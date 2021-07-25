#Using map, create a list assigned to the variable greeting_doubled that doubles each element in the list lst

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
greeting_doubled = map(lambda x: x * 2, lst)

#Below, we have provided a list of strings called abbrevs. Use map to produce a new list called abbrevs_upper that contains all the same strings in upper case.

abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]

abbrevs_upper=map(lambda x:x.upper(),abbrevs)

