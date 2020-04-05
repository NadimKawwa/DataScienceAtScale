import sys
import json
from collections import Counter

def hw(tweet_file):
    #store hashtags in an array
    arr=[]
    for l in tweet_file:
        #read with json
        tweet = json.loads(l)
        #get entities
        ent = tweet.get('entities')
        if ent is not None:
            if len(ent['hashtags'])>0:
                arr.append(ent['hashtags'][0]['text'])
                
    #instantiate counter object
    hash_count = Counter(arr)
    for h, c in hash_count.most_common(10):
        print h + ' ' + str(c)
                
    

def main():
    #make a read only object
    tweet_file = open(sys.argv[1], 'r')

    hw(tweet_file)


if __name__ == '__main__':
    main()
