import os, csv, re, nltk, json
from textblob import TextBlob
from nltk.corpus import stopwords

###################################################
###################################################
###################################################

nltk.download("stopwords")
# def 

###################################################
###################################################
###################################################

def parse_csv():
	a = open("year_title.csv", "r+")
	b = csv.reader(a)
	c = []
	for d in b:
		if d[2].isdigit() == True and len(d[2]) == 4:
			c.append(d)
	return c

###################################################
###################################################
###################################################

def get_desc(content):
	a = str(content[5])
	try:
		a += str(content[6])
	except:
		pass
	a = re.sub(r'[\[[0-9]*\]]', ' ', a)
	a = re.sub(r'\s+', ' ', a)
	a = a.replace("[", "").replace("]", "")
	a = TextBlob(a)
	return a

###################################################
###################################################
###################################################

def get_wordlist(content):
	a = content.words
	# 	wordlist = [g for g in e if g.lower() not in stopwords.words('english')]
	
		

	# 	for h in stopwords.words('english'):
	# 		i = i.replace(" " + str(h) + " ", " ")
	# 	# print(f)

	# 	# e = d.sentiment
	# 	# print(e)
	# 	# print(n_grams(i))
	# 	sentiment_check(n_grams(i))
	# 	print("*"*50)
		# print(n_grams(text_blob))

###################################################
###################################################
###################################################

def n_grams(text_blob):
	a = ""
	for b in text_blob.ngrams(2):
		for c in b:
			a += c + " "
	return a

###################################################
###################################################
###################################################

def sentiment_check(text_collection):
	a = TextBlob(text_collection)
	a = a.sentiment

###################################################
###################################################
###################################################

def get_terms():
	c = open("year_title.csv", "r")
	d = csv.reader(c)
	y = open("combined_movies_pres_02.csv", "w+")
	x = csv.writer(y, delimiter="^")
	for e in d:
		if e[2].isdigit() == True:
			a = open("presidents.csv", "r")
			b = csv.reader(a)
			for z in b:
				start_pres 	= z[2]
				start_pres 	= start_pres.split("-")
				start_pres 	= int(start_pres[0])

				end_pres 	= z[3]
				end_pres	= end_pres.split("-")
				end_pres 	= int(end_pres[0])
				print("*"*50)
				if start_pres <= int(e[2]) and end_pres >= int(e[2]):
					new_line = [z[1], z[4], e[0], e[1], e[2], e[3], e[4], e[5], e[6]]
					x.writerow(new_line)
					# print(new_line)
					# print("---------")

###################################################
###################################################
###################################################

def process_shit():
	a 					= open("combined_test1.csv", "r+", encoding="utf8", errors="ignore")
	b 					= csv.reader(a)
	total_collection 	= []

	for c in b:
		d = str(c)
		# d = str(c).split("^")
		new_entry 				= {}
		new_entry["president"]	= d[0].replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace("\\", "").replace("/", "").replace(",", "").replace("'", "").replace('"', "")
		new_entry["party"]		= d[1].replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace("\\", "").replace("/", "").replace(",", "").replace("'", "").replace('"', "")
		new_entry["id"]			= d[2]
		new_entry["movie"]		= d[3]
		new_entry["year"]		= d[4]
		new_entry["genres"]		= d[5]
		new_entry["taglines"]	= d[6]
		new_entry["desc"]		= d[7].replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace("\\", "").replace("/", "").replace(",", "").replace("'", "").replace('"', "")
		new_entry["plot"]		= d[8].replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace("\\", "").replace("/", "").replace(",", "").replace("'", "").replace('"', "")
		new_entry["sentiments"]	= []

		plot_sentiment			= TextBlob(str(d[8]))
		print(plot_sentiment.sentiment)
		# plot_sentiment			= TextBlob(new_entry["plot"]).sentiment

		# new_entry["sentiments"].append({})

		# print(d[0])
		# print(d[1])
		# print(d[2])
		# print(d[3])
		# print(d[4])
		# print(d[5])
		# print(d[6])
		# print(d[7])
		# print(d[8])
		print(c)
		print("*"*50)
		print("*"*50)
		print("*"*50)
		# new_entry["president"]	= d[0]
		# new_entry["president"]	= d[0]
		# d = str(d).split("^")
		# print(d)
		# new_entry = 
		# print(d[0])

###################################################
###################################################
###################################################


def init():
	process_shit()
	get_terms()
	# a = parse_csv()
	# for b in a:
	# 	c = get_desc(b)
	# 	print(c)

###################################################
###################################################
###################################################

init()
