class Category:

    def __init__(self, category):
        """
        Initializes the Category object.
        :param category: The name of the category.
        """
        self.category = category
        self.ledger = []
    
    def deposit(self, amount, description=""):
        """
        Deposits an amount into the category.
        :param amount: Amount to be deposited
        :param description: Description of the deposit (optional)
        """
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        """
        Withdraws an amount from the category.
        :param amount: Amount to be withdrawn
        :param description: Description of the withdrawal (optional)
        :return: True if withdrawal is successful, False otherwise
        """
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
    
    def get_balance(self):
        """
        Calculates the balance of the category.
        :return: The current balance
        """
        balance = 0
        for record in self.ledger:
            balance += record["amount"]
        return balance
    
    def transfer(self, amount, category):
        """
        Transfers an amount from current category to another category.
        :param amount: Amount to be transferred
        :param category: The category to transfer the amount to
        :return: True if transfer is successful, False otherwise
        """
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.category}")
            category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        """
        Checks if the amount can be withdrawn from the category.
        :param amount: Amount to be withdrawn
        :return: True if the amount can be withdrawn, False otherwise
        """
        return amount <= self.get_balance()

    def __str__(self):
        """
        String representation of the Category object.
        :return: The string representation
        """
        title = f"{self.category:*^30}\n"
        items = ""
        total = 0
        for record in self.ledger:
            items += f"{record['description'][0:23]:23}" + f"{record['amount']:>7.2f}\n"
            total += record['amount']
        output = title + items + "Total: " + str(total)
        return output
    

def create_spend_chart(categories):
    """
    Creates a bar chart showing the percentage spent by each category.
    :param categories: List of categories
    :return: String representing the spending chart
    """
    chart = "Percentage spent by category\n"
    total_spent = 0
    spent = []
    names = []
    # Calculating total spent and extracting category names
    for category in categories:
        total = 0
        for record in category.ledger:
            if record["amount"] < 0:
                total -= record["amount"]
        spent.append(total)
        names.append(category.category)
        total_spent += total

    # Calculating percentages
    percentages = []
    for value in spent:
        percentages.append((value / total_spent) * 100)
    
    # Building the chart
    for i in range(100, -10, -10):
        chart += str(i).rjust(3) + "| "
        for percent in percentages:
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    
    chart += "    -" + "---" * len(categories) + "\n"
    
    # Adding category names to the chart
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
print(clothing)
print(create_spend_chart([food, clothing]))