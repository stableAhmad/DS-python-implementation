"""
ADS :
	insert()			done	
	delete()
	get_tree_height()		done
	traversal :
		in order		done
		pre order		trivial
		post order		trivial
	level traversal  		done	
	get_size()			done
	get_node_depth()		done
	get_node_height()		done

"""
class BST:
	def __init__(self):
		self.root = None
		self.size = 0

	def get_root(self):
		return self.root
	def set_root(self , val):
		self.root = Node()
		Node.val = val	

	def insert(self , val):
		new_node = Node()
		new_node.val = val
		root = self.get_root()
		if root :
			current = root
			while(True):
				if(new_node.val < current.val):
					if(current.left):
						current = current.left
					else:
						current.left = new_node
						break
				else:
					if(current.right):
						current = current.right
					else:
						current.right = new_node
						break

		else:
			self.root = new_node
		self.size+=1

	def get_size(self):
		return self.size
	def in_order_traversal(self):
		self.in_recursion(self.root)

	def in_recursion(self , node):
		if not node:
			return
		self.in_recursion(node.left)
		print(node.val , end=" ")
		self.in_recursion(node.right)


	def level_traversal(self):
		if(not self.root):
			return
		
		q = [self.root]
		while(q):
			current = q.pop(0)
			print(current.val)
			if(current.left):
				q.append(current.left)
			if(current.right):
				q.append(current.right)
	def find_node(self , val):
		if not self.root:
			return -1
		q = [self.root]
		while(q):
			current = q.pop(0)
			if(current.val == val):
				return current
			if(current.left):
				q.append(current.left)
		
			if(current.right):
				q.append(current.right)	

		return -1
	def get_node_height(self , val):
		node = self.find_node(val)
		if node == -1:
			return
		return self.height_recursion(node)
		 
	def height_recursion(self, node):
		if( not node):
			return -1
		return max(1+self.height_recursion(node.left) , 1+self.height_recursion(node.right))
	def get_tree_height(self):
		return get_node_height(self.root)
	
	def get_node_depth(self, val):
		ans = self.depth_recur(0 , val , self.root)
		if(ans == -1):
			print("element not found")
		return ans
	def depth_recur(self , so_far , val , node):
		if(not node):
			return -1
		if(node.val == val):
			return so_far
		left = self.depth_recur(so_far + 1 , val , node.left)
		right = self.depth_recur(so_far+1 ,   val , node.right)
		return max(left , right)
	
		
class Node:
	def __init__(self):
		self.val = 0
		self.left = self.right = None


