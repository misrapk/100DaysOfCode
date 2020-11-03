import nltk
# nltk.download();

#tokenizing == word or sentence tokenizer
#corpora - body of text
#lexicon - words and their means

#investor-speak... regular english-speak
#investor speak 'bull' = someone who is positive about the market
#english-speak 'bull' = scary animal


from nltk.tokenize import sent_tokenize, word_tokenize

example = "Hello India and Mr. PK, How are you! The Covid is going far far and far. We are coding from hours."

# print(sent_tokenize(example))

# print(word_tokenize(example))

for i in word_tokenize(example):
	print(i)