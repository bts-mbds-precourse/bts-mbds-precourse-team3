import csv
f=open('C:\\Users\\jordi\\Downloads\\train.csv')
Sniffer = csv.Sniffer()
dialect = Sniffer.sniff(f.read(2048))
print(dialect)
f.seek(0)
reader = csv.reader(f,dialect)
Passenger_Id = []
Survived = []
Pclass = []
Name = []
Sex = []
Age = []
Sibsp = []
Parch = []
Ticket = []
Fare = []
Cabin = []
Embarked = []
for row in reader:
    Passenger_Id.append(row[0])
    Survived.append(row[1])
    Pclass.append(row[2])
    Name.append(row[3])
    Sex.append(row[4])
    Age.append(row[5])
    Sibsp.append(row[6])
    Parch.append(row[7])
    Ticket.append(row[8])
    Fare.append(row[9])
    Cabin.append(row[10])
    Embarked.append(row[11])
print(Passenger_Id)
print(Survived)
print(Pclass)
print(Name)
print(Sex)
print(Age)
print(Sibsp)
print(Parch)
print(Ticket)
print(Cabin)
print(Embarked)


import matplotlib
import scipy
import pandas as pd
df = pd.read_csv('C:\\Users\\jordi\\Downloads\\train.csv')

import pandas
df = pandas.read_csv('C:\\Users\\jordi\\Downloads\\train.csv', index_col='Name', parse_dates=['Survived'])
print(df['Survived'])

import matplotlib.pyplot as plt

data = {'Pclass': 1, 'Sex': 'female'}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey = True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)
fig.suptitle('Categorical Plotting')

plt.show()