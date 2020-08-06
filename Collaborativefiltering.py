import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

##Step 1: Read CSV File
import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore
if not firebase_admin._apps:
    # take credentials to can use the database
    cred = credentials.Certificate('./finalecommerce-823b1-firebase-adminsdk-zhev9-485f1905e1.json')
    default_app = firebase_admin.initialize_app(cred)
    db = firestore.client()
    # bring the data from firestore database
    docs = db.collection(u'place').stream()
    # change it to dicitionary of lists
    my_dict = {doc.id: doc.to_dict() for doc in docs}
    df = pd.DataFrame(docs)

ratings= pd.read_csv('ratings.csv')
place= pd.read_csv('place.csv')
ratings=pd.merge(ratings,place).drop(['PlaceOwner','creditcardtype','Placeemail','Placephoto','Place Type','PlaceAddress','creditcardinfo','Placephone','place_description','place_Capacity'],axis=1)
ratings.head()
user_ratings=ratings.pivot_table(index=['userId'],columns=['title'],values='rating')
user_ratings.head()
user_ratings=user_ratings.dropna(thresh=5,axis=1).fillna(0)
user_ratings.head()
item_similarity_df=user_ratings.corr(method='pearson')
item_similarity_df.head()
cosine_similer=cosine_similarity(user_ratings.T)
place_similarity_df=pd.DataFrame(cosine_similer,index=user_ratings.columns,columns=user_ratings.columns)

url = "http://192.168.1.5:443/list/"
user_lover = [("A10 Networks, Inc.", 4), ("ARC Document Solutions, Inc.", 5), ("American Homes 4 Rent", 2.5),
              ("American Tower Corporation (REIT)", 3.2)]

def get_similar_place(title,user_rating):
    similar_score=place_similarity_df[title]*(user_rating)
    similar_score=similar_score.sort_values(ascending=False)
    return similar_score
similar_place = pd.DataFrame()
for title, rating in user_lover:
    similar_place = similar_place.append(get_similar_place(title, rating))
similar_place = similar_place.to_json(orient='records')

#user_lover=[("A10 Networks, Inc.",4),("ARC Document Solutions, Inc.",5),("American Homes 4 Rent",2.5),("American Tower Corporation (REIT)",3.2)]
#similar_place=pd.DataFrame()
#for title,rating in user_lover:
 #   similar_place=similar_place.append(get_similar_place(title,rating))
#similar_place.head()
#print(similar_place.sum().sort_values(ascending=False))




