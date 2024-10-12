import csv
import copy

myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

for key, value in myVehicle.items():
    print("{} : {}".format(key,value))

myInventoryList = []

with open('car_fleet.csv') as csv_file:
    csvReader = csv.reader(csv_file, delimiter=',')  
    lineCount = 0  
    for row in csvReader:
        if lineCount == 0:
            print('Column names are: {}'.format(",".join(row)))  
            lineCount += 1  
        else:  
            print('vin: {} make: {}, model: {}, year: {}, range: {}, topSpeed: {}, zeroSixty: {}, mileage: {}'.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))  
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    print('Processed {} lines.'.format(lineCount))

currentVehicle = copy.deepcopy(myVehicle)

for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key,value))
        print("-----")