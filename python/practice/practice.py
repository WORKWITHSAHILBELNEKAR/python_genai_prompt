import csv 

with open('data.csv','r') as file :
    content =  csv.reader(file)
    
    for row in content:
        print (row)

data = [["sahil" , 23],["sasa", 22]]

with open ('data.csv','w') as file:
    writer = csv.writer(file)
    writer.writerows(data)