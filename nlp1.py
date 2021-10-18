from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

'''
#breaks our text into two separate objects for each sentence
print(blob.sentences)

#makes a list of all words in text
print(blob.words)

print(blob.tags)

print(blob.noun_phrases)



#returns a sentiment stating whether the object is positive or negative
    #subjectivity: 0.0 (objective) to 1.0 (subjective)
    #polarity: -1 to 1
print(round(blob.sentiment.polarity,3))
print(round(blob.sentiment.subjectivity,3))

for sentence in blob.sentences:
    print(sentence)
    print(round(sentence.sentiment.polarity,3))



from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())
'''

for sentence in blob.sentences:
    print(sentence.sentiment)

spanish = blob.translate(to='es')
print(spanish)

chinese = blob.translate(to='zh')
print(chinese)

print(chinese.translate())











