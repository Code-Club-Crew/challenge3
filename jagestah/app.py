#!/bin/python
#order of operations
    #all arguments need to ignore case
    #Argument 1 will be the data type such as Starship, Planet, etc
        #Call the entire data type and save the json
        #Will need to deal with pagination; can borrow from Challenge 1 alternative
    #Argument 2 will be a string that is searched for in the argument 1 data type
        #Add the entire entry to a results list to be printed at the end
    #Output will be a list of all results found
        #Print a count of the number of results found
        #Print a human readable list of the results and their Key-Value pairs

#Maybe add a third argument for the key user is looking for
    #IE `app.py starships destroyer name` to print the name of anything with a value of destroyer

import sys
import json
import requests
import pprint

final_result = []

pp = pprint.PrettyPrinter(depth=3)
url = 'https://swapi.co/api/'+str(sys.argv[1]+'/')
search_string = str(sys.argv[2])

def gather_data(url):
    request_results = requests.get(url)
    print(request_results)
    if request_results.status_code == 200:
        data = request_results.json()["results"]
        # while request_results.json()["next"]:
        #     request_results = requests.get(request_results.json()["next"])
        #     data = data + request_results.json()["request_results"]
        print("Gathered data")
        pp.pprint(data)
        # check_data(data, search_string)
    else:
        print('Incorrect arg1')

def check_data(data, search_string):
    for level1 in data:
        # if search_string in level1.values[0]()
        final_result = final_result+level1
        print(type(level1))
    print(final_result)

if __name__ == "__main__":
    gather_data(url)
