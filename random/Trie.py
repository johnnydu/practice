class Node:
	def __init__(self):
		self.is_end = False
		self.count = 0
		self.children = {}

class Trie:
	def __init__(self):
		self.root = Node()

	def add_word(self, word):
		curr = self.root
		
		for c in word:
			if c not in curr.children:
				curr.children[c] = Node()
			curr = curr.children[c]
		curr.is_end = True


	def is_word(self, word):
		curr = self.root	
		for c in word:
			if not curr or c not in curr.children:
				return False
			curr = curr.children[c]
		return curr.is_end
