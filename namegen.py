#Python code for Name generation

#Import random library
import random  
#Number generator function
def printname(name): 
	print name+" "+str(random.randint(6,15))

#Ask for input
inp = raw_input()
#Call the number generator function
printname(inp)