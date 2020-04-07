import MapReduce
import sys
import json

"""
Assume you have two matrices A and B in a sparse matrix format, where each record is of the form i, j, value. Design a MapReduce algorithm to compute the matrix multiplication A x B

!! Map Input !!
The input to the map function will be a row of a matrix represented as a list. Each list will be of the form [matrix, i, j, value] where matrix is a string and i, j, and value are integers.

The first item, matrix, is a string that identifies which matrix the record originates from. This field has two possible values: "a" indicates that the record is from matrix A and "b" indicates that the record is from matrix B.

!! Reduce Output !!
The output from the reduce function will also be a row of the result matrix represented as a tuple. Each tuple will be of the form (i, j, value) where each element is an integer.

input example:

["a", 4, 2, 96]
["a", 4, 3, 27]
["b", 0, 0, 63]
["b", 0, 1, 18]



"""

#create a MapReduce object that is used to pass data 
#between the map function and the reduce function

mr = MapReduce.MapReduce()

# =============================

def mapper(record):
    key = ''.join([str(record[1]), str(record[2])])
    value = ''.join([str(record[0]), str(record[3])])
    if record[0] =='a':
        #note that range is probably less efficient than xrange
        for i in range(5):
            mr.emit_intermediate(''.join([str(record[1]), str(i)]), 
                                 record)
            
    elif record[0] =='b':
        for i in range(5):
            mr.emit_intermediate(''.join([str(i), str(record[2])]), 
                                 record)

    
def reducer(key, list_of_values):
    result, temp = 0, 0
    
    #very inefficient O**2n
    for v1 in list_of_values:
        for v2 in list_of_values:
            if v1[0] == 'a':
                if (v1[2] == v2[1]) and (v2[0]=='b'):
                    temp = v1[-1] * v2[-1]
                    result += temp
                    
    mr.emit((int(list(key)[0]),int(list(key)[1]),result))
            
    

# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)