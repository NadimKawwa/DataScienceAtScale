import MapReduce
import sys
import json

"""
Consider a simple social network dataset consisting of a set of key-value pairs (person, friend) representing a friend relationship between two people. Describe a MapReduce algorithm to count the number of friends for each person.

!! Map Input !!
Each input record is a 2 element list [personA, personB] where personA is a string representing the name of a person and personB is a string representing the name of one of personA's friends. Note that it may or may not be the case that the personA is a friend of personB.

!! Reduce Output !! 
The output should be a pair (person, friend_count) where person is a string and friend_count is an integer indicating the number of friends associated with person.

"""

#create a MapReduce object that is used to pass data 
#between the map function and the reduce function

mr = MapReduce.MapReduce()

# =============================

def mapper(record):
    key, value = record[0], record[1]
    mr.emit_intermediate(key, value)

    
def reducer(key, list_of_values):
    mr.emit((key, len(list_of_values)))
    


# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)