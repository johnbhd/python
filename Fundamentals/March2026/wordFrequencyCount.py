def word_frequency(text):
	arrText = text.lower().split()
	counts = {}

	for word in arrText:
		counts[word] = counts.get(word, 0) + 1

	return counts

text = "apple banana mango apple apple banana banana"
frequency = word_frequency(text)

print(frequency)
