from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)
print(blob)

# break it into sentences
print(type(blob.sentences))

# break it into words
print(blob.words)
