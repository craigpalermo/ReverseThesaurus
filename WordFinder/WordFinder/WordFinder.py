'''
Created on Aug 12, 2013

@author: Craig
'''

import operator

def FindSimilarWords(input_list):
    file_name = 'thesaurus.txt'
    results_list = {}
    
    # open the thesaurus file
    with open(file_name) as f:
        # process the file one line at a time
        for line in f:
            # separate the line by commas and store as a list
            temp = [x.strip() for x in line.split(',')]
            related_count = 0
            
            # check how many words in each line match the list of words entered by the user
            for word in input_list:
                if word in temp[1:]:
                    related_count += 1
            
            # add the original word to the results list if any matches were found
            if related_count > 0:
                results_list[temp[0]] = related_count
                related_count = 0
    
    # sort the list by number of matches in descending order
    sorted_results = sorted(results_list.iteritems(), key=operator.itemgetter(1), reverse=True)
    
    if len(sorted_results) > 0:
        count = 0
        
        print "#) Word, (Matches Found)"
        print "------------------------"
        
        # print the closest matches found
        while count < 10:
            print "%d) %s, %d" % (count + 1, sorted_results[count][0], sorted_results[count][1],)
            count += 1
    else:
        print "No matching words were found."
            
if __name__ == "__main__":
    input_list = ['evil', 'mean', 'angry',]
    FindSimilarWords(input_list)