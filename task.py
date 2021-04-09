import logging

class Bank:
  clients=[]

  def __init__(self, name, id):
    self.name = name
    self.id = id
    logging.info(f'Creating a bank: {name}, {id}')

  def __str__(self):
    return f'Bank: {self.name}, {self.id}'

  def add_client(self, client):
    logging.info(f'Adding a client: {client}')
    self.clients.append(client)

class Client:
  def __init__(self, name, surname, initial_balance, id):
    self.name = name
    self.surname = surname
    self.balance = initial_balance
    self.id = id
    logging.info(f'Creating a bank: {name}, {surname}, {initial_balance}, {id}')

  def __str__(self):
    return f'Client: {self.name}, {self.surname}, {self.balance}, {self.id}'

  def transaction(self, amount, destination):
    if amount < 0 and abs(amount) > self.balance:
      logging.warning(f'Insufficient account balance for{self.id}')
      return -1

    logging.info(f'Changing {self.id} balance by {amount}')
    self.balance += amount

    if destination != "same":
      logging.info(f'Sending money to client:{Banks[destination[0] - 1].clients[0].id}')
      Banks[destination[0]-1].clients[0].balance += abs(amount)

  def cash_transaction(self, amount):
    logging.info('Trying cash transaction')
    self.transaction(amount, 'same')

  def get_balance(self):
    return self.balance


if __name__ == '__main__':
  logging.basicConfig(filename='task.log', level=logging.DEBUG)

  Banks = [
    Bank('Bank A', 1),
    Bank('Bank B', 2)
    ]

  c1 = Client('Asdf', 'Tyio', 100, 123)
  c2 = Client('Qwer', 'Jklm', 0, 321)

  Banks[0].add_client(c1)
  Banks[1].add_client(c2)

  c1.cash_transaction(+500)
  c2.cash_transaction(-100)

  c1.transaction(-100, (2, 321))

  print(f'C1 final balance: {c1.get_balance()}')
  print(f'C2 final balance: {c2.get_balance()}')
