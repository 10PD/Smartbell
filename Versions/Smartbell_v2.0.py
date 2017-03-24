#Smartbell
#Program to handle JSON data
#Basically, a practice framework for talking to the web server
#Using example data from 'Databae'

#Imported libraries
import json

#Object handling JSON input data
class jsonData(object):
    #Descriptor Definitions:
    #Instantiated as JSON list or empty
    def __init__(self, *args):
        if args:
            self.data = json.loads(','.join(x for x in args))
        else:
            self.data = []
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
    def dump(self, *args):
        #Prints all items of key
        if args:
            for x in self.data:
                print(x[args[0]])
        #Prints all items
        else:
            for x in self.data:
                print(x)

    #search utility; basic searching:
    #Returns list of instances by key or query
    def search(self, *args):
        resultList = []
        if args:
            for x in self.data:
                if (x[args[0]] == args[1]):
                    resultList.append(x)
        return resultList

#Example data    
Databae_data = '[{"name":"Carl","age":28,"city":"Ipswich"},{"name":"Kevin","age":28,"city":"Ipswich"},{"name":"Owen","age":28,"city":"Ipswich"},{"name":"Ryan","age":28,"city":"Ipswich"}]'

#Examples of using and handling:
#Creates object holding example JSON data
myObject = jsonData(Databae_data)
#Search
print(myObject.search("name","Carl"))
#Creates new empty object
newObject = jsonData()

#myObject.dump("name")

