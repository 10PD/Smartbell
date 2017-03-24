#Smartbell
#Program to handle JSON data
#Basically, a practice framework for talking to the web server
#Using example data from 'Databae'

#Imported libraries
import json

#Descriptor object handling JSON data
#Currently only standard descriptors
#Will be updated to fit our ADT needs
class jsonDesc(object):
    #Descriptor Definitions:
    #Instantiated as list
    def __init__(self):
        self.values = []    
    #Sets data to input data
    def __set__(self, obj, setData):
        self.values = setData
    #Gets data from class
    def __get__(self, instance, owner):
        return self.values
    #Deletes current data
    def __del__(self):
        del self.values

    
#Main object, instantiates 'data' from jsonDesc
class jsonHolder(object):
    #Defined constructor
    #Takes 0 OR 1 args (More args ignored but no exception thrown)
    #Inits data as empty OR parses JSON
    def __init__(self, *args):
        self.data = jsonDesc()
        if args:
            try:
                self.data = json.loads(args[0])
            except json.decoder.JSONDecodeError:
                print("Invalid JSON argument passed! Initialised as empty.")

    #Getters / Setters
    def setJson(self, setData):
        self.data = json.loads(setData)
    def getJson(self):
        return json.dumps(self.data)
    
    #print utility; printing:
    def printer(self, *args):
        #Prints all values of stored key
        if args:
            for x in self.data:
                try:
                    print(x[args[0]])
                except KeyError:
                    print("Key not found in this item")
        #Prints all items
        else:
            for x in self.data:
                print(x)

    #search utility; basic searching:
    #Returns list of results by key and/or query
    def search(self, key, value):
        resultList = []
        for x in self.data:
            if (x[key] == value):
                resultList.append(x)
        return resultList

    #filter utility; essentially layered basic searching:
    #Takes keyvalue pair and optional bool arg for OR / AND filter (Default OR)
    #Returns list of results
    def filter(self, layer=False, **qargs):
        resultList = []
        filterCheck = 0
        if qargs:
            for x in self.data:
                for key, value in qargs.items():
                    if layer:
                        if (x[str(key)] == value):
                            filterCheck += 1
                        if (filterCheck == len(qargs)):
                            resultList.append(x)
                    else:
                        if (x[str(key)] == value):
                            resultList.append(x)
        return resultList
    
#Example data    
Databae_data = '[{"name":"Carl","age":34,"city":"Ipswich"},{"name":"Carl","age":28,"city":"Ipswich"},{"name":"Kevin","age":28,"city":"Ipswich"},{"name":"Owen","age":28,"city":"Ipswich"},{"name":"Ryan","age":28,"city":"Ipswich"}]'

#EXAMPLES of using and handling:
#Creates new object and sets JSON value
f = jsonHolder()
f.setJson(Databae_data)
#Variation of object creation / population
g = jsonHolder(Databae_data)
#Accessing data by index and key
print("Accessing data by index 0 and key 'name': ")
print(f.data[0]["name"])

#Utility function examples:
#Assigns g data to f's filter returned results
#Takes 'True' for AND filter, plus query arguments
g.data = f.filter(True, name="Carl", age=28)

#Printer utility showing results
print("Results where 'name'='Carl' and 'age'=28:")
g.printer()

#Search utility
print("Results where 'age' = 34")
print(f.search("age", 34))
