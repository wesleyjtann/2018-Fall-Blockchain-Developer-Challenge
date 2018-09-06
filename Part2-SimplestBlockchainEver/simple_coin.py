from blockchain import Blockchain

#Initiates blockchain

def generate_blocks(number_of_blocks):
	"""
	input: number_of_blocks: int
	output: hash of final block: str

	Given a number of blocks return the output after x amount of block as a string. Input blocks are EMPTY
	"""


	### YOUR CODE HERE

	# init new chain every time generate_blocks() called
	new_chain = Blockchain()

	# create new blocks and add to chain 
	for block in range(number_of_blocks-1):
		new_chain.mine(new_chain.get_current_block())

	# return the last block's hash
	return new_chain.get_current_block().hash

