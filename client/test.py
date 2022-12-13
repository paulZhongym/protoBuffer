from unittest.mock import *
import unittest
import book_pb2
from inventory_client import InventoryClient
from get_book_titles import getBookList

isbns = ["isbn1", "isbn2"]

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

class TestAPIMethods(unittest.TestCase):
    def testWithMockServer(self):
        print("----testing mock server----")

        client = InventoryClient()
        
        client.getBook = Mock()
        client.getBook.side_effect = [book1, book2]

        ans = getBookList(client,isbns)
        self.assertEqual(ans,[book1, book2])

    def testRealServer(self):
        print("----testing real server----")
        client = InventoryClient()
        ans = getBookList(client, isbns)
        self.assertEqual(ans,[book1, book2])



if __name__ == '__main__':
    unittest.main()