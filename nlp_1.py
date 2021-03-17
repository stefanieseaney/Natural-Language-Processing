from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)
print(blob)

# break it into sentences
print(type(blob.sentences))

# break it into words
print(blob.words)

# prints list of tags that analyzes each word
print(blob.tags)

# noun phrases
print(blob.noun_phrases)

# sentiment analysis based on blob
print(blob.sentiment)

# polarity is from -1 to 1
# subjectivity = how subjective it is versus objective

print(round(blob.sentiment.polarity, 3))
print(round(blob.sentiment.subjectivity, 3))

# pattern analyzer
sentences = blob.sentences

for sentence in sentences:
    print(sentence)
    print(sentence.sentiment)
    print(round(sentence.sentiment.polarity, 3))

# name bayes analyzer
from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

print(blob.sentiment)

"""
# language detections
print(blob.detect_language())

spanish = blob.translate(to="es")
print(spanish)
"""

# inflection
from textblob import Word

index = Word("index")

print(index.pluralize())

cacti = Word("cacti")

print(cacti.singularize())

animals = TextBlob("dog cat fish bird").words

print(animals.pluralize())

# spell check and correction
word = Word("theyr")

print(word.spellcheck())

corrected_word = word.correct()
print(corrected_word)

sentence = TextBlob("Ths sentence has missplled wrds.")
corrected_sentence = sentence.correct()
print(corrected_sentence)