#!/usr/bin/env python3

import os, csv, json
from imdb import IMDb


# # Create the object that will be used to access the IMDb's database.
# ia = imdb.IMDb() # by default access the web.

# # Search for a movie (get a list of Movie objects).
# s_result = ia.search_movie('The Untouchables')

# # Print the long imdb canonical title and movieID of the results.
# for item in s_result:
#    print(item['long imdb canonical title'], item.movieID)

# # Retrieves default information for the first result (a Movie object).
# the_unt = s_result[0]
# ia.update(the_unt)

# # Print some information.
# print(the_unt['runtime'])
# print(the_unt['rating'])
# director = the_unt['director'] # get a list of Person objects.

# # Get the first item listed as a "goof".
# ia.update(the_unt, 'goofs')
# print(the_unt['goofs'][0])

# # The first "trivia" for the first director.
# b_depalma = director[0]
# ia.update(b_depalma, 'trivia')
# print(b_depalma['trivia'][0])


##########################################################################
##########################################################################
##########################################################################

# DATASET IN USE
# https://grouplens.org/datasets/movielens/

##########################################################################
##########################################################################
##########################################################################

term_trump 		= range(2017, 2020)
term_obama 		= range(2008, 2016)
term_bush_jr 	= range(2008, 2016)
ia 				= IMDb()

##########################################################################
##########################################################################
##########################################################################

def get_title(movie_title):
	movie_title = str(movie_title).split("(")
	movie_title	= str(movie_title[0])
	return str(movie_title)
	
##########################################################################
##########################################################################
##########################################################################

def get_year(movie_title):
	item_year = str(movie_title).replace("(", "")
	item_year = str(item_year).replace(")", "")
	item_year = item_year.split(" ")
	item_year = item_year[len(item_year)-1]
	return item_year

##########################################################################
##########################################################################
##########################################################################

def get_id(movie_title):
	item_id 	= 0
	item_search 	= ia.search_movie(movie_title)
	
	with open("temp_search.txt", "w+") as a:
		a.write(str(item_search))
	
	with open("temp_search.txt", "r+") as a:
		for b in a:
			c 			= str(b).split(">,")
			c 			= c[0].replace("[http]", "")
			c 			= c.split("title:")
			c 			= c[0].replace("[<Movie id:", "")
			item_id 	= c

	return item_id

##########################################################################
##########################################################################
##########################################################################

def get_info(movie_id):
	item_info 		= ia.get_movie(movie_id, info=["synopsis", "plot", "taglines"])
	item_synopsis 	= item_info.get("synopsis")
	item_plot 		= item_info.get("plot")
	item_tagline 	= item_info.get("taglines")
	return [item_synopsis, item_plot, item_tagline]

##########################################################################
##########################################################################
##########################################################################

def check_existing_csv():
	a = open("year_title.csv", "r+")
	b = csv.reader(a)
	c = [e for e in b]
	return c

##########################################################################
##########################################################################
##########################################################################

def parse_dates_titles():
	a = open("movies.csv", "r+")
	b = csv.reader(a)
	z = check_existing_csv()
	with open("year_title.csv", "a") as c:
		e = csv.writer(c)
		for d in b:
			movie_title	= get_title(d[1])
			print("CHECKING ENTRIES FOR: " + str(movie_title))
			
			if str(movie_title) not in str(z):
				try:	
					movie_year		= get_year(d[1])
					movie_id		= get_id(movie_title)
					movie_info 		= get_info(movie_id)
					movie_synopsis	= movie_info[0]
					movie_plot		= movie_info[1]
					movie_tagline	= movie_info[2]
					movie_tags		= d[2]
					add_entry 		= [movie_id, movie_title, movie_year, movie_tags, movie_tagline, movie_plot, movie_synopsis]
					print("NEW ENTRY FOR: " + str(movie_title))
					print(movie_title)
					print("*"*50)
					e.writerow(add_entry)
				
				except:
					pass

##########################################################################
##########################################################################
##########################################################################

parse_dates_titles()

