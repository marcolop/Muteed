import pymongo
import pprint

from pymongo.errors import ConnectionFailure

client = pymongo.MongoClient("mongodb+srv://demo:Techno92@cluster0-b2vez.mongodb.net/test?retryWrites=true")

try:
    status = client.admin.command("serverStatus")
    print("Connected to mongoDB Atlas with status: ")
    pprint.ppprint(status)
except ConnectionFailure:
   print("MongoDb Atlas Connection not established.")
