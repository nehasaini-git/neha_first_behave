from utilities.configurations import *


def addBookPayload(isbn, aisle):
    bookdata = {
        "name": "Learn Neha Study Books",
        "isbn": isbn,
        "aisle": aisle,
        "author": "Neha"
    }
    return bookdata


def buildPayloadfromDB(query):
    addbody = {}
    tp = getQuery(query)
    addbody['name'] = tp[0]
    addbody['id'] = tp[1]
    addbody['location'] = tp[2]
    addbody ['age'] = tp[3]
    return addbody


def staticdata():
    body = {
        'name': 'Neha',
        'id': 123,
        'location': 'Delhi',
        'age': 35 
    }
    return body

