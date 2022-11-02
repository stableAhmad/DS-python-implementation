#to do
# -heap should handle duplicates
"""
max heap
heap ADS 
	memeber variables : size , list
	operations :
		insert     		done 
		print  			done
		delete			done
		get size 		done 
		constructor  	done
		peek			done 
		
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
		if(self.size == 0):
			self.nums.append(value)

			
		else:
			self.nums.append(value)
			self.heapify(self.size)

		self.size+=1
		self.root = self.nums[0]

	def heapify(self,  pos):
		parent = self.get_parent(pos)
		while(pos != 0):
			if(self.nums[pos] > self.nums[parent]):
				self.swap(pos , parent)
				pos = parent
				parent = self.get_parent(pos)
			else:
				break	

	def peek(self):
		if(self.size != 0):
			return self.root
		else:
			print("the heap is empty")

	def delete(self , pos):
		if(self.size == 0):
			return None
		l = self.get_left_child(pos)
		r = self.get_right_child(pos)
		l_valid = self.is_valid(l)
		r_valid = self.is_valid(r)
		while(l_valid or r_valid):
			target = 0
			if(l_valid and r_valid):
				target = l if(self.nums[l] > self.nums[r]) else r
			elif(l_valid):
				target = l
			elif(r_valid):
				target = r
			self.swap(pos , target)
			pos = target
			l = self.get_left_child(pos)
			r = self.get_right_child(pos)
			l_valid = self.is_valid(l)
			r_valid = self.is_valid(r)

		
		y = self.nums.pop(pos)
		self.size-=1
		if(self.size > 0):
			self.root = self.nums[0]
		else:
			self.root = None
		return  y

	def print(self):
		levels = self.get_tree_levels()
		count = 1
		while(levels > 0):
			index = count-1
			for i in range(count):
				if(self.is_valid(index)):
					print(self.nums[index] , end=" ")
					index+=1
				else:
					break
			print("")
			levels-=1
			count*=2	

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
		temp = self.nums[pos1]
		self.nums[pos1] = self.nums[pos2]
		self.nums[pos2] = temp	






