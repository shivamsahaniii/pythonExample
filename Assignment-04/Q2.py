# Concept: Classes & Objects
# Q2. Create a class Book with the following attributes:
    # • title
    # • author
    # • list of reviews
# And add methods to:
    # • add a new review
    # • count reviews
    # • display all reviews

class Book:
    def __init__(self):
        self.title = input("Enter book title: ")
        self.author = input("Enter author name: ")
        self.reviews = []

    def add_review(self):
        review = input("Enter the review of the book: ")
        self.reviews.append(review)
        print("Review added successfully!")

    def count_reviews(self):
        return len(self.reviews)

    def display_all_reviews(self):
        if not self.reviews:
            print("No reviews available.")
        else:
            print("\nReviews:")
            for i, review in enumerate(self.reviews, start=1):
                print(f"{i}. {review}")


book = Book()

while True:
    print("\n1. Add a new review")
    print("2. Count reviews")
    print("3. Display all reviews")
    print("4. Exit")

    option = input("Select an option: ")

    if option == "1":
        book.add_review()
    elif option == "2":
        print(f"Total reviews: {book.count_reviews()}")
    elif option == "3":
        book.display_all_reviews()
    elif option == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid option. Try again.")
