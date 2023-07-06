import requests
from itertools import chain
from db_connections import db 
import re
import uuid
import base64
character_connection = db['Characters']
book_connection = db['Books']
cover_connection = db['Covers']

def import_all_data():

  print('**** obtendo as informacoes dos livros ****\n')

  books_url="https://anapioficeandfire.com/api/books"
  books =  requests.get(books_url)
  data = books.json()


  book_hash_table = {}
  character_hash_table = {}
  cover_hash_table ={}

  
  for obj in data:
    match = re.search(r'\d+$', obj['url'])
    if not match:
      match = str(uuid.uuid4())

    id = int(match.group())
    
    obj['id'] = id
    if "characters" in obj:
      del obj["characters"]


    book_hash_table[id] = obj


  pov_characters_list = list(map(lambda element: element["povCharacters"], data))

  pov_characters_list_norm = list(chain(*pov_characters_list))


  # tirar a repetição
  pov_characters_list_norm =list(set(pov_characters_list_norm)) 
  

  print('**** obtendo as informação dos personagens ****\n')
  for chac_url in pov_characters_list_norm:
    match = re.search(r'\d+$', chac_url)
    

    characters_response =  requests.get(chac_url)
    character_data = characters_response.json()
    id = int(match.group())
    character_data['id'] = id
    
    
    character_hash_table[id] = character_data
 
  print('**** formatando as informação dos personagens ****\n')
  character_list = []
  for charac_key in character_hash_table:
    character = character_hash_table[charac_key]
    povBooks = character['povBooks']
    povBooks_formatted = format_pov(povBooks,book_hash_table)

    character['povBooks'] = povBooks_formatted
    del character['books']

    character_list.append(character)


  print('**** formatando as informacoes dos livros ****\n')
  book_list = []
  cover_id_list =[]
  for book_key in book_hash_table:
    book = book_hash_table[book_key]

    povCharacters = book['povCharacters']
    povCharacters_formatted = format_pov(povCharacters,character_hash_table)
    book['povCharacters'] = povCharacters_formatted


    book['isbn'] = int(str(book['isbn']).replace('-',''))

    cover_struct = {
      'id':book['isbn'],
      'book_id':book['id']
    }
    cover_id_list.append(cover_struct)
    book_list.append(book)


  print('**** obtendo as informação das capas dos livros ****\n')
# https://covers.openlibrary.org/b/isbn/
  cover_list =[]
  for cover_obj in cover_id_list:
    url_cover = 'https://covers.openlibrary.org/b/isbn/$ID-M.jpg'

    cover_id = cover_obj['id']
    book_id = cover_obj['book_id']
    cover_entity={}
    cover = requests.get(url_cover.replace('$ID',str(cover_id)))
    cover_base64 = base64.b64encode(cover.content).decode('utf-8')
    
    cover_entity['id'] = cover_id
    cover_entity['bookId'] = book_id

    cover_entity['content'] = cover_base64

    # cover_hash_table[cover_id] = cover_base64


    cover_list.append(cover_entity)




  # insert on db
  print('**** inserindo as informação dos personagens no banco ****\n')
  character_connection.insert_many(character_list)
  print('**** inserindo as informação dos livros no banco ****\n')
  book_connection.insert_many(book_list)
  print('**** inserindo as informação dos personagens no banco ****\n')
  cover_connection.insert_many(cover_list)

def format_pov(list,hash_table):
  new_list = []
  for url in list:
    obj = {}

    id =  int(re.search(r'\d+$', url).group())
    element = hash_table[id]
    obj['id']=id
    obj['name']=element['name']
    new_list.append(obj)

  return new_list






import_all_data()