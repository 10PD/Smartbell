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
        try:
            self.data = json.loads(','.join(str(x) for x in args))
        except:
            self.data = []            
    #Sets data to input data
    def __set__(self, obj, setData):
        print("Called")
        try:
            self.data = json.loads(json.dumps(setData))
        except:
            print("Object takes JSON format ONLY.")
    #Gets data from class
    def __get__(self, instance, owner):
        return self.data
    #Deletes current data
    def __del__(self):
        del self.data

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
    #Returns list of results of keyvalue pairs

class Foo():
    Databae_data = '[{"name":"Carl","age":34,"city":"Ipswich"},{"name":"Carl","age":28,"city":"Ipswich"},{"name":"Kevin","age":28,"city":"Ipswich"},{"name":"Owen","age":28,"city":"Ipswich"},{"name":"Ryan","age":28,"city":"Ipswich"}]'
    bar = jsonData(Databae_data)

#Example data    
Databae_data = '[{"name":"Carl","age":34,"city":"Ipswich"},{"name":"Carl","age":28,"city":"Ipswich"},{"name":"Kevin","age":28,"city":"Ipswich"},{"name":"Owen","age":28,"city":"Ipswich"},{"name":"Ryan","age":28,"city":"Ipswich"}]'

#EXAMPLES of using and handling:
#Creates object holding example JSON data
myObject = jsonData(Databae_data)
#Searches and prints the returned list
#print("Printing result of search for the 'name' of 'Carl':")
#print(myObject.search("name","Carl"))
#Creates new object
f = Foo()
f.data = "New"
#Sets newObj with result list
#'True' bool given to make filter require all conditions to be met
#newObj.data = myObject.filter(True, name="Carl", age=28)

