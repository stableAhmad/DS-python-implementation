"""
max heap
heap ADS 
	memeber variables : size , list
	operations :
		insert     		done 
		print  			done
		delete
		get size 		done 
		constructor  	done
		peek			done 
		poll
		
"""
import math

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

			
		else:
			nums.append(value)
			heapify(size)

		size+=1
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

	def print(self):
		levels = self.get_tree_levels()
		count = 1
		while(levels > 0):
			index = count-1
			for i in range(count):
				if(is_valid(index)):
					print(self.nums[index] , end=" ")
					index+=1
				else:
					break
			print("")
			levels-=1
			count*=2	
	def delete(self):
		pass
	#helper functions

	def is_valid(self , pos):
		if(pos >= 0 and pos < self.size):
			return True
		return False

	def get_tree_levels(self):
		base = 2
		value = self.size +1
		levels = math.ceil(math.log(value , base))
		return levels

	def swap(self, pos1 , pos2):
		temp = pos1
		pos1 = pos2
		pos2 = temp	



"""
testing :
	-print --> adding levels line to ppt file
	-

"""
