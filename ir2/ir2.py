# 1. Collect documents.
document = "he didn't know where he worked."

# 2. Tokenize
tokens = ["he", "didn't", "know", "where", "he", "worked"] # split; remove punctuation
types = ["he", "didn't", "know", "where", "worked"] # unique tokens.

# 3. Normalize
# remove common words like 'where'; collapse word forms like worked -> work
terms = ["he", "didnt", "know", "work"]

# 4. Index
index = {'he': [0],
         'didnt': [0],
         'know' : [0],
         'work' : [0],}

print(document.split())
print('what     about multiple     spaces?'.split())

import re  # Regular expression module
print(re.split('x', 'axbxc'))

print(re.split('x+', 'axxxxbxxxxc'))
print(re.split('x', 'axxxxbxxxxc'))

print(re.split('\+\+', 'hi+++there'))
print(re.split('([\W\s]|t)', "what's up?"))

text = "A first-class ticket to the U.S.A. isn't expensive?"
print(re.split(' ', text))
print(re.split('\W+',  text)) # \W=not a word character; +=1 or more
print(re.findall('\w+', text)) # \w=a word character [a-zA-Z0-9_]
# group punctuation with following letters
print(re.findall('\w+|\S\w*', text))  # \S=not a space; |=OR
print(re.findall("\w+(?:[-']\w+)*|[-.(]+|\S\w*", text))# (?: specifies what to match, not what to capture
print(re.findall("(?:[A-Z]\.)+|\w+(?:[-']\w+)*|[-.(]+|\S\w*", text))


s = 'hello'
def stem(word):
    for suffix in ['ies', 's', 'ed', 'ing']: # order matters!
    	if word.endswith(suffix):
            return word[:-len(suffix)]
types = ['tied', 'ties', 'tis', 'bed', 'cities']
print([stem(w) for w in types])



from nltk.stem import PorterStemmer # See nltk.org (`pip install nltk`)
# http://tartarus.org/~martin/PorterStemmer/
# Original paper: http://web.simmons.edu/~benoit/lis466/PorterStemmingAlgorithm.pdf
porter = PorterStemmer()
print(types)
print([porter.stem(x) for x in types])




print(porter.stem('city'))

types = ['bed', 'kiss',
         'tied', 'tis',
         'universal', 'university',
         'experiment', 'experience',
         'past', 'paste',
         'alumnus', 'alumni',
         'adhere', 'adhesion',
         'create', 'creation']
porter_results = [porter.stem(x) for x in types]
print(porter_results)




from nltk.stem.wordnet import WordNetLemmatizer
# See description: https://wordnet.princeton.edu/wordnet/man/morphy.7WN.html
lemm = WordNetLemmatizer()
lemm_results = [lemm.lemmatize(x) for x in types]
print('%15s\t%15s\t%15s' % ('type', 'porter', 'lemmatizer'))
print('\n')
print('\n'.join(['%15s\t%15s\t%15s' % (t[0], t[1], t[2])
                 for t in zip(types, porter_results, lemm_results)]))

print(lemm.lemmatize('are'))
print(lemm.lemmatize('is'))

print(lemm.lemmatize('are', 'v'))
print(lemm.lemmatize('is', 'v'))