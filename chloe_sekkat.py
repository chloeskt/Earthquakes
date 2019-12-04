from random import*

def guess_game():
	""""
	Guess the random number
	"""
	number = randint(1,100)
	question = input("What is the number ?")
	i = 0
	while number != question: 
	    if question < number:
	    	i += 1
	        print "Too low, try again !"
	        question = int(input("What is the number ?"))
	    elif question > number:
	    	i += 1
	        print "Too large !"
	        question = int(input("What is the number ?"))
	if question == number:
		print "You guessed it after %s tries" %(i+1) 

guess = guess_game()

