
from bson.json_util import dumps
import json
def  parser_result(data):
  
  json_data = dumps(data)
  data = json.dumps(json_data)
  result = json.loads(data)
  return result

