import sys
import random as R


def printer(Title, Guess):
	print "Guess a letter: "
	
	for i in xrange(0, len(Title)):
		if Title[i].isalpha() and Guess[i] is 0:
			print " ",
		elif Title[i].isalpha() and Guess[i] is 1:
			print Title[i],
		else:
			print Title[i],
	print

	for i in xrange(0, len(Title)):
		if Title[i].isalpha():
			print "-",
		else:
			print " ",
	print


def guess(Title, Guess, letter):
	for i in xrange(0, len(Title)):
		if letter.strip().lower() == Title[i].lower():
			Guess[i] = 1
	return Guess

def solved(Title, Guess):
	Solve_Flag = True
	for item in Guess:
		if item is 0:
			Solve_Flag = False
	return Solve_Flag

def whole_solve(Title, letter):
	Solve_Flag = True
	for i in xrange(0, len(Title)):
		if letter[i].lower() == Title[i].lower():
			pass
		else:
			Solve_Flag = False
	return Solve_Flag

def main():
	try:
		with open("movies.txt") as F:
			Movies = F.readlines()
	except:
		print "File was not able to be accessed exiting"
		sys.exit(1)
	Title = Movies[R.randrange(0, len(Movies))].strip()

	Guess = [0] * len(Title)

	for i in xrange(0, len(Title)):
		if not Title[i].isalpha():
			Guess[i] = 1


	while not solved(Title, Guess):
		printer(Title, Guess)
		letter = raw_input()
		if len(letter) is 1:
			while not letter.isalpha():
				print "Error: please enter valid letter"
				printer(Title, Guess)
				letter = raw_input()
			Guess = guess(Title, Guess, letter)
			if solved(Title, Guess):
				print "Correct! You Win!"
				break

		else:
			print "Checking Solution..."
			if whole_solve(Title, letter):
				print "Correct! You Win!"
				break
			else:
				print "Incorrect. Game Over"
				break

if __name__ == '__main__':
	main()