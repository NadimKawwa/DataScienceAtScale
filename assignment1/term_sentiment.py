import sys
import json


def hw(sent_file, tweet_file):
    #read the sent file
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an intege
        
    for line in tweet_file:
        #read with json
        tweet = json.loads(line)
        #keep track of positive score
        pos_score = 0
        neg_score = 0
        #check if tweet has text
        if 'text' in tweet:
            #get the text
            text = tweet['text']
            #loop every word in text and split at whitespace
            for word in text.split():
                #get score of words
                if word in scores:
                    if scores[word]>0:
                        pos_score += scores[word]
                    else:
                        neg_score -= scores[word]
                    
            for word in text.split():
                if word not in scores:
                    #safeguard against zero positive
                    if neg_score<=0:
                        print word + ' '  + str(pos_score)
                    else:
                        print word + ' ' + str(pos_score/float(neg_score))
                    
                    
        
    

def main():
    sent_file = open(sys.argv[1], 'r')
    tweet_file = open(sys.argv[2], 'r')
    hw(sent_file, tweet_file)


if __name__ == '__main__':
    main()
