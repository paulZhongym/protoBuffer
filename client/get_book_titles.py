from inventory_client import InventoryClient

isbns = ["isbn1", "isbn2"]


def getBookList(client, isbns):
    return [ client.getBook(i) for i in isbns ]

if __name__ == '__main__':
    ans = getBookList(isbns)
    print("----- get book titles result ------")
    print(ans)
