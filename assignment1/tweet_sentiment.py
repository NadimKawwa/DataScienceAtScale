import sys
import json

def hw(sent_file, tweet_file):
    #read the sent file
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an intege
    
    
    #The sentiment of a tweet is equivalent to the sum of the sentiment scores for each term in the tweet
    #for every line
    for line in tweet_file:
        #read with json
        tweet = json.loads(line)
        #instantiate new score
        score = 0
        #check if tweet has text
        if 'text' in tweet:
            #get the text
            text = tweet['text']
            #loop every word in text and split at whitespace
            for word in text.split():
                if word in scores:
                    score += scores[word]
            print score
               
        else:
            #print score of 0 if no text
            print score
            
           
    

def main():
    #make a read only object
    sent_file = open(sys.argv[1], 'r')
    tweet_file = open(sys.argv[2], 'r')

    hw(sent_file, tweet_file)


if __name__ == '__main__':
    main()
