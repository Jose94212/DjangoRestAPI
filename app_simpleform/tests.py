import json
from django.test import TestCase
import requests

# Create your tests here.

URL="http://127.0.0.1:8000/simpleform/studentapi/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)

    r=requests.get(url=URL,data=json_data)

    data=r.json()
    print("\ndata=",data)

get_data()

