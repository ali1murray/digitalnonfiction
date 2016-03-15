#=====================================================================================

def countSyllables(word):
	count = 0
	vowels = 'aeiouy'
	word = word.lower().strip(".:;?!")
	if word[0] in vowels:
		count += 1
	for index in range(1,len(word)):
		if word[index] in vowels and word[index-1] not in vowels:
			count += 1
	if word.endswith('e'):
		count -= 1
	if word.endswith('le') and word[-3] not in vowels:
		count += 1
	if word.endswith('les') and word[-4] not in vowels:
		count += 1
	if word.endswith('ian') and not (word.endswith('tian') or word.endswith('cian')):
		count += 1
	if word.startswith('mc'):
		count += 1
	if word.startswith('tri') and word[3] in vowels:
		count += 1
	if word.startswith('bi') and word[2] in vowels:
		count += 1
	if count == 0:
		count += 1
	return count

#=====================================================================================

first_line = "Shall I compare thee to a summer's day?"
second_line = {
	1: "{:s} art more lovely and more temperate.",
	2: "Thou art more {:s} and more temperate.",
	3: "Thou art more lovely and more {:s}."
}
# "Rough winds do shake the darling buds of May,"
# "And summer's lease hath all too short a date."
# "Sometime too hot the eye of heaven shines,"
# "And often is his gold complexion dimmed;"
# "And every fair from fair sometime declines,"
# "By chance, or nature's changing course, untrimmed;"
# "But thy eternal summer shall not fade,"
# "Nor lose possession of that fair thou ow'st,"
# "Nor shall death brag thou wand'rest in his shade,"
# "When in eternal lines to Time thou grow'st."
# "\tSo long as men can breathe, or eyes can see,"
# "\tSo long lives this, and this gives life to thee."

word1 = raw_input("Enter a word for the first line: ")
word2 = raw_input("Enter a word for the second line: ")
# word3 = raw_input("Enter a word for the third line: ")
# word4 = raw_input("Enter a word for the fourth line: ")
# word5 = raw_input("Enter a word for the fifth line: ")
# word6 = raw_input("Enter a word for the sixth line: ")
# word7 = raw_input("Enter a word for the seventh line: ")
# word8 = raw_input("Enter a word for the eighth line: ")
# word9 = raw_input("Enter a word for the nineth line: ")
# word10 = raw_input("Enter a word for the tenth line: ")
# word11 = raw_input("Enter a word for the eleventh line: ")
# word12 = raw_input("Enter a word for the twelfth line: ")
# word13 = raw_input("Enter a word for the penultimate line: ")
# word14 = raw_input("Enter a word for the last line: ")

print "\nYour sonnet:"

line1 = first_line.split(" ")
for index in range(0,len(line1)):
	if countSyllables(line1[index]) == countSyllables(word1):
		line1[index] = word1
print " ".join(line1)

print second_line[countSyllables(word2)].format(word2)

# words = []
# words.append(word1)
# words.append(word2)
# print words

#=====================================================================================
#=====================================================================================






















