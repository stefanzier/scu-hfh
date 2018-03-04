from pymongo import MongoClient
from itertools import chain
import urllib.request, json
import ssl

# This is the library for inserting new info and accessing info based on searches
# Check for the function signatures for clear and simple ways to use the functions of this library

# Insertion
def addShelter(name, zipcode, address, capacity, services, active):
	client = MongoClient("mongodb://scuhfh:gobroncos@disasterinfo-shard-00-00-vhxix.mongodb.net:27017,disasterinfo-shard-00-01-vhxix.mongodb.net:27017,disasterinfo-shard-00-02-vhxix.mongodb.net:27017/test?ssl=true&replicaSet=DisasterInfo-shard-0&authSource=admin", ssl=True)
	db = client.DisasterInfo
	shelters = db.shelters # Collection name inside database
	
	shelter_data = { # Creating data packet
		'Name': name,
      	'ZIP': int(zipcode),
		'Address': address,
		'Capacity': capacity,
      	'Services': services,
		'Visitors' : 0,
      	'Active': active
	}
	result = shelters.insert_one(shelter_data) # Pushing data to database
	return ('Posted: {0}'.format(result.inserted_id))

# name zip addy
def addProvisions(name, zipcode, address, active):
	client = MongoClient("mongodb://scuhfh:gobroncos@disasterinfo-shard-00-00-vhxix.mongodb.net:27017,disasterinfo-shard-00-01-vhxix.mongodb.net:27017,disasterinfo-shard-00-02-vhxix.mongodb.net:27017/test?ssl=true&replicaSet=DisasterInfo-shard-0&authSource=admin", ssl=True)
	db = client.DisasterInfo
	provisions = db.provisions # Collection name inside database

	provision_data = { # Creating data packet
		'Name': name,
		'ZIP': int(zipcode),
		'Address': address,
		'Visitors' : 0,
		'Active': active
	}
	result = provisions.insert_one(provision_data)
	return ('Posted: {0}'.format(result.inserted_id))

def addUserInfo(name, zipcode, phoneNum):
	client = MongoClient("mongodb://scuhfh:gobroncos@disasterinfo-shard-00-00-vhxix.mongodb.net:27017,disasterinfo-shard-00-01-vhxix.mongodb.net:27017,disasterinfo-shard-00-02-vhxix.mongodb.net:27017/test?ssl=true&replicaSet=DisasterInfo-shard-0&authSource=admin", ssl=True)
	db = client.DisasterInfo
	userInfo = db.userInfo
	
	if isinstance(phoneNum, str):
		phoneNum = phoneNum.replace('+', '').replace('-', "").replace(' ', '').replace('(', '').replace(')', '')
		phoneNum = int(phoneNum)
	
	if userInfo.find({'Phone Number' : phoneNum}).count() > 0:
		return userInfo.find({'Phone Number' : phoneNum})
	
	
	user_data = { # Create data packet
		'Name': name,
		'ZIP': int(zipcode),
      	'Phone Number': phoneNum
	}
	result = userInfo.insert_one(user_data)
	return ('Post ID: {0}'.format(result.inserted_id))

def addImportantItems(disaster, items):
	client = MongoClient("mongodb://scuhfh:gobroncos@disasterinfo-shard-00-00-vhxix.mongodb.net:27017,disasterinfo-shard-00-01-vhxix.mongodb.net:27017,disasterinfo-shard-00-02-vhxix.mongodb.net:27017/test?ssl=true&replicaSet=DisasterInfo-shard-0&authSource=admin", ssl=True)
	db = client.DisasterInfo
	importantItems = db.importantItems

	items_data = { # Create data packet
		'Disaster': disaster,
		'Items': items
	}
	result = importantItems.insert_one(items_data)
	return ('Post ID: {0}'.format(result.inserted_id))
	
	
# RETRIEVAL

