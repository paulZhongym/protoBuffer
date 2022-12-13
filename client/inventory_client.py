
"""The Python implementation of the GRPC book client."""

from __future__ import print_function

import logging


import grpc
import book_pb2
import book_pb2_grpc

book1 = book_pb2.Book()
book1.isbn = "isbn3"
book1.title = "third book"
book1.author = "Tom"
book1.year = 2011
book1.genre = 2

class InventoryClient:
    def __init__(self):
        pass
    
    def createBook(self, book):
        with grpc.insecure_channel('0.0.0.0:50051') as channel:
            stub = book_pb2_grpc.InventoryServiceStub(channel)
            print("----create a book----")
            response = stub.CreateBook(book_pb2.CreateBookRequest(book=book))
        print("client received: " + response.message)

    def getBook(self, isbn):
        with grpc.insecure_channel('0.0.0.0:50051') as channel:
            stub = book_pb2_grpc.InventoryServiceStub(channel)
            print("----calling inventory client get a book-------")
            nextRes = stub.GetBook(book_pb2.GetBookRequest(isbn=isbn))
        print("client received:\n" + str(nextRes.book))
        return nextRes.book


if __name__ == '__main__':
    logging.basicConfig()
    client = InventoryClient()
    client.getBook("isbn1")
    client.getBook("isbn2")
    client.getBook("isbn3")
