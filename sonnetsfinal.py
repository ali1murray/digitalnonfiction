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

first_line = {
    1: "Shall I compare {:s} to a summer's day?",
    2: "{:s} is better than a summer's day.",
    3: "{:s} far outshines a summer's day.",
    4: "{:s} outshines a summer's day",
}
second_line = {
	1: "Thou art more {:s}, lovely, and temperate-",
	2: "Thou art more {:s} and more temperate-",
	3: "Thou art more {:s}, more temperate-",
    4: "You're more {:s}, more temperate-",
    5: "You're {:s}, more temperate-",
    6: "You're {:s}, temperate-"
}
third_line = {
    1: "With you on a bed of {:s} I would lay.",
    2: "Pretty as a {:s} or a bluejay.",
    3: "Like a {:s} drifting on a bay.",
    4: "A {:s} blooming in late May.",
}
fourth_line = {
    1: "Your life is precious; I wish {:s} on it.",
    2: "If {:s} you seek, so I will make it.",
    3: "{:s} you seek? So I will make it.",
    4: "Bless your life with {:s} in it.",
}
fifth_line = {
    1: "Let's go to sweet {:s}, just the two of us.",
    2: "Take me to {:s} by plane, train, or bus.",
    3: "Meet me in {:s}, won't you? Just us.",
    4: "We will live in {:s}, just us.",
}
sixth_line = {
    1: "And oh, {:s}, ah, it will be so worthwhile.",
    2: "We'll drive around and sing '{:s}' each mile.",
    3: "I'll call you {:s}, you'll call me Lyle.",
    4: "We'll name our house {:s} and smile.",
}
seventh_line = {
    1: "Drink {:s} by the fire and don't make a fuss,",
    2: "Drink now your {:s} and don't make a fuss,",
    3: "Drink your {:s} and don't make a fuss,",
    4: "Drink {:s} and don't make a fuss,",
}
eighth_line = {
    1: "I'll solve all our problems with {:s} and guile.",
    2: "You always knew I was a {:s}-phile.",
    3: "I'm the good ship '{:s}' on the Nile.",
    4: "{:s} colors our bathroom tile.",
}
ninth_line = {
    1: "Hey, you cheated! {:s}? There's simply no way!",
    2: "We'll go to the market every {:s},",
    3: "We'll go to the market on {:s},",
    4: "Cheater! Lying! {:s}? No way.",
}
tenth_line = {
    1: "And I'll pick up {:s}, coffee, and fresh bread.",
    2: "And I'll pick up {:s}, tea, and fresh bread.",
    3: "And I'll pick up {:s} and fresh bread.",
    4: "And I'll pick up {:s} and bread.",
}
eleventh_line = {
    1: "Into your darling ear, '{:s}' I will say.",
    2: "Into your warm ear, '{:s}' I will say.",
    3: "Into your ear, '{:s}' I will say.",
    4: "In your ear, '{:s}' I will say.",
    5: "To you, '{:s}' I will say.",
    6: "To you, '{:s}' I'll say.",
    7: "'{:s}' I will say.",
    8: "'{:s}' I'll say.",
}
twelfth_line = {
    1: "Morning and night, my {:s}, 'til I am dead.",
    2: "All the time, my {:s}, 'til I am dead.",
    3: "All the time, {:s}, 'til I am dead.",
    4: "Always, {:s}, 'til I am dead.",
    5: "Always, {:s}, 'til I'm dead.",
    6: "{:s}, 'til I am dead.",
    7: "{:s}, 'til I'm dead.",
}
thirteenth_line = {
    1: "\tIf I should fail, dunk me in {:s}, and then",
    2: "\tShould I fail, dunk me in {:s}, and then",
    3: "\tShould I fail, give me {:s}, and then",
    4: "\tShould I fail, give me {:s}; then,",
}

lines = [0, first_line, second_line, third_line, fourth_line, fifth_line, sixth_line, seventh_line, eighth_line, ninth_line, tenth_line, eleventh_line, twelfth_line, thirteenth_line]

messages = {
    1: "What is your first name? ",
    2: "Describe, in one word, the sound of your favorite song: ",
    3: "What is the flower that you like the most? ",
    4: "What do you want, more than anything? ",
    5: "Where do you want to go? ",
    6: "Open a nearby book to the sixth page, and write here the sixth word: ",
    7: "What would you like to drink? ",
    8: "What positive trait do you lack? ",
    9: "What day of the week are you free? ",
    10: "What would you like to eat? ",
    11: "What phrase have you been longing to hear? ",
    12: "What is your nickname? ",
    13: "What is something you hate or fear? ",
    14: "What else should I know about you? "
}

words = [0]

index = 1
while len(words) < 15:
    word = raw_input(messages[index])
    if len(word) == 0:
        print "No."
    elif index < 14 and countSyllables(word) > len(lines[index]):
        print "No."
    else:
        index += 1
        words.append(word)

print "\nYour sonnet:"

print first_line[countSyllables(words[1])].format(words[1])
print second_line[countSyllables(words[2])].format(words[2])
print third_line[countSyllables(words[3])].format(words[3])
print fourth_line[countSyllables(words[4])].format(words[4])
print fifth_line[countSyllables(words[5])].format(words[5])
print sixth_line[countSyllables(words[6])].format(words[6])
print seventh_line[countSyllables(words[7])].format(words[7])
print eighth_line[countSyllables(words[8])].format(words[8])
print ninth_line[countSyllables(words[9])].format(words[9])
print tenth_line[countSyllables(words[10])].format(words[10])
print eleventh_line[countSyllables(words[11])].format(words[11])
print twelfth_line[countSyllables(words[12])].format(words[12])
print thirteenth_line[countSyllables(words[13])].format(words[13])
print "\tGenerate one of these sonnets again."


#=====================================================================================
#=====================================================================================






















