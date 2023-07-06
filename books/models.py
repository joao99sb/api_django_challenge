from django.db import models
from db_connections import db 

# Create your models here.
character_connection = db['Characters'] # mudar para Characters
book_connection = db['Books']
cover_connection = db['Covers']
