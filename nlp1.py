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


for sentence in blob.sentences:
    print(sentence.sentiment)

spanish = blob.translate(to='es')
print(spanish)

chinese = blob.translate(to='zh')
print(chinese)

#translates back to english
print(chinese.translate())
'''


from textblob import Word

index = Word('index')
print(index.pluralize())

cacti = Word ('cacti')
print(cacti.singularize())

#wordlist
animals = TextBlob('dog cat fish bird').words
print(animals.pluralize())


#spellcheck and correction
word = Word('theyr')
#gives you a percent of the highest confidence the program has that you meant a certain word
print(word.spellcheck())
#displays the word the program is most confident you meant
print(word.correct())

#normalization
word1 = Word("studies")
word2 = Word("varieties")

print(word1.stem())
print(word2.stem())

#lemmatize gives the correct singular version of the words
print(word1.lemmatize())
print(word2.lemmatize())


#definitions, synonyms, and antonyms from WordNet
happy = Word("happy")
print(happy.definitions)
#synonyms
print(happy.synsets)

for s in happy.synsets:
    for l in s.lemmas():
        print(l.name())

synonym = happy.synsets[1].lemmas()[0].name()
print(synonym)
#antonyms
antonym = happy.synsets[0].lemmas()[0].antonyms()[0].name()
print(antonym)
