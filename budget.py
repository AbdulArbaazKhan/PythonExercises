class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_category.category}")
            budget_category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        title = f"{self.category:*^30}\n"
        items = ""
        for item in self.ledger:
            items += f"{item['description'][:23]:<23} {item['amount']:0.2f}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    spendings = []
    names = []
    max_name_length = 0

    for category in categories:
        withdrawals = sum(item["amount"] for item in category.ledger if item["amount"] < 0)
        print(withdrawals)
        spendings.append(withdrawals)
        names.append(category.category)
        if len(category.category) > max_name_length:
            max_name_length = len(category.category)

    for percentage in range(100, -1, -10):
        chart += str(percentage).rjust(3) + "| "
        print(percentage)
        for spending in spendings:
            print(spending)
            if abs((spending)) >= percentage:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    for i in range(max_name_length):
        chart += "     "
        for name in names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        chart += "\n"

    return chart.rstrip()


# Example usage:
# food_category = Category("Food")
# clothing_category = Category("Clothing")
# entertainment_category = Category("Entertainment")

# food_category.deposit(1000, "Initial deposit")
# food_category.withdraw(50, "Groceries")

# clothing_category.deposit(500, "Initial deposit")
# clothing_category.transfer(100, food_category)

# entertainment_category.deposit(300, "Initial deposit")
# entertainment_category.withdraw(150, "Concert tickets")

# categories = [food_category, clothing_category, entertainment_category]
# print(create_spend_chart(categories))




#
# food = Category("Food")
# food.deposit(1000, "initial deposit")
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")
# # print(food.get_balance())
# clothing = Category("Clothing")
# food.transfer(50, clothing)
# clothing.withdraw(25.55)
# clothing.withdraw(100)
# auto = Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(15)
# #
# # print(food)
# # print(clothing)
#
# print(create_spend_chart([food, clothing, auto]))
food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(create_spend_chart([business, food, entertainment]))
print("Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  ")