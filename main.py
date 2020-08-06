import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore
#take credentials to can use the database
cred = credentials.Certificate('./finalecommerce-823b1-firebase-adminsdk-zhev9-485f1905e1.json')
default_app=firebase_admin.initialize_app(cred)
db=firestore.client()
#bring the data from firestore database
docs = db.collection(u'Events').stream()
#change it to dicitionary of lists
my_dict = { doc.id: doc.to_dict() for doc in docs }
#change it to lists
Events =ids= events= []
#take the values without the ids

for a in my_dict.values():
    Events.append(a)
df=pd.DataFrame(Events)
df.to_csv("eventss.csv",index=False)
#
# #bring the data from firestore database
# do = db.collection(u'join_event').stream()
# #change it to dicitionary of lists
# dict = { doc.id: doc.to_dict() for doc in do }
# #change it to lists
# joined = events= []
# #take the values without the ids
# for a in dict.values():
#     joined.append(a)
# di=pd.DataFrame(joined)
# print(di)
# di.to_csv("joined.csv",index=False)
