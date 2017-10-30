import json
import hashlib
from time import time

class Blockchain(object):
	def __init__(self):
		self.chain = []
		self.current_transactions = []

		#create genesis block
		self.new_block(previous_hash = 1, proof = 100)

	def new_block(self, proof, previous_hash=None):
		#creates a new block and adds to the blockchain
		pass

	def new_transaction(self, sender, recipient, amount):
		#creates a new transaction and add it to the blockchain

		"""

		:param sender: address of the sender <str>
		:param recipient: address of the recipient <str>
		:param amount: amount <int>
		:return: index of the block that will contain this trans

		"""

		self.current_transactions.append({
			'sender': sender,
			'recipient': recipient,
			'amount': amount,
			})

		return self.last_block['index'] + 1

	@staticmethod
	def hash(block):
		#hashes a block
		pass

	@property
	def last(block):
		#returns the last block in the chain
		pass

