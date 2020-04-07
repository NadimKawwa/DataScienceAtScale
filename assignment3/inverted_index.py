import MapReduce
import json
import sys

"""
Create an Inverted index. Given a set of documents, an inverted index is a dictionary where each word is associated with a list of the document identifiers in which that word appears.

The input is a 2-element list: [document_id, text], where document_id is a string representing a document identifier and text is a string representing the text of the document. The document text may have words in upper or lower case and may contain punctuation. You should treat each token as if it was a valid word; that is, you can just use value.split() to tokenize the string.

"""

#instantiate a mapreduce object
mr = MapReduce.MapReduce()

# ============================= # 


def mapper(record):
    # key: document identifier
    # value: document contents
    
    #define key value pair
    key, value = record[0], record[1]
    #split the values on whitespace to get words
    words = value.split()
    for w in words:
        mr.emit_intermediate(w, key)
        
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    
    arr = []
    for val in list_of_values:
        if val not in arr:
            arr.append(val)
            
    mr.emit((key, arr))
    
    
# ============================= # 
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
    
    
    
    
    
    
