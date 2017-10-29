class Blockchain(object):
	def __init__(self):
		self.chain = []
		self.current_transactions = []

	def new_block(self):
		#creates a new block and adds to the blockchain
		pass

	def new_transaction(self):
		#creates a new transaction and add it to the blockchain
		pass 

	@staticmethod
	def hash(block):
		#hashes a block
		pass

	@property
	def last(block):
		#returns the last block in the chain
		pass

	