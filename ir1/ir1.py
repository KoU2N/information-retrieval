#part1 Simplest information retrieval problem
def search(documents, query):
    return [doc for doc in documents if doc == query]

def search2(documents, query):
    results = []
    for doc in documents:
        if doc == query:
            results.append(doc)
    return results

documents = ['dog', 'cat', 'zebra', 'cat']
print(search(documents, 'cat'))


#part2 Most documents have more than one word...
def search(documents, query):
    return [doc for doc in documents if query in doc]
    
documents = [['dog', 'cat'], ['cat', 'zebra'], ['dog', 'puma']]
print(search(documents, 'cat'))


#part3 Inverted Index
# Map each word to the list of indices of documents that contain it.
index = {'dog': [0, 2],
         'cat': [0, 1],  # IDs are sorted. Why?
         'zebra': [1],
         'puma': [2]}
# Recall: 
# documents = [['dog', 'cat'], ['cat', 'zebra'], ['dog', 'puma']]
print(index['dog'])

def indexed_search(documents, index, query):
    return [documents[doc_id] for doc_id in index[query]]
print(indexed_search(documents, index, 'cat'))

#part4 Query Processing
def and_search(documents, index, queries):
    doc_ids = set(index[queries[0]])
    for query in queries[1:]: # For remaining words in query
        doc_ids &= set(index[query]) # Set intersection
    return [documents[doc_id] for doc_id in doc_ids]
print(and_search(documents, index, ['cat', 'dog']))
#part5 
# survey.txt contains tab-separated survey results.
survey = [line.strip().split('\t') for line in open('survey.txt')]
print(survey[0])

import matplotlib.pyplot as plt # a plotting library 
from collections import Counter  # A dict for counting.

def plot_results_for_column(survey, colidx):
    counts = Counter(row[colidx] for row in survey[1:])
    keys = sorted(counts.keys())
    plt.figure()
    plt.bar(range(len(keys)), [counts[k] for k in keys], width=.5)
    plt.xticks(range(len(counts)), keys)
    plt.title(survey[0][colidx])
    plt.xlabel('count')
    plt.ylabel('frequency')
    plt.show()
plot_results_for_column(survey, 6)    
plot_results_for_column(survey, 7)
plot_results_for_column(survey, 8)

# Count terms in responses to "Why are you taking this course?"# Count  
term_counts = Counter()
for row in survey:
    term_counts.update(row[9].lower().split())
print(term_counts.most_common(20))


# Count 2-word phrases (bigrams) in responses to "Why are you taking this course?"# Count  
term_counts = Counter()
for row in survey:
    words = row[9].lower().split()
    term_counts.update(zip(words[:-1], words[1:]))
print(term_counts.most_common(20))