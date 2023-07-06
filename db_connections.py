import pymongo

url = 'mongodb+srv://root:root@cluster0.6pjdgz2.mongodb.net/'
client =pymongo.MongoClient(url)

db = client['mongo_py']