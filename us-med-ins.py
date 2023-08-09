import csv
from collections import Counter
from matplotlib import pyplot as plt

my_file = "insurance.csv"

fields = []
rows = []

#Reading File
with open(my_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)

#Info
print("The total number of clients is: " + str(len(rows)))
print("The fields are: " + ', '.join(field for field in fields))

#Client Averages Stats
class ClientStats:
    def __init__(self):
        pass

    def average_age(self, rows):
        total = 0
        for i in range(len(rows)):
            age = int(rows[i][0])
            total += age
            average_age = float(total)/float(len(rows))
        return average_age

    def average_cost(self, rows):
        total = 0
        for i in range(len(rows)):
            cost = float(rows[i][-1])
            total += cost
            average_cost = float(total)/float(len(rows))
        return average_cost

    def male_v_female(self, rows):
        males = []
        females = []
        for i in range(len(rows)):
            sex = rows[i][1]
            if sex == 'male':
                males.append(rows[i])
            else:
                females.append(rows[i])
        total_m = 0
        for i in range(len(males)):
            cost = float(males[i][-1])
            total_m += cost 
            average_m_cost = total_m/float(len(males))
        total_f = 0
        for i in range(len(females)):
            cost = float(females[i][-1])
            total_f += cost
            average_f_cost = total_f/float(len(females))
        return [round(average_m_cost, 2), round(average_f_cost, 2)]
    
    def average_bmi(self, rows):
        total = 0
        for i in range(len(rows)):
            bmi = float(rows[i][2])
            total += bmi
            average_bmi = float(total)/float(len(rows))
        return average_bmi
    
    def location(self, rows):
        locations = []
        for i in range(len(rows)):
            location = rows[i][-2]
            locations.append(location)
        num_area = Counter(locations)
        return num_area

    def calculate(self, rows):
        average_cost = self.average_cost(rows)
        average_cost = round(average_cost, 2)
        print(f"The average cost for clients is: ${average_cost}.")

        mvf_cost = self.male_v_female(rows)
        print(f"Males average cost is ${mvf_cost[0]} and females average cost is ${mvf_cost[1]}.")

        average_age = self.average_age(rows)
        average_age = round(average_age, 2)
        print(f"The average age of clients is: {average_age} years old.")

        average_bmi = self.average_bmi(rows)
        average_bmi = round(average_bmi, 2)
        print(f"The average bmi of clients is: {average_bmi}.")

        location = self.location(rows)
        print(f"Clients reside from the following geographical areas: {location}")

stats = ClientStats()
stats.calculate(rows)


#Plotting Cost Correlations

bmi = []
cost = []
smoker = []

for i in range(len(rows)):
    bmi.append(float(rows[i][2]))
for i in range(len(rows)):
    cost.append(float(rows[i][-1]))
for i in range(len(rows)):
    smoker.append(rows[i][-3])
    


plt.title("BMI vs Cost Correlation")
plt.xlabel("BMI")
plt.ylabel("Cost")
plt.scatter(bmi, cost)
plt.show()

plt.title("Smoker vs Cost Correlation")
plt.xlabel("Smoker")
plt.ylabel("Cost")
plt.bar(smoker, cost)
plt.show()









