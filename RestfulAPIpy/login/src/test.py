import requests

BASE_URL = "http://127.0.0.1:5000/"

data = [{"likes": 78,"name": "Joe", "views":10000},
        {"likes": 72228 ,"name": "Apı", "views":564654},
        {"likes": 34 , "name": "3123QWE", "views":2000}]

for i in range(len(data)):
    response = requests.put(BASE_URL+ "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.patch(BASE_URL + "video/2", {"views":31} )
print(response.json())