class MyFirstClass():

    print("Who wrote this?")
    index = "Author-Book"

    def hand_list(self, philosopher, book, year):
        print(MyFirstClass.index)
        print(philosopher + " wrote the book: " + book + " in " + str(year))


whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu", "The Art of War", 1990)
# Who wrote this?
# Author-Book
# Sun Tzu wrote the book: The Art of War
