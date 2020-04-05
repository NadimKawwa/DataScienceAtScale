import sys
import json


def hw(tweet_file):
    #create dict of tweets
    d = {}
    for line in tweet_file:
        #read with json
        tweet = json.loads(line)
        #check if tweet has text
        if 'text' in tweet:
            #get the text
            text = tweet['text']
            #loop every word in text and split at whitespace
            for word in text.split():
                #count occurence
                if word in d:
                    d[word] +=1
                else:
                    d[word] = 1
        
    #count all words in file
    corpus_length = sum(d.values())
    
    for key in d:
        d[key] = d[key]/float(corpus_length)
        print key + ' ' + str(d[key])


def main():
    tweet_file = open(sys.argv[1], 'r')
    hw(tweet_file)


if __name__ == '__main__':
    main()
