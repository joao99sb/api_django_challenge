from db_connections import db,close_connection



collections = ['Characters', 'Books', 'Covers']

for collection in collections:
    db[collection].drop()


close_connection()