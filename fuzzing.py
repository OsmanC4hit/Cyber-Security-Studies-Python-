import requests
URL = input("Site: ")
WordLists = input("Wordlists: ") 
Lists = open(WordLists,"r").readlines()
for x in range(0, len(Lists)):
    enum = Lists[0].replace("\n","")
    r = requests.get(URL+enum)
    if(r.status_code != 404):
        print(URL+enum + " -----> " + str(r.status_code))