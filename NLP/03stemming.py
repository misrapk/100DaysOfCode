#stemming -- form of data preprocessing

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example = ["python", "pythonist", "pythonic", "pythoner", "pythonly"]

# for w in example:
	# print(ps.stem(w))

new_ex = "It is very important to work in a working condition. Becuase if you used to worked daily then workist will work for your workening in working contiont."

words = word_tokenize(new_ex)
for w in words:
	print(ps.stem(w))