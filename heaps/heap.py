"""
max heap
heap model 
	memeber variables : size , list
	operations :
		insert     		done 
		print heap
		delete
		get size 		done 
		constructor  		done
		peek			done 
		poll
		
"""
class heap:
	
	def __init__(self):
		self.size = 0
		self.nums = []
		self.root = None
	def get_size(self):
		return self.size
	def get_parent(self, pos):
		return (pos-1)//2 
	def get_left_child(self , pos):
		return (pos * 2)+1
	def get_right_child(self ,pos):
		return self.get_left_child(pos)+1		
	
	def insert(self , value):
		if(size == 0):
			nums.append(value)
			size+=1
			
		else:
			pass
			#use heapify()	
		self.root = self.nums[0]

	def heapify(self,  pos):
		parent = get_parent(pos)
		while(pos != 0):
			if(arr[pos] > arr[parent]):
				swap(pos , parent)
				pos = parent
			else:
				break	
	def peek(self):
		if(size != 0):
			return self.root
		else:
			print("the heap is empty")
	#helper functions
	def swap(self, pos1 , pos2):
		temp = pos1
		pos1 = pos2
		pos2 = temp	
