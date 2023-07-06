from django.shortcuts import render
from .models import (character_connection,book_connection,cover_connection)
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from utils.json_parser import parser_result
import base64



@api_view(['GET'])
def get_all_characters(request):
  try :

    response = HttpResponse()
    
    characters = character_connection.find()
    characters_list = list(characters)

    result = parser_result(characters_list)

    response['Content-Type'] = 'application/json'
    response.content = result
    return response
  except Exception:
    return JsonResponse({})
  

@api_view(['GET'])
def get_character_info(request,ids):
  try :
    response = HttpResponse()
    
    ids_list = ids.split('&')
    ids_list = list(map(lambda id: int(id),ids_list))

    query = {"id":{'$in':ids_list}}
    character = character_connection.find(query)
    
    result = parser_result(character)
    
    response['Content-Type'] = 'application/json'
    response.content = result
    return response
  except Exception:
    return JsonResponse({})
  

@api_view(['GET'])
def get_character_book(request,id):
  try :
    response = HttpResponse()
    query = {"id":id}
    characters = character_connection.find_one(query)

    pov_books = list(characters['povBooks'])

    id_books_list = list(map(lambda obj:obj['id'],pov_books))

    # pegar os livros
    
    query_books = {"id":{'$in':id_books_list}}
    books = book_connection.find(query_books)
    if not characters:
        books = []

    result = parser_result(books)


    response['Content-Type'] = 'application/json'
    response.content = result
    return response
  except Exception:
    return JsonResponse({})
  
  
@api_view(['GET'])
def get_all_books(request): 

  try :
    response = HttpResponse()
    
    books = book_connection.find()
    books_list = list(books)

    result = parser_result(books_list)

    response['Content-Type'] = 'application/json'
    response.content = result
    return HttpResponse(result)
  except Exception:
    return JsonResponse({})


@api_view(['GET'])
def get_book_info(request,ids): 

  try :
    response = HttpResponse()
    
    ids_list = ids.split('&')
    ids_list = list(map(lambda id: int(id),ids_list))

    query = {"id":{'$in':ids_list}}
    book = book_connection.find(query)
    
    result = parser_result(book)
    
    response['Content-Type'] = 'application/json'
    response.content = result
    return response
  except Exception:
    return JsonResponse({})

@api_view(['GET'])
def get_books_cover(request): 

  try :
    response = HttpResponse()
      
    cover = cover_connection.find()
    
    result = parser_result(cover)
    
    response['Content-Type'] = 'application/json'
    response.content = result
    return response
  except Exception:
    return JsonResponse({})

@api_view(['GET'])
def get_cover(request,book_ids): 

  try :
    response = HttpResponse()
      
    ids_list = book_ids.split('&')
    ids_list = list(map(lambda id: int(id),ids_list))
    
    query = {"bookId":{'$in':ids_list}}
    cover = cover_connection.find(query)
    
    result = parser_result(cover)

    response['Content-Type'] = 'application/json'
    response.content = result
    return response
  except Exception:
    return JsonResponse({})

