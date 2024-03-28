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
        balance = 0
        for record in self.ledger:
            balance += record["amount"]
        return balance
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.category}")
            category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.category:*^30}\n"
        items = ""
        total = 0
        for record in self.ledger:
            items += f"{record['description'][0:23]:23}" + f"{record['amount']:>7.2f}\n"
            total += record['amount']
        output = title + items + "Total: " + str(total)
        return output
    
#function to create a spend chart
def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    total_spent = 0
    spent = []
    names = []
    for category in categories:
        total = 0
        for record in category.ledger:
            if record["amount"] < 0:
                total -= record["amount"]
        spent.append(total)
        names.append(category.category)
        total_spent += total
    
    percentages = []
    for value in spent:
        percentages.append((value / total_spent) * 100)
    
    for i in range(100, -10, -10):
        chart += str(i).rjust(3) + "| "
        for percent in percentages:
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    
    chart += "    -" + "---" * len(categories) + "\n"
    
    longest_name = max(names, key=len)
    for i in range(len(longest_name)):
        chart += "     "
        for name in names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        if i < len(longest_name) - 1:
            chart += "\n"
    
    return chart



# Test
food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
print(food)

# Test 2
print(create_spend_chart([food, clothing]))