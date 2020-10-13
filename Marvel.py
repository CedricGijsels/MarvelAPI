#Import these 3 modules
import urllib.parse
import requests
import hashlib

#Link to connect to API
api = "http://gateway.marvel.com/v1/public/characters?"
#Your public key (provide your own ;) )
public_key = "9c1c31539bc187b82ae4f5c34a7f9736"
#Give a timestamp
timestamp = "1"
#Your private key (again provide your own ;) )
private_key = "c28a6df6f619b886c39fdbad71f960a2d2b27008"
pre_hash = timestamp + private_key + public_key
#MD5 hash
result = hashlib.md5(pre_hash.encode())

while True:
    name = input("What character do you want to look up? (give a blank to stop)")
    if name == "":
        break
    url = api + urllib.parse.urlencode({"name": name, "ts":timestamp, "apikey":public_key, "hash":result.hexdigest()})
    #This is the JSON data of the API
    data = requests.get(url).json()
    status = data["code"]
    if status == 200:
        if data["data"]["total"] == 0:
            print("Not found, are you sure he/she exists?")
        else:
            print("API status: " + str(status))
            print("Name: " + name)
            print("Description: " + str(data["data"]["results"][0]["description"]))
            print(name + " appears in these comics.")
            print("--------------------------------------------------")
            #Here we loop over the different comics
            for each in data["data"]["results"][0]["comics"]["items"]:
                print(each["name"])
            print("--------------------------------------------------\n")