# Simulacro de Examen: Gestión de Inventario de una Librería en Python

# Inventory which saves the initial books and for future books
inventory = [
  {"Title": "Harry Potter", "Price": 10.0, "Amount": 5},
  {"Title": "El principito", "Price": 20.0, "Amount": 10},
  {"Title": "La Odisea", "Price": 32.0, "Amount": 15},
  {"Title": "El Quijote", "Price": 60.0, "Amount": 6},
  {"Title": "Crimen y castigo", "Price": 40.0, "Amount": 17}
]

# Function which show the menu for the user
def show_menu():

  print("""

  --- Library Inventory ---
        
  1. Add a new book
  2. Search a book 
  3. Update a book price
  4. Delete a book
  5. Calculate the total price of the inventory
  6. Exit to the program

  """)

# Function to add a new book inside the inventory 
def add_book(title, price, amount):

  new_book = {
    "Title": title,
    "Price": price,
    "Amount": amount
  }

  inventory.append(new_book)

# Function to validate the book title
def validate_book_title(title):
  while not all(book.isalpha() for book in title.split()):
    print("❌ ERROR!, Enter only charachters and spaces.")
    title = str(input("- Enter a valid book title: ")).lower()

  return title

# Function to search a specific book and return that book with its details
def search_book(title):

  for book in inventory:

    if book["Title"].lower() == title:

      return book
    
  return None
# Function to update a new price for the book
def update_book_price(book, new_price):

  old_price = book["Price"]
  
  book["Price"] = new_price

  return f"\n✅ The old price for the book {book["Title"]} was: {old_price} - Now the price for the book is: {book["Price"]}"

# Function to delete book
def delete_book(book_name):

  for index, book in enumerate(inventory):

    if book.get("Title") == book_name:

      inventory.pop(index)

# Function to calculate the total price of the inventory
def calculate_total_inventory():

  total_inventory = 0

  for book in inventory:

    # Obtain price
    price = book["Price"]

    # Obtain amount
    amount = book["Amount"]

    calculate_total = price * amount
    
    total_inventory += calculate_total

  # Return the variable which contain the total
  return total_inventory
flag = True
while flag:
  show_menu()

  try:

    user_option = int(input("Choose an option for the menu: "))

    match user_option:

      # Add new book
      case 1:
        
        # Request book's title
        book_title = str(input("\n- Enter the title of the book: ")).lower()

        # Validate a valid book's title
        book_title = validate_book_title(book_title)

        # Request book's price
        book_price = float(input("\n- Enter the price of the book (it must be positive): "))

        # Request books's amount
        book_amount = int(input("\n- Enter the amount of the book (it must be positive): "))

        # Validate positive values for both price and amount.
        while (book_price < 0) or (book_amount < 0):
          print("\n❌ ERROR, You entered an invalid value.")

          if book_price < 0:
            book_price = float(input("- Enter a valid price for the book: "))
          print("")
          if book_amount < 0:
            book_amount = int(input("- Enter a valid amount for the book: "))

        print("")

        # Call the function add_book() with the arguments.
        add_book(book_title, book_price, book_amount)
        print(f"✅ The book {book_title.capitalize()} was added succesfully.\n")
      
      # Search book.
      case 2:
        
        # Request book's title to search.
        book_title = str(input("\n- Enter the book's title to search: ")).lower()

        book_title = validate_book_title(book_title)

        find_book = search_book(book_title)

        # Validate if the book exist or not
        if find_book is None:
          print(f"\n❌ ERROR!, The book {book_title} does not exist in the inventory.")
        else:
          # Show the details of the book found.
          print(f"\n✅ Search result => Title: {find_book["Title"].capitalize()} | Price: {find_book["Price"]} | Amount: {find_book["Amount"]}")

      # Update price for a specific book
      case 3:
        
        # Request book's title to update a new price
        book_title = str(input("\n- Enter the title of the book to update price: "))

        book_title = validate_book_title(book_title)

        find_book = search_book(book_title)

        if find_book is None:
          print(f"\n❌ ERROR!, The book {book_title} does not exist in the inventory.")
        else:
          new_book_price = float(input(f"- Enter the new price for the book {book_title}: "))

          while new_book_price < 0:
            print("\n❌ ERROR!, You entered a negative price.")
            new_book_price = int(input("Enter a valid price: "))

          update_price = update_book_price(find_book, new_book_price)
          print(update_price)

      # Delete book
      case 4: 
        
        # Request book's title to delete
        book_title = str(input("\n- Enter the title of the book to delete: "))

        book_title = validate_book_title(book_title)

        find_book = search_book(book_title)

        if find_book is None:
          print(f"\n❌ ERROR!, The book {book_title} does not exist in the inventory.")
        else:
          delete = str(input(f"- Are you sure you want to delete the book {book_title} from the inventory? yes/no: ")).lower()

          match delete:
            case "yes":

              print(f"\n✅ The book {book_title} was deleted succesfully from the inventory")
              delete_book(book_title)

            case "no":

              print(f"\nThe book {book_title} was not deleted.")

            case _:

              print("❌ ERROR!, You entered an invalid value.")

      # Show the books of the inventory and show the total value of the inventory
      case 5:
        
        print(f"\nBelow, you will see all the books from the inventory\n")

        # Show books whit their details
        for i in range(len(inventory)):

          print(f"- Book #{i + 1} => [Title: {inventory[i]["Title"]} | Price: {inventory[i]["Price"]} | Amount: {inventory[i]["Amount"]}]")

        total_inventory = calculate_total_inventory()
        print(f"\nThe total value of the inventory is: {total_inventory:,.2f}")

      case 6:
        print("Saliendo del programa...")
        flag = False

  except ValueError:
    print("ERROR!, You entered an invalid value, Try again.") 