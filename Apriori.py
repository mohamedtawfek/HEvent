import json

import pandas as pd
from apyori import apriori
import jsonify
from collections import defaultdict
def Apriori():
	ds=pd.read_csv('apriori.csv',header=0)
	num_records=len(ds)
	#print(num_records)
	records=[]
	for i in range(0,num_records):
		records.append([str(ds.values[i,j])for j in range(0,6)])
	association_rule=apriori(records,min_support=0.1,min_confidence=0.05,min_lift=2,min_length= 2)
	association_Results=list(association_rule)
	#print(association_Results)
	results=[]
	tracks=[]
	for item in association_Results:
		pair = item[0]
		items=[x for x in pair]
		value0=item[0]
		value1=str(item[1])
		value2=str(item[1])[:7]
		value3=str(item[2][0][2])[:7]
		rows=[value0,value1,value2,value3]
		results.append(rows)
		tracks.append(value0)
		#print(value0)
		#print(results)
		label=['Tracks','Support','confidence','Lift']
		Event_suggestion =pd.DataFrame.from_records(results,columns=label)
		#print(Event_suggestion)
	#print(items)
	#k=Event_suggestion.iloc[0]
	#print(k)
	i=0
	tracks_users=[]
	for x in tracks:
		tracks_users=list(tracks[i])
		i=i+1
		if i>20:
			break
	#print(tracks_users)
	dic={
	"data":tracks_users
	}
	return dic
print(json.dumps(Apriori()))
# items=[]
# for item in Apriori().values():
# 	items=item
# 	print(items)

