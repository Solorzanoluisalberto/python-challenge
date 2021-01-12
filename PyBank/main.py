# main PyBank file
# dataset is composed of two columns: "Date" and "Profit/Losses"
import csv
from numpy import mean
import statistics
listasuma = []
listavalor = []
with open('Resources/budget_data.csv') as file:
    reader = csv.DictReader(file, delimiter=',')
    count = 0
    suma = 0
    #lineas = len(reader[])
    for row in reader:
    # suma = suma + int(row['Profit/Losses'])
        listasuma.append(int(row['Profit/Losses'])) # assign to a list
        listavalor.append(row['Date']) # assign to a list
        suma = suma + int(row['Profit/Losses']) # acumulate all Profit/Losses values
        count = count + 1 # count += 1
average = round(suma/count,2) # average from list value 
average1 = round(sum(listasuma)/len(listasuma),2) # average from list value 
print(" Financial Analysis ")
print(" --------------------- ")
print('Total Months: ', count)
#moneda = "${:,.2f}".format(suma)
print('Total:', ("${:}".format(suma))) # ("${:,.2f}".format(suma)))
print("Average Change: ", ("${:2}".format(round((listasuma[-1]-listasuma[0])/(len(listasuma)-1),2)))) # print average change 
minimoindex = min(listasuma) # minimum value in the data set
maximoindex = max(listasuma) # maximum value in the data set
minimoindex = listasuma.index(minimoindex) # index of the minimum value in the data set
maximoindex = listasuma.index(maximoindex) # index of the maximum value in the data set
print("Greatest Increase in Profits: ", listavalor[maximoindex] , "(","${:2}".format(max(listasuma)),")") # print greates value
print("Greatest Decrease in Profits: ", listavalor[minimoindex] , "(","${:2}".format(min(listasuma)),")") # print minimun value
#avera = mean(listasuma)  # average from list value

