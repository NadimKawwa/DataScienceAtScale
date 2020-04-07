import MapReduce
import sys
import json

"""
Consider a set of key-value pairs where each key is sequence id and each value is a string of nucleotides, e.g., GCTTCCGAAATGCTCGAA....

Write a MapReduce query to remove the last 10 characters from each string of nucleotides, then remove any duplicates generated.

!! Map Input !!
Each input record is a 2 element list [sequence id, nucleotides] where sequence id is a string representing a unique identifier for the sequence and nucleotides is a string representing a sequence of nucleotides

!! Reduce Output !!
The output from the reduce function should be the unique trimmed nucleotide strings.t should be all pairs (friend, person) such that (person, friend) appears in the dataset but (friend, person) does not.

"""

#create a MapReduce object that is used to pass data 
#between the map function and the reduce function

mr = MapReduce.MapReduce()

# =============================

def mapper(record):

    mr.emit_intermediate(record[1][:-10], 1)

    
def reducer(key, list_of_values):
    mr.emit(key)
    

# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)