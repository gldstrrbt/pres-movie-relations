# launchctl list | grep -v '^-' | sort -nr -k 1
import os, csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

########################################################################################################
########################################################################################################
########################################################################################################

def split_multi_genres():
	a = open("combined_movies_pres_01.csv", "r+")
	b = csv.reader(a, delimiter="^")
	c = open("genre_rows.csv", "w+")
	d = csv.writer(c, delimiter="^")
	e = open("multi_genre.csv", "w+")
	f = csv.writer(e, delimiter="^")

	for g in b:
		try:
			append_multi_genres(g, g[5], "", f)
		except:
			pass

########################################################################################################
########################################################################################################
########################################################################################################

def append_multi_genres(row, genres, csv_a, csv_b):
	if "|" in str(genres):
		csv_b.writerow(row)
	a = genres.split("|")
	if len(a) > 1:
		for b in a:
			row[5] = b
			csv_a.writerow(row)
	else:
		csv_a.writerow(row)

########################################################################################################
########################################################################################################
########################################################################################################

def analyze_df():
	df = pd.read_csv("multi_genre.csv", delimiter="^")
	# df.apply(lambda x: x.factorize()[0]).corr()
	heat_map = sns.heatmap(pd.crosstab(df.president, df.genres))
	# heat_map.savefig("multi_heatmap.png")
	# plt.show()
	df = pd.DataFrame(df)
	df.head()
	green_bars = sns.countplot(y="genres", data=df, palette="Greens_d")
	# green_bars.savefig("multi_greenbars.png")
	df = df.groupby(["president", "genres"]).size()
	df = df.unstack()
	df.plot(kind="bar")
	plt.figure(figsize=(8,10))
	plt.savefig("multi_test.png", dpi=100)

########################################################################################################
########################################################################################################
########################################################################################################

def init():
	# split_multi_genres()
	analyze_df()

########################################################################################################
########################################################################################################
########################################################################################################

init()