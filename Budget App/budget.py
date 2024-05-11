class Category:
  def __init__(self, category_name):
    self.name = category_name
    self.ledger = []
  
  def deposit(self, amount, description=""):
    self.ledger.append({
      "amount": amount,
      "description": description
    })

  def get_balance(self):
    balance = 0.0
    for item in self.ledger:
      balance += item["amount"]
    return balance
  
  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    else:
      return True
  
  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({
        "amount": -amount,
        "description": description
      })
      return True
    else:
      return False
  
  def transfer(self, amount, other_category):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {other_category.name}")
      other_category.deposit(amount, f"Transfer from {self.name}")
      return True
    else:
      return False
  
  def __str__(self):
    chars = ""
    char = "*"
    char_number = 30 - len(self.name)
    for i in range(char_number):
        chars += char
    result = chars[:char_number//2] + self.name + chars[char_number//2:] + "\n"

    for item in self.ledger:
      description = item["description"][:23]
      for i in range(23 - len(description)):
        description += " "
      amount = str(round(item["amount"] + 0.0, 2))
      if len(amount.split(".")[1]) == 1:
        amount += "0"
      for i in range(7 - len(amount)):
        amount = " " + amount
      result += description + amount + "\n"
    
    result += f"Total: {self.get_balance()}"

    return result


def create_spend_chart(categories):
  result = "Percentage spent by category\n"
  names = []
  percentages = []

  # Calculate Percentages
  total_withdrawals = 0.0
  for category in categories:
    for item in category.ledger:
      if item["amount"] < 0:
        total_withdrawals += abs(item["amount"])
  for category in categories:
    withdrawals = 0.0
    for item in category.ledger:
      if item["amount"] < 0:
        withdrawals += abs(item["amount"])
    percentage_spent = (withdrawals / total_withdrawals) * 100
    rounded_percentage = round(percentage_spent, -1)
    if rounded_percentage > percentage_spent:
      rounded_percentage -= 10
    names.append(category.name)
    percentages.append(rounded_percentage)

  # Draw Bar Chart  
  for label in range(100, -1, -10):
    if result.find(f" {label}|") == -1:
      if label == 100:
        result += "100| "
      elif label == 0:
        result += "  0| "
      else:
        result += f" {label}| "
    for percentage in percentages:
      if percentage >= label:
        result += "o  "
      else:
        result += "   "
    result += "\n"
  
  # Display Dashes
  result += "    "
  dashes = len(categories) * 3 + 1
  for i in range(dashes):
    result += "-"
  result += "\n"

  # Display Category Names
  for i in range(len(max(names, key=len))):
    result += "     "
    for name in names:
      try:
        result += f"{name[i]}  "
      except:
        result += "   "
    if len(max(names, key=len)) != i + 1:
      result += "\n"

  return result  
