import csv

newData = []

with open('demoData.csv', 'rt', encoding='UTF8') as readFile:
    listOfRows=csv.reader(readFile, delimiter=',')
    for row in listOfRows:
        newRow = []
        for element in row:
            newElement=""
            for index in range(len(element)):
                # newElement is nog leeg dus voegen we het eerste element toe (als hoofdletter).
                if(len(newElement)==0):
                    newElement += element[index].upper()
                else:
                    # is het nieuwe element text?
                    if(newElement.isalpha() and element[index].isalpha()):
                        newElement += element[index]
                    # is het nieuwe element een getal?
                    elif(newElement.isdigit() and element[index].isdigit()):
                        newElement+=element[index]
            # newElement is een getal
            if(newElement.isdigit()):
                newRow.append(int(newElement))
            # newElement is geen getal.
            else:
                newRow.append(newElement)
        newData.append(newRow)

for row in newData:
    print(row)
