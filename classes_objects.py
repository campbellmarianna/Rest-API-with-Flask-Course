lottery_player_dict = {
'name' : 'Rolf',
'numbers' : (5, 9, 12, 3, 1, 21)
}

# A class can do stuff on it's own data
class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5, 9, 12, 3, 1, 21)

    def total(self):
        return sum(self.numbers)

# Two different entities that share the same signature
player_one = LotteryPlayer("Rolf")
player_one.numbers = (1, 2, 3, 6, 7, 8)
player_two = LotteryPlayer("John")

print(player_one.numbers == player_two.numbers)

##

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

anna = Student("Anna", "MIT")
anna.marks.append(56)
anna.marks.append(71)
print(anna.average())

#Exercise
class Store:
    def __init(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        item = { 'name' : name, 'price' : price}
        self.items.append(item)

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        # iterate over the items
        return sum([item['price'] for item in self.items])
