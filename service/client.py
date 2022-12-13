
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

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('0.0.0.0:50051') as channel:
        stub = book_pb2_grpc.InventoryServiceStub(channel)
        print("----create a book----")
        response = stub.CreateBook(book_pb2.CreateBookRequest(book=book1))
        print("client received: " + response.message)
        print("----get a book-------")
        nextRes = stub.GetBook(book_pb2.GetBookRequest(isbn="isbn1"))

    print("client received:\n" + str(nextRes.book))


if __name__ == '__main__':
    logging.basicConfig()
    run()