class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        result = self.name.center(30, "*") + "\n"
        for item in self.ledger:
            result += "{:<23}{:>7.2f}".format(item["description"][:23], item["amount"]) + "\n"
        result += "Total: {:.2f}".format(self.get_balance())
        return result

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": amount * -1,
                "description": description
            })
            return True
        return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + budget_category.name)
            budget_category.deposit(amount, "Transfer from " + self.name)
            return True
        return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def get_expenses(self):
        total = 0
        for item in self.ledger:
            if item["amount"] < 0:
                total += abs(item["amount"])
        return total


def create_spend_chart(categories):
    # Calcular total gastado
    expenses = []
    for category in categories:
        expenses.append(category.get_expenses())

    total_expenses = sum(expenses)
    percentage_spent = [item / total_expenses * 100 for item in expenses]

    # Calcular gráfica
    graphic = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        graphic += "{:>3}|".format(i)
        for percentage_category in percentage_spent:
            if percentage_category > i:
                graphic += " o "
            else:
                graphic += "   "
        graphic += " \n"
    graphic += "{:<4}".format("") + "---" * len(categories) + "-"

    # Agregar nombre de las categorías
    categories_length = [len(category.name) for category in categories]

    for i in range(max(categories_length)):
        graphic += "\n{:<4}".format("")
        for category in categories:
            if i < len(category.name):
                graphic += category.name[i].center(3, " ")
            else:
                graphic += "   "
        graphic += " "

    return graphic