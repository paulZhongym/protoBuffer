"""The Python implementation of the GRPC book server."""

from concurrent import futures
import logging

import grpc
import book_pb2
import book_pb2_grpc

# the data for books

book1 = book_pb2.Book()
book1.isbn = "isbn1"
book1.title = "first book"
book1.author = "Alice"
book1.year = 2001
book1.genre = 0

book2 = book_pb2.Book()
book2.isbn = "isbn2"
book2.title = "second book"
book2.author = "Bob"
book2.year = 2021
book2.genre = 3

books = {
    "isbn1":book1,
    "isbn2":book2,
}

class InventoryService(book_pb2_grpc.InventoryServiceServicer):

    def CreateBook(self, request, context):
        try:
            print("creating book ", request)
            book = request.book
            books[book.isbn] = book
            print(books)
            return book_pb2.CreateBookResponse(message="success")
        except:
            return book_pb2.CreateBookResponse(message="failed")

    def GetBook(self, request, context):
        return book_pb2.GetBookResponse(book=books.get(request.isbn,None))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    book_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()