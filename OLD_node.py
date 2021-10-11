from uuid import uuid4

from blockchain import Blockchain
from utility.verification import Verification
from wallet import Wallet

class Node:
  def __init__(self):
    self.wallet = Wallet()
    self.blockchain = Blockchain(self.wallet.public_key)


  def get_transaction_value(self):
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Enter the transaction amount: '))
    # this returns a tuple
    return tx_recipient, tx_amount


  def get_user_option(self):
    return input('Your option: ')


  def print_blockchain_elements(self):
    for block in self.blockchain.chain:
      print('*' * 10)
      print('Outputting block:')
      print(block)


  def listen_for_input(self):
    waiting_for_input = True
    while waiting_for_input:
      print('-' * 20)
      print('Please choose an option:')
      print('1: Add a new transaction')
      print('2: Mine a new block')
      print('3: Output the blockchain blocks')
      print('4: Check transaction validity')
      print('5: Create wallet')
      print('6: Load wallet')
      print('7: Save wallet')
      print('q: Quit')
      user_option = self.get_user_option()
      if user_option == '1':
        tx_data = self.get_transaction_value()
        recipient, amount = tx_data
        signature = self.wallet.sign_transaction(self.wallet.public_key, recipient, amount)
        if self.blockchain.add_transaction(recipient, self.wallet.public_key, signature, amount=amount):
          print('Added transaction')
        else:
          print('Transaction failed')
        print(self.blockchain.get_open_transactions())
      elif user_option == '2':
        if not self.blockchain.mine_block():
          print('Mining failed! Got no wallet?')
      elif user_option == '3':
        self.print_blockchain_elements()
      elif user_option == '4':
        if Verification.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance):
          print('All transactions are valid')
        else:
          print('There are invalid transactions')
      elif user_option == '5':
        self.wallet.create_keys()
        self.blockchain = Blockchain(self.wallet.public_key)
      elif user_option == '6':
        self.wallet.load_keys()
        self.blockchain = Blockchain(self.wallet.public_key)
      elif user_option == '7':
        self.wallet.save_keys()
      elif user_option == 'q':
        waiting_for_input = False
      else:
        print('Invalid input, please enter a value from the list.')
      if not Verification.verify_chain(self.blockchain.chain):
        print('Invalid Blockchain!')
        self.print_blockchain_elements()
        break
      print('Balance of {}: {:6.2f}'.format(self.wallet.public_key, self.blockchain.get_balance()))
    else:
      print('User left')
    print('Done!')


# only instantiate if it's directly executed and not imported from somewhere else
if __name__ == '__main__':
  node = Node()
  node.listen_for_input()