# change graph
def getShelters(zipcode, nearby):
	client = MongoClient("mongodb://scuhfh:gobroncos@disasterinfo-shard-00-00-vhxix.mongodb.net:27017,disasterinfo-shard-00-01-vhxix.mongodb.net:27017,disasterinfo-shard-00-02-vhxix.mongodb.net:27017/test?ssl=true&replicaSet=DisasterInfo-shard-0&authSource=admin", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
	db = client.DisasterInfo
	shelters = db.shelters # Collection name inside database
	#shelter_posts = shelters.find({'ZIP' : zipcode, 'Active' : True})
	shelter_posts = shelters.find({'ZIP' : 00000, 'Active' : True})
	
	if nearby:
		zipcodes = nearbyZipcodes(zipcode)
		for zipcode in zipcodes:
			tempShelters = shelters.find({'ZIP' : zipcode, 'Active' : True})
			shelter_posts = [x for x in chain(shelter_posts, tempShelters)]

	return shelter_posts

def getProvisions(zipcode, nearby):
	client = MongoClient("mongodb://scuhfh:gobroncos@disasterinfo-shard-00-00-vhxix.mongodb.net:27017,disasterinfo-shard-00-01-vhxix.mongodb.net:27017,disasterinfo-shard-00-02-vhxix.mongodb.net:27017/test?ssl=true&replicaSet=DisasterInfo-shard-0&authSource=admin", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
	db = client.DisasterInfo
	provisions = db.provisions # Collection name inside database

	if nearby:
		zipcodes = nearbyZipcodes(zipcode)
		for zipcode in zipcodes:
			tempProvisions = provisions.find({'ZIP' : zipcode, 'Active' : True})
			provisions_posts = [x for x in chain(provisions_posts, tempProvisions)]
	
	provisions_posts = provisions.find({'ZIP' : zipcode, 'Active' : True})
	return provisions_posts

def getUserInfo(phoneNum):
	client = MongoClient("mongodb://scuhfh:gobroncos@disasterinfo-shard-00-00-vhxix.mongodb.net:27017,disasterinfo-shard-00-01-vhxix.mongodb.net:27017,disasterinfo-shard-00-02-vhxix.mongodb.net:27017/test?ssl=true&replicaSet=DisasterInfo-shard-0&authSource=admin", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
	db = client.DisasterInfo
	userInfo = db.userInfo # Collection name inside database

	if isinstance(phoneNum, str):
		phoneNum = phoneNum.replace('+', '').replace('-', "").replace(' ', '').replace('(', '').replace(')', '')
		phoneNum = int(phoneNum)
	
	userInfo_post = userInfo.find_one({'Phone Number' : phoneNum})
	return userInfo_post

def nearbyZipcodes(zipcode):
	zipcodes = []

	urlPage = 'https://www.zipcodeapi.com/rest/LJkqEki0QKzPWMYUcMo9xDImL6M1ePFlKbTPyQylK2i4FYKzY7TzeJARiiwFzECr/radius.json/' + str(zipcode) + '/5/mile?minimal'
	
	with urllib.request.urlopen(urlPage) as url:
		data = json.loads(url.read().decode())
		for zipcode in data['zip_codes']:
			zipcodes.append(int(zipcode))
	zipcodes.remove(int(zipcode))
	return zipcodes	

	
# UPDATING

def incrShelterVisitors(name):
	client = MongoClient("mongodb://scuhfh:gobroncos@disasterinfo-shard-00-00-vhxix.mongodb.net:27017,disasterinfo-shard-00-01-vhxix.mongodb.net:27017,disasterinfo-shard-00-02-vhxix.mongodb.net:27017/test?ssl=true&replicaSet=DisasterInfo-shard-0&authSource=admin", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
	db = client.DisasterInfo
	shelters = db.shelters
	shelters.update_one({'Name' : name}, {'$inc': {'Visitors' : 1}}, upsert=False)

def clearShelterVisitors(name):
	client = MongoClient("mongodb://scuhfh:gobroncos@disasterinfo-shard-00-00-vhxix.mongodb.net:27017,disasterinfo-shard-00-01-vhxix.mongodb.net:27017,disasterinfo-shard-00-02-vhxix.mongodb.net:27017/test?ssl=true&replicaSet=DisasterInfo-shard-0&authSource=admin", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
	db = client.DisasterInfo
	shelters = db.shelters
	shelters.update_one({'Name' : name}, {'$set': {'Visitors' : 0}}, upsert=False)
	
def renameShelter(name, newName):
	client = MongoClient("mongodb://scuhfh:gobroncos@disasterinfo-shard-00-00-vhxix.mongodb.net:27017,disasterinfo-shard-00-01-vhxix.mongodb.net:27017,disasterinfo-shard-00-02-vhxix.mongodb.net:27017/test?ssl=true&replicaSet=DisasterInfo-shard-0&authSource=admin", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
	db = client.DisasterInfo
	shelters = db.shelters
	shelters.update_one({'Name' : name}, {'$set': {'Name': newName}}, upsert=False)
	
def renameProvisions(name, newName):
	client = MongoClient("mongodb://scuhfh:gobroncos@disasterinfo-shard-00-00-vhxix.mongodb.net:27017,disasterinfo-shard-00-01-vhxix.mongodb.net:27017,disasterinfo-shard-00-02-vhxix.mongodb.net:27017/test?ssl=true&replicaSet=DisasterInfo-shard-0&authSource=admin", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
	db = client.DisasterInfo
	provisions = db.provisions
	provisions.update_one({'Name' : name}, {'$set': {'Name': newName}}, upsert=False)

def updateShelterActive(name, active):
	client = MongoClient("mongodb://scuhfh:gobroncos@disasterinfo-shard-00-00-vhxix.mongodb.net:27017,disasterinfo-shard-00-01-vhxix.mongodb.net:27017,disasterinfo-shard-00-02-vhxix.mongodb.net:27017/test?ssl=true&replicaSet=DisasterInfo-shard-0&authSource=admin", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
	db = client.DisasterInfo
	shelters = db.shelters
	shelters.update_one({'Name' : name}, {'$set': {'Active': active}}, upsert=False)
    
def updateProvisionsActive(name, active):
	client = MongoClient("mongodb://scuhfh:gobroncos@disasterinfo-shard-00-00-vhxix.mongodb.net:27017,disasterinfo-shard-00-01-vhxix.mongodb.net:27017,disasterinfo-shard-00-02-vhxix.mongodb.net:27017/test?ssl=true&replicaSet=DisasterInfo-shard-0&authSource=admin", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
	db = client.DisasterInfo
	provisions = db.provisions
	provisions.update_one({'Name' : name}, {'$set': {'Active': active}}, upsert=False)