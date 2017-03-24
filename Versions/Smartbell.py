#Smartbell
#Program to handle JSON data
#Basically, a practice framework for talking to the web server
#Using example data from 'Databae'

#Imported libraries
import json

#Object handling JSON input data
class jsonData(object):
    #Descriptor Definitions:
    #Instantiation
    def __init__(self):
        self.data = []
    #Instantiates from JSON data
    def __init__(self, dataList):
        self.data = json.loads(dataList)
    #Sets data to input list data
    def __set__(self, dataList):
        self.data = dataList
    #Gets data from class as list
    def __get__(self):
        return self.data
    #Deletes current data
    def __del__(self):
        del self.data

    #Getters / Setters:
    #Gets all values of a key
    def get_byKey(self, key):
        return ','.join([x[key] for x in self.data])
  

    #dump utility; printing:
    #Prints all data
    def dump(self):
        for x in self.data:
            print(x)
    #Prints all instances of key
    def dump(self, key):
        for x in self.data:
            print(x[key])

    #search utility; basic searching:
    #Returns list of instances from key and query
    def search(self, key, query):
        resultList = []
        for x in self.data:
            if (x[key] == query):
                resultList.append(x)
        return resultList

#Example data    
Databae_data = '[{"name":"Carl","age":28,"city":"Ipswich"},{"name":"Kevin","age":28,"city":"Ipswich"},{"name":"Owen","age":28,"city":"Ipswich"},{"name":"Ryan","age":28,"city":"Ipswich"}]'

#Creates object holding example JSON data
myObject = jsonData(Databae_data)

#Examples of using and handling

print(myObject.search("name", "Carl"))

