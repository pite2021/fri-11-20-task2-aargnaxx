import logging

class Bank:
  def __init__(self, name, id):
    self.name = name
    self.id = id
    logging.info(f'Creating a bank: {name}, {id}')


  def __str__(self):
    return f'Bank: {self.name}, {self.id}'

  def add_client(client):
    logging.info(f'Adding a client: {client}')
    self.clients.append(client)

class Client:
  def __init__(self, name, surname, initial_balance, id):
    self.name = name
    self.name = surname
    self.balance = initial_balance
    self.id = id
    logging.info(f'Creating a bank: {name}, {surname}, {initial_balance}, {id}')

  def __str__(self):
    return f'Client: {self.name}, {self.surname}, {self.balance}, {self.id}'

  def transaction(self, amount, destination):
    if amount < 0 and abs(amount) > balance:
      logging.warning(f'Insufficient account balance for{self.id}')
      return -1

    logging.info(f'Changing {self.id} balance by {amount}')
    self.balance += amount

    if destination != "same":
      logging.info(f'Sending money to client:{destination[0].clients[destination[1]].id}')
      destination[0].clients[destination[1]].balance += abs(amount)

  def cash_transaction(self, amount):
    logging.info('Trying cash transaction')
    self.transaction(amount, 'same')

  def get_balance(self):
    return self.balance


if __name__ == '__main__': 
  logging.basicConfig(filename='task.log', level=logging.DEBUG)

  b1 = Bank('Bank A', 1)
  b2 = Bank('Bank B', 2)

  c1 = Client('Asdf', 'Tyio', 100, 123)
  c2 = Client('Qwer', 'Jklm', 0, 321)

  c1.cash_transaction(+500)
  c2.cash_transaction(-100)

  c1.transaction(-100, (2,321))

  print(c1.get_balance())
  print(c2.get_balance())
