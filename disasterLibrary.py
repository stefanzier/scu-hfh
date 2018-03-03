from pymongo import MongoClient

# This is the library for inserting new info and accessing info based on searches
# Check for the function signatures for clear and simple ways to use the functions of this library

# Insertion
def addShelter(name, zipcode, address, capacity, services, active):
	client = MongoClient("mongodb://scuhfh:gobroncos@disasterinfo-shard-00-00-vhxix.mongodb.net:27017,disasterinfo-shard-00-01-vhxix.mongodb.net:27017,disasterinfo-shard-00-02-vhxix.mongodb.net:27017/test?ssl=true&replicaSet=DisasterInfo-shard-0&authSource=admin")
	db = client.DisasterInfo
	shelters = db.shelters # Collection name inside database
	
	shelter_data = { # Creating data packet
		'Name': name,
      	'ZIP': zipcode,
		'Address': address,
		'Capacity': capacity,
      	'Services': services,
      	'Active': active
	}
	result = shelters.insert_one(shelter_data) # Pushing data to database
	return ('Posted: {0}'.format(result.inserted_id))
	
def addProvisions(name, address, zipcode, active):
	client = MongoClient("mongodb://scuhfh:gobroncos@disasterinfo-shard-00-00-vhxix.mongodb.net:27017,disasterinfo-shard-00-01-vhxix.mongodb.net:27017,disasterinfo-shard-00-02-vhxix.mongodb.net:27017/test?ssl=true&replicaSet=DisasterInfo-shard-0&authSource=admin")
	db = client.DisasterInfo
	provisions = db.provisions # Collection name inside database

	provision_data = { # Creating data packet
		'Name': name,
		'ZIP': zipcode,
		'Address': address,
		'Active': active
	}
	result = provisions.insert_one(provision_data)
	return ('Posted: {0}'.format(result.inserted_id))

def addUserInfo(name, zipcode, phoneNum):
	client = MongoClient("mongodb://scuhfh:gobroncos@disasterinfo-shard-00-00-vhxix.mongodb.net:27017,disasterinfo-shard-00-01-vhxix.mongodb.net:27017,disasterinfo-shard-00-02-vhxix.mongodb.net:27017/test?ssl=true&replicaSet=DisasterInfo-shard-0&authSource=admin")
	db = client.DisasterInfo
	userInfo = db.userInfo
	
	if isinstance(phoneNum, str):
		phoneNum = phoneNum.replace('+', '').replace('-', "").replace(' ', '').replace('(', '').replace(')', '')
		phoneNum = int(phoneNum)
	
	user_data = { # Create data packet
		'Name': name,
		'ZIP': zipcode,
      	'Phone Number': phoneNum
	}
	result = userInfo.insert_one(user_data)
	return ('Post ID: {0}'.format(result.inserted_id))

def addImportantItems(disaster, items):
	client = MongoClient("mongodb://scuhfh:gobroncos@disasterinfo-shard-00-00-vhxix.mongodb.net:27017,disasterinfo-shard-00-01-vhxix.mongodb.net:27017,disasterinfo-shard-00-02-vhxix.mongodb.net:27017/test?ssl=true&replicaSet=DisasterInfo-shard-0&authSource=admin")
	db = client.DisasterInfo
	importantItems = db.importantItems

	items_data = { # Create data packet
		'Disaster': disaster,
		'Items': items
	}
	result = importantItems.insert_one(items_data)
	return ('Post ID: {0}'.format(result.inserted_id))
	
# RETRIEVAL
	
def getShelters(zipcode):
	client = MongoClient("mongodb://scuhfh:gobroncos@disasterinfo-shard-00-00-vhxix.mongodb.net:27017,disasterinfo-shard-00-01-vhxix.mongodb.net:27017,disasterinfo-shard-00-02-vhxix.mongodb.net:27017/test?ssl=true&replicaSet=DisasterInfo-shard-0&authSource=admin")
	db = client.DisasterInfo
	shelters = db.shelters # Collection name inside database
	
	shelter_posts = shelters.find({'ZIP' : zipcode})
	return shelter_posts

def getProvisions(zipcode):
	client = MongoClient("mongodb://scuhfh:gobroncos@disasterinfo-shard-00-00-vhxix.mongodb.net:27017,disasterinfo-shard-00-01-vhxix.mongodb.net:27017,disasterinfo-shard-00-02-vhxix.mongodb.net:27017/test?ssl=true&replicaSet=DisasterInfo-shard-0&authSource=admin")
	db = client.DisasterInfo
	provisions = db.provisions # Collection name inside database

	provisions_posts = provisions.find({'ZIP' : zipcode})
	return provisions_posts

def getUserInfo(phoneNum):
	client = MongoClient("mongodb://scuhfh:gobroncos@disasterinfo-shard-00-00-vhxix.mongodb.net:27017,disasterinfo-shard-00-01-vhxix.mongodb.net:27017,disasterinfo-shard-00-02-vhxix.mongodb.net:27017/test?ssl=true&replicaSet=DisasterInfo-shard-0&authSource=admin")
	db = client.DisasterInfo
	userInfo = db.userInfo # Collection name inside database

	if isinstance(phoneNum, str):
		phoneNum = phoneNum.replace('+', '').replace('-', "").replace(' ', '').replace('(', '').replace(')', '')
		phoneNum = int(phoneNum)
	
	userInfo_post = userInfo.find_one({'Phone Number' : phoneNum})
	return userInfo_post

	
addUserInfo("Mickey", 94539, "(408)-966-8994")
print(getUserInfo("408-966-8994"))