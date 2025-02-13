from pymongo import MongoClient
import pprint
import re

# Connect to MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Get reference to 'chinook' database
db = client["chinook"]

# Get a reference to the 'customers' collection
customers_collection = db["customers"]

# Compile the regex to match LastName starting with "G"
rgx = re.compile('^G.*?$', re.IGNORECASE)

# Find all documents with LastName starting with "G"
cursor = customers_collection.find({"LastName": rgx})
num_docs = 0

# Print each document and count the number of documents found
for document in cursor:
    num_docs += 1
    pprint.pprint(document)
    print()

print("# of documents found: " + str(num_docs))

# Close the connection
client.close()