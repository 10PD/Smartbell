import requests
import json

jsonString = '[{"dumbell_id": "58dfca3f1d3448278f2fc68a","workout": "Pi Test","reps": 80,"form": 97}]'
#HTTP Post request on z
head = {'Content-Type': 'application/json'}
r = requests.post('http://46.101.3.244:8080/api/workoutData', data = jsonString, headers=head)
print(r)
