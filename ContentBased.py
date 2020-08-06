import pandas as pd
import numpy as np
import random
import jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def combine_features(row):
	try:
		return row['speaker']+" "+row['address']
	except:
		print ("Error:", row)
df = pd.read_csv("Content.csv")

###### helper functions. Use them when needed #######
# def get_title_from_index(id):
# 	diction={
# 		"name": 	df[df.Int_ID == id]["name"].values[0],
# 		"owner":	df[df.Int_ID == id]["owner"].values[0],
# 		"trakName": df[df.Int_ID == id]["trakName"].values[0],
# 		"decription":	df[df.Int_ID == id]["decription"].values[0],
# 		"place_owner":	df[df.Int_ID == id]["place_owner"].values[0],
# 		"image":	df[df.Int_ID == id]["image"].values[0],
# 		"date": 	df[df.Int_ID == id]["date"].values[0],
# 		"place":	df[df.Int_ID == id]["place"].values[0],
# 		"speakers_id":	df[df.Int_ID == id]["speakers_id"].values[0],
# 		"serchIndex":	df[df.Int_ID == id]["serchIndex"].values[0],
# 	}
# 	return diction
#
# def name(id):
# 	return 		df[df.Int_ID == id]["name"].values[0]
# def owner(id):
# 	return 		df[df.Int_ID == id]["owner"].values[0]
# def trakName(id):
# 	return 		df[df.Int_ID == id]["trakName"].values[0]
# def decription(id):
# 	return 		df[df.Int_ID == id]["decription"].values[0]
# def place_owner(id):
# 	return 		df[df.Int_ID == id]["place_owner"].values[0]
# def image(id):
# 	return 		df[df.Int_ID == id]["image"].values[0]
# def date(id):
# 	return 		df[df.Int_ID == id]["date"].values[0]
# def place(id):
# 	return 		df[df.Int_ID == id]["place"].values[0]
# def speakers_id(id):
# 	return 		df[df.Int_ID == id]["speakers_id"].values[0]
# def serchIndex(id):
# 	return 		df[df.Int_ID == id]["serchIndex"].values[0]

def get_index_from_title(event):
	return df[df.event == event]["id"].values[0]
##################################################

##Step 1: Read CSV File
import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore


def ContentBased(data):
	if not firebase_admin._apps:

		# take credentials to can use the database
		cred = credentials.Certificate('./finalecommerce-823b1-firebase-adminsdk-zhev9-485f1905e1.json')
		default_app = firebase_admin.initialize_app(cred)
		db = firestore.client()
		# bring the data from firestore database
		docs = db.collection(u'Events').stream()
		# change it to dicitionary of lists
		my_dict = {doc.id: doc.to_dict() for doc in docs}
		# change it to lists
		Events = events = []
		# take the values without the ids
		for a in my_dict.values():
			Events.append(a)
		df = pd.DataFrame(Events)
		#print(df)
		df.to_csv("Content.csv", index=False)

	#print df.columns
	##Step 2: Select Features
	hdb=pd.read_csv("Content.csv",)
	features = ['speaker','address']
	##Step 3: Create a column in DF which combines all selected features
	for feature in features:
		hdb[feature] = hdb[feature].fillna('')


	hdb["combined_features"] = hdb.apply(combine_features,axis=1)

	#print "Combined Features:", df["combined_features"].head()

	##Step 4: Create count matrix from this new combined column
	cv = CountVectorizer()

	count_matrix = cv.fit_transform(hdb["combined_features"])

	##Step 5: Compute the Cosine Similarity based on the count_matrix
	cosine_sim = cosine_similarity(count_matrix)
	#Event_user_likes = "KN"

	## Step 6: Get index of this Event from its title

	Event_Index = random.choice(data)
	print(Event_Index)
	similar_Event =  list(enumerate(cosine_sim[Event_Index]))
	#print(similar_Event)
	## Step 7: Get a list of similar Event in descending order of similarity score
	sorted_similar_Event = sorted(similar_Event,key=lambda x:x[1],reverse=True)
	## Step 8: Print titles of first 5 Event
	#print(sorted_similar_Event)

	#print(items)
	ids=""
	eventsid=""
	Events_IDS=[]

	for a in sorted_similar_Event:
		if a[0]<7:
			Events_IDS.append(a[0]+1)
	dicEvents={
		"Data":Events_IDS
		}
	print(dicEvents)
	return dicEvents

