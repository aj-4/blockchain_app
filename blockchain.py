import json
import hashlib

from time import time
from uuid import uuid4

class Blockchain(object):
	def __init__(self):
		self.chain = []
		self.current_transactions = []

		#create genesis block
		self.new_block(previous_hash = 1, proof = 100)

	def new_block(self, proof, previous_hash = None):
		#creates a new block and adds to the blockchain
		
		"""
			
		:param proof: the proof given by the proof of work algorithm <int>
		:param previous_hash: (optional) the hash of prev block <int>
		:return: new block <dict>

		"""

		block = {
			'index' : len(self.chain) + 1,
			'timestamp' : time(),
			'transactions' : self.current_transactions,
			'proof' : proof,
			'previous_hash' : previous_hash or self.hash(self.chain[-1]),
		}

		#reset current transactions
		self.current_transactions = [];

		self.chain.append(block)
		return block

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


	@property
	def last_block(self):
		return self.chain[-1]

	def proof_of_work(self, last_proof):
		"""
		PoW Algorithm:
		-finds num p' such that hash(pp') contains leading 4 zeroes, where p is the previous p
		-p is the previous proof, and p' is the new proof

		:param last_proof: (int)
		:return: (int)

		"""

		proof = 0
		while self.valid_proof(last_proof, proof) is False:
			proof += 1

		return proof

	@staticmethod
	def valid_proof(last_proof, proof):
		"""
		Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?

		:param last_proof: Previous Proof (int)
		:param proof: Current Proof (int)
		:return: True if Correct, False if Not (bool)

		"""

		guess = f'{last_proof}{proof}'.encode()
		guess_hash = hashlib.sha256(guess).hexdigest()
		return guess_hash[:4] == "0000"

	@staticmethod
	def hash(block):
		#hashes a block (SHA - 256)

		"""

		:param: block (dict)
		:return: (str)

		"""

	#order dictionary
	block_string = json.dumps(block, sort_keys = True).encode()

	return hashlib.sha256(block_string).hexdigest()
