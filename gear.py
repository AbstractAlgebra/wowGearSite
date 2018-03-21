import urllib.request
import json
import time

import requests

def achvLookup(achvNum):
	url = "https://us.api.battle.net/wow/achievement/" + achvNum + "?locale=en_US&apikey=m7z72pa2f75dsa4mmnx8du7cfrpfbt5u"
	response = urllib.request.urlopen(url)


	data = json.loads(response.read())
	print(data['title'])
	print(data['rewardItems'][0]['name'])
#	print (response.read())

#achvNum = input("Enter the achievement number you would like to look up. ")
#achvLookup(achvNum)
def classConverter(charClass):
	url = "https://us.api.battle.net/wow/data/character/classes?locale=en_US&apikey=m7z72pa2f75dsa4mmnx8du7cfrpfbt5u"
	response = urllib.request.urlopen(url)
	data = json.loads(response.read())
	return data['classes'][charClass-1]['name']

def raceConverter(charRace):
	url = "https://us.api.battle.net/wow/data/character/races?locale=en_US&apikey=m7z72pa2f75dsa4mmnx8du7cfrpfbt5u"
	response = urllib.request.urlopen(url)
	data = json.loads(response.read())	
	
	#charRace = 10 BLOOD ELF
	
	if charRace == 22:
		return data['races'][charRace-11]['name']
	
	if charRace > 22:
		offset = 11
		counter = 1
		for i in range(24,31):
			if charRace != i:
				counter += 1
			else: 
				return data['races'][offset+counter]['name']

	return data['races'][charRace-1]['name']

def charLookup(realmName, charName, fields = ""):
	url = "https://us.api.battle.net/wow/character/" + realmName + "/" + charName + "?locale=en_US&apikey=m7z72pa2f75dsa4mmnx8du7cfrpfbt5u"
	response = urllib.request.urlopen(url)
	data = json.loads(response.read())
	print("Character Name: " + data['name'])
	print("Character Realm: " + data['realm'])
	print("Character Class: " + classConverter(data['class']))
	print("Character Race: " + raceConverter(data['race']))
	print("The last time this character logged in was: " + str(time.strftime('%c',time.localtime(data['lastModified']/1000))))


def gearLookup(realmName, charName):
	url = "https://us.api.battle.net/wow/character/" + realmName + "/" + charName + "?fields=items&locale=en_US&apikey=m7z72pa2f75dsa4mmnx8du7cfrpfbt5u"
	response = requests.get(url)
	data = json.loads(response.content)
	print("Character Name: " + data['name'])
	print("Character Realm: " + data['realm'])

	iconURL = "https://wow.zamimg.com/images/wow/icons/large/" + data['items']['head']['icon'] + ".jpg"

	print(iconURL)



gearLookup("Tichondrius","Flannel")
