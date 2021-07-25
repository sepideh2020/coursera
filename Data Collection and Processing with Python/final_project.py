# 1.Your first task will be to fetch data from TasteDive. The documentation for the API is at https://tastedive.com/read/api.
#
# Define a function, called get_movies_from_tastedive. It should take one input parameter, a string that is the name of a movie or music artist. The function should return the 5 TasteDive results that are associated with that string; be sure to only get movies, not other kinds of media. It will be a python dictionary with just one key, ‘Similar’.
#
# Try invoking your function with the input “Black Panther”.
#
# HINT: Be sure to include only q, type, and limit as parameters in order to extract data from the cache. If any other parameters are included, then the function will not be able to recognize the data that you’re attempting to pull from the cache. Remember, you will not need an api key in order to complete the project, because all data will be found in the cache.
#
# The cache includes data for the following queries:

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages

import requests_with_caching
import json

def get_movies_from_tastedive(title):
    baseurl = 'https://tastedive.com/api/similar'
    params_diction = {}
    params_diction['q'] =title
    params_diction['type'] = 'movies'
    params_diction['limit'] = '5'
    movie = requests_with_caching.get(baseurl, params=params_diction)
    return movie.json()
get_movies_from_tastedive("Bridesmaids")
get_movies_from_tastedive("Black Panther")



#2.Please copy the completed function from above into this active code window. Next, you will need to write a function that extracts just the list of movie titles from a dictionary returned by get_movies_from_tastedive. Call it extract_movie_titles.

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages

import requests_with_caching
import json

def get_movies_from_tastedive(name):
    baseurl = 'https://tastedive.com/api/similar'
    params_diction = {}
    params_diction['q'] = name
    params_diction['type'] = 'movies'
    params_diction['limit'] = '5'
    movie = requests_with_caching.get(baseurl, params=params_diction)
    return movie.json()

def extract_movie_titles(movies):
     return ([movie['Name'] for movie in movies['Similar']['Results']])
extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
extract_movie_titles(get_movies_from_tastedive("Black Panther"))


#3.Please copy the completed functions from the two code windows above into this active code window. Next, you’ll write a function, called get_related_titles. It takes a list of movie titles as input. It gets five related movies for each from TasteDive, extracts the titles for all of them, and combines them all into a single list. Don’t include the same movie twice.

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages


import requests_with_caching
import json

def get_movies_from_tastedive(name):
    baseurl = 'https://tastedive.com/api/similar'
    params_diction = {}
    params_diction['q'] = name
    params_diction['type'] = 'movies'
    params_diction['limit'] = '5'
    movie = requests_with_caching.get(baseurl, params=params_diction)
    return movie.json()

def extract_movie_titles(movies):
     return ([movie['Name'] for movie in movies['Similar']['Results']])


def get_related_titles(movie_list):
    li = []
    for movie in movie_list:
        li.extend(extract_movie_titles(get_movies_from_tastedive(movie)))
    return list(set(li))


get_related_titles(["Black Panther", "Captain Marvel"])
#
# 4.Your next task will be to fetch data from OMDB. The documentation for the API is at https://www.omdbapi.com/
#
# Define a function called get_movie_data. It takes in one parameter which is a string that should represent the title of a movie you want to search. The function should return a dictionary with information about that movie.
#
# Again, use requests_with_caching.get(). For the queries on movies that are already in the cache, you won’t need an api key. You will need to provide the following keys: t and r. As with the TasteDive cache, be sure to only include those two parameters in order to extract existing data from the cache



# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_data("Venom")
# get_movie_data("Baby Mama")
import requests_with_caching
import json


def get_movie_data(title):
    endpoint = 'http://www.omdbapi.com/'
    param = {}
    param['t'] = title
    param['r'] = 'json'
    this_page_cache = requests_with_caching.get(endpoint, params=param)

    return json.loads(this_page_cache.text)
get_movie_data("Venom")
get_movie_data("Baby Mama")


#5.Please copy the completed function from above into this active code window. Now write a function called get_movie_rating. It takes an OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an integer. For example, if given the OMDB dictionary for “Black Panther”, it would return 97. If there is no Rotten Tomatoes rating, return 0.

import requests_with_caching
import json


def get_movie_data(title):
    endpoint = 'http://www.omdbapi.com/'
    param = {}
    param['t'] = title
    param['r'] = 'json'
    this_page_cache = requests_with_caching.get(endpoint, params=param)
    return json.loads(this_page_cache.text)
print(get_movie_data("Black Panther")['Ratings'][1])
def get_movie_rating(dic):
    ranking = dic['Ratings']
    for dic_item in ranking:
        if dic_item['Source'] == 'Rotten Tomatoes':
            return int(dic_item['Value'][:-1])
    return 0
get_movie_rating(get_movie_data("Deadpool 2"))

#6.Now, you’ll put it all together. Don’t forget to copy all of the functions that you have previously defined into this code window. Define a function get_sorted_recommendations. It takes a list of movie titles as an input. It returns a sorted list of related movie titles as output, up to five related movies for each input movie title. The movies should be sorted in descending order by their Rotten Tomatoes rating, as returned by the get_movie_rating function. Break ties in reverse alphabetic order, so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.

import requests_with_caching
import json


def get_movies_from_tastedive(title):
    endpoint = 'https://tastedive.com/api/similar'
    param = {}
    param['q'] = title
    param['limit'] = 5
    param['type'] = 'movies'
    this_page_cache = requests_with_caching.get(endpoint, params=param)
    return json.loads(this_page_cache.text)


def extract_movie_titles(dic):
    list = []
    for i in dic['Similar']['Results']:
        list.append(i['Name'])
    return (list)


def get_related_titles(titles_list):
    list = []
    for i in titles_list:
        new_list = extract_movie_titles(get_movies_from_tastedive(i))
        for i in new_list:
            if i not in list:
                list.append(i)
    print(list)
    return list


def get_movie_data(title):
    endpoint = 'http://www.omdbapi.com/'
    param = {}
    param['t'] = title
    param['r'] = 'json'
    this_page_cache = requests_with_caching.get(endpoint, params=param)
    return json.loads(this_page_cache.text)


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_rating(get_movie_data("Deadpool 2"))

def get_movie_rating(data):
    rating = 0
    for i in data['Ratings']:
        if i['Source'] == 'Rotten Tomatoes':
            rating = int(i['Value'][:-1])
            # print(rating)
    return rating


def get_sorted_recommendations(list):
    new_list = get_related_titles(list)
    new_dict = {}
    for i in new_list:
        rating = get_movie_rating(get_movie_data(i))
        new_dict[i] = rating
    print(new_dict)
    # print(sorted(new_dict, reverse=True))
    return [i[0] for i in sorted(new_dict.items(), key=lambda item: (item[1], item[0]), reverse=True)]

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])
