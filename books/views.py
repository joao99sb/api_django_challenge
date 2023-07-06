from django.shortcuts import render
from .models import (character_connection,book_connection)
from django.http import JsonResponse, HttpResponse
from bson.json_util import dumps
import json



def get_all_characters(request):


  try :
    characters = character_connection.find()
    characters_list = list(characters)

    result = parser_result(characters_list)

    return HttpResponse(result)
  except Exception:
    return JsonResponse({})
  


def get_character_info(request,id):
  try :
    id = int(id)
    query = {"id":id}
    character = character_connection.find_one(query)
    result = parser_result(character)
    return HttpResponse(result)
  except Exception:
    return JsonResponse({})
  
def get_all_books():
  
  try :
    id = int(id)
    query = {"id":id}
    character = character_connection.find_one(query)
    result = parser_result(character)
    return HttpResponse(result)
  except Exception:
    return JsonResponse({})

def  parser_result(data):
  
  json_data = dumps(data)
  data = json.dumps(json_data)
  result = json.loads(data)
  return result