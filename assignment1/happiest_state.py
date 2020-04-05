import sys
import json

def hw(sent_file, tweet_file):
    d = {}

    
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
        #check if tweet has text
        if ('text' in tweet) and ('place' in tweet):
            #get the text
            text = tweet['text']
            place = tweet['place']
            #loop every word in text and split at whitespace
            if place is not None:
                if place['country_code']=='US':
                    #take last two as state code
                    state = place['full_name'].split(' ')[-1]
                    #make sure we get a state and not a territory
                    if len(state) ==2:
                        
                        score = 0
                        for word in text.split():
                            if word in scores:
                                score += scores[word]
                        if state in d:
                            d[state] += score
                        else:
                            d[state] = score
                        
                        
    current_max = 0
    state_max = ''
    for key in d:
        if d[key] > current_max:
            state_max = key
            current_max = d[key]
            
    print state_max
                            

    

def main():
    #make a read only object
    sent_file = open(sys.argv[1], 'r')
    tweet_file = open(sys.argv[2], 'r')

    hw(sent_file, tweet_file)


if __name__ == '__main__':
    main()
