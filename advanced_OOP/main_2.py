from classes_2 import Item, Suitcase

# ----------Start Test Part 1------------------
book = Item("ABC Book", 2)
phone = Item("Nokia 3210", 1)

print("Name of the book:", book.name())
print("Weight of the book:", book.weight())

print("Book:", book)
print('Phone:', phone)
# --------End Test Pat 1 ---------------------

# ----------Start Test Part 2 & 3------------------
brick = Item("Brick", 4)

suitcase = Suitcase(5)
print(suitcase)

suitcase.add_item(book)
print(suitcase)

suitcase.add_item(phone)
print(suitcase)

suitcase.add_item(brick)
print(suitcase)
# --------End Test Pat 2 & 3 ---------------------

# ----------Start Test Part 4-----------------------
suitcase = Suitcase(10)
suitcase.add_item(book)
suitcase.add_item(phone)
suitcase.add_item(brick)

print("The suitcase contains the following items:")
suitcase.print_items()
combined_weight = suitcase.weight()
print(f"Combined weight: {combined_weight} kg")
# --------End Test Part 4 --------------------------

# ----------Start Test Part 5-----------------------
heaviest = suitcase.heaviest_item()
print(f"The heavies item: {heaviest}")
# ----------End Test Part 5-----------------------