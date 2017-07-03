import requests
import json
import sys


jsonString = '[{"dumbell_id": "58dfca3f1d3448278f2fc68a","workout":' + '"' + sys.argv[2] + '"' + ',"reps":' + sys.argv[3] + ',"form":' + sys.argv[4] + '}]'
#HTTP Post request on z
head = {'Content-Type': 'application/json'}
print jsonString
r = requests.post('http://46.101.3.244:8080/api/workoutData', data = jsonString, headers=head)
print(r)
