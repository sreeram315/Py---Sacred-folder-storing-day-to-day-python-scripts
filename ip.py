
class Conversion: 
	def __init__(self, capacity): 
		self.top = -1
		self.capacity = capacity 
		self.array = [] 
		self.output = [] 
		self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3} 
	

	def is_empty(self): 
		return True if self.top == -1 else False

	def peek(self): 
		return self.array[-1] 

	def pop(self): 
		if not self.is_empty(): 
			self.top -= 1
			return self.array.pop() 
		else: 
			return "$"

	def push(self, op): 
		self.top += 1
		self.array.append(op) 

	def is_operand(self, ch): 
		return ch.isalpha() 

	def not_greater(self, i): 
		try: 
			a = self.precedence[i] 
			b = self.precedence[self.peek()] 
			return True if a <= b else False
		except: 
			return False

	def infix_to_postfix(self, exp): 
		for i in exp: 
			if self.is_operand(i): 
				self.output.append(i) 
			elif i == '(': 
				self.push(i) 
			elif i == ')': 
				while( (not self.is_empty()) and
								self.peek() != '('): 
					a = self.pop() 
					self.output.append(a) 
				if (not self.is_empty() and self.peek() != '('): 
					return -1
				else: 
					self.pop() 
			else: 
				while(not self.is_empty() and self.not_greater(i)): 
					self.output.append(self.pop()) 
				self.push(i) 
		while not (self.is_empty()): 
			self.output.append(self.pop()) 
		print ("".join(self.output) )


exp = "x^y/(5*z)+2"
obj = Conversion(len(exp)) 
obj.infix_to_postfix(exp) 



