from disasterLibrary import *

addUserInfo("Test", 94539, 1230984567)

for shelter in getShelters(94539, True):
	print(shelter)