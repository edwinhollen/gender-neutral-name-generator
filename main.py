import random
import sys
import json

namesToGenerate = 10
firstNames = []
lastNames = []

if len(sys.argv) > 1:
    namesToGenerate = int(sys.argv[1])

with open('./last_names.json') as lastNamesFile:
    lastNames = json.load(lastNamesFile)

with open('./first_names.json') as firstNamesFile:
    firstNames = json.load(firstNamesFile)

for i in range(namesToGenerate):
    firstName = random.choice(firstNames)
    lastName = random.choice(lastNames)
    print(firstName + ' ' + lastName)