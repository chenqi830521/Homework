# Function used to judge if a word is palindromic or not
def IfPalindromicWord(raw_word:str = "") -> bool:

	# word_rev = reversed(word)?

	if(raw_word == raw_word[::-1]): # Actually "==" compares the value of strings not id
		return True
	else:
		return False

# Main function
if __name__ == '__main__':

	# Input a word
	word_input = input("Please input a word: ")

	if(IfPalindromicWord(word_input)):
		print(word_input, "is Palindromic Word!")
	else:
		print(word_input, "is not Palindromic Word!")