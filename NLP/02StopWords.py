from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example = "Hello Mr. PK, This is a Coding Session. Welcome to FreePlacementPrep!"
stop_words = set(stopwords.words("english"))
# print(stop_words)

words = word_tokenize(example)

# filtered_sentence = []

# for w in words:
# 	if w not in stop_words:
# 		filtered_sentence.append(w)

# print(filtered_sentence)

#TODO: using one liner
filtered_sentence = [w for w in words if not w in stop_words]
print(filtered_sentence)
