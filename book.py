#this file was set up in conjunction with book.py. it shows us how to read from a file

import re               #re library for regular expressions
import collections      #allows us to count the occurances of words

text = open('book.txt').read().lower()       #read everything into a string called text using read method all in lower case
                                                
                    
words = re.findall('\w+', text)  #regular expressions findall method ensure all occurances of pattern are found and text string
                                    #pattern we're using \w+ (w=anything thats not a white space. +(plus) denotes 1 or more)
                         #essentially for every occurance of 1 or more characters that are not whitespace..we view it as a word
                         #might get some false positives
print(collections.Counter(words).most_common(10))       #use counter method from our collections and 10 most common words
                                                        #counts how many occurances there are
                                                        #most common method limits the results to 10 words
                    
#output:
#list of tuples where each tuple contains the word and number of ocurances 