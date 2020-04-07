import MapReduce
import sys
import json

"""
The relationship "friend" is often symmetric, meaning that if I am your friend, you are my friend. Implement a MapReduce algorithm to check whether this property holds. Generate a list of all non-symmetric friend relationships.

!! Map Input !! 
Each input record is a 2 element list [personA, personB] where personA is a string representing the name of a person and personB is a string representing the name of one of personA's friends. Note that it may or may not be the case that the personA is a friend of personB.

!! Reduce Output !! 
The output should be all pairs (friend, person) such that (person, friend) appears in the dataset but (friend, person) does not.

"""

#create a MapReduce object that is used to pass data 
#between the map function and the reduce function

mr = MapReduce.MapReduce()

# =============================

def mapper(record):
    key, value = record[0], record[1]
    #let the key and value pair point to the same value
    key_hash = hash(key) + hash(value)
    mr.emit_intermediate(key_hash, record)

    
def reducer(key, list_of_values):
    if len(list_of_values) == 1:
        mr.emit((list_of_values[0][0], list_of_values[0][1]))
        mr.emit((list_of_values[0][1], list_of_values[0][0]))
    


# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)