#Importing the natural language toolkit 
import nltk

#From the imported Toolkit import the tokenization function word_Tokenize
from nltk.tokenize import word_tokenize  

#From the Toolkit i'll also need the stemming fuction
from nltk.stem import PorterStemmer 

#From the toolkit i'll also need a library of stop words or short words of all known words (library ya maneno zimefupishwa)
from nltk.corpus import stopwords  


import string 


MySentence = input ("Write the text you want to be stemmed In English: ")

#Breaking Mysentence to tokens for the machine to understand well
FirstTokens = word_tokenize(MySentence)

#Converting Mysentence to lowercase for uniformity and to also identify words like Brian and brian as one word
LowerTokens = [word.lower() for word in FirstTokens]

#Removing punctuations
NoPunctuationTokens = [word for word in LowerTokens if word not in string.punctuation]  

#setting the stop words reference library  to english
Stop_Words_List = set(stopwords.words('english'))

#replacing the words with the ones found in the stop word english dictionary
StopWordTokens = [word for word in NoPunctuationTokens if word not in Stop_Words_List]  

#Stemming 
Stemmer = PorterStemmer() 
Stemmed_Tokens = [Stemmer.stem(word) for word in StopWordTokens] 

# Print the results
print( "Here you go ")
print("The first Tokens are:", FirstTokens)
print( "final stemmed Tokens are:", Stemmed_Tokens)