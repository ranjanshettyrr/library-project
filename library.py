class library:
    def __init__(self, books, name):
        self.listbooks = books
        self.name = name
        self.lendict = {}

    def displaybook(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.listbooks:
            print(book)

    def lendbook(self, book, user):
        if book not in self.lendict.keys():
            self.lendict.update({book: user})
            print("Lender-Book database has been updated. You can take the book now")
        else:
            print(f"Book is already being used by {self.lendict[book]}")

    def addbook(self, book):
        self.listbooks.append(book)
        print(f"Book has been added to the book list")

    def returnbook(self, book):
        self.lendict.pop(book)


if __name__ == '__main__':
    ranjan = library(['python', 'c++', 'Javascript', 'php','Java','Data Science'], "library")

    while (True):
        print(f"Welcome to my {ranjan.name}. Enter your choice to continue")
        print("Press 1 for Display book")
        print("Press 2 for lend book")
        print("Press 3 for Add book")
        print("Press 4 for remove book")

        userchoice = input()
        if userchoice not in ['1', '2', '3', '4']:
            print("Please enter valid input")

        if userchoice == "1":
            ranjan.displaybook()

        elif userchoice == "2":
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter the user name")
            ranjan.lendbook(book, user)
        elif userchoice == "3":
            book = input("Enter the name of the book you want to add:")
            ranjan.addbook(book)
        elif userchoice == "4":
            book = input("Enter the name of the book you want to return:")
            ranjan.returnbook(book)
        else:
            print("Not a valid option")

        print("Press q for exit and c for continue")
        userchoice2 = ""
        while userchoice2 != "q" and userchoice2 != "c":
            userchoice2 = input()
            if userchoice2 == "q":
                exit()
            elif userchoice2 == "c":
                continue























