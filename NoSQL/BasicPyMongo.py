# MongoDB stores data in JSON-like documents, which makes the database very flexible and scalable.
# Python needs a MongoDB driver to access the MongoDB database.
# One of the most known MongoDB driver's is "PyMongo".
from pymongo import MongoClient
import pandas as pd

# Establishes a connection with Cluster0
myclient = MongoClient("XXXX")

# Lists all the DBs in Cluster0
print(myclient.list_database_names())

# Instantiates a single DB in the Cluster
db = myclient['sample_airbnb']

# Fetches a particular Collection from the DB
col=db['listingsAndReviews']

#In MongoDB we use the find and findOne methods to find data in a collection.
#Just like the SELECT statement is used to find data in a table in a MySQL database.

#With first_one() we print the 1st register from the DB
#print(col.find_one()) 

# Using pandas, we print the 1st register as a DataFrame
# data = col.find_one()
# mydb = pd.DataFrame.from_dict(data,orient='index')
# print(mydb)

#Fetches all the documents from the Collection as a dictionary
data2 = col.find({})

# Ranges the dictionary as a pandas DataFrame
mydb2 = pd.DataFrame.from_dict(data2)

# Prints the first 5 registers from the DB
print(mydb2[:5])

#Finishes the connection with Cluster0
myclient.close()