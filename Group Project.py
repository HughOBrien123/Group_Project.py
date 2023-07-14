import pandas as pd, matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
businesses = pd.read_csv('https://data.cityofnewyork.us/api/views/w7w3-xahh/rows.csv?accessType=DOWNLOAD')


# Initialize count variables for each borough, other categories, and states
Brooklyn_Count = 0
Bronx_Count = 0
Manhattan_count = 0
Queens_count = 0
Staten_Island_count = 0
Outside_count = 0
Undefined = 0
New_York_Count = 0
Inactive_count = 0

# Iterate over each row in the DataFrame
for Business_Type in businesses.values:
    # Extract relevant information from the row
    Type_of_Business = Business_Type[1]
    State = Business_Type[12]
    Borough = Business_Type[15]
    Activity = Business_Type[3]

    # Check conditions and increment the corresponding count variables
    if Type_of_Business == 'Business' and State == 'NY' and Borough == 'Brooklyn' and Activity == 'Active':
        Brooklyn_Count += 1

    if Type_of_Business == 'Business' and State == 'NY' and Borough == 'Bronx' and Activity == 'Active':
        Bronx_Count += 1

    if Type_of_Business == 'Business' and State == 'NY' and Borough == 'Manhattan' and Activity == 'Active':
        Manhattan_count += 1

    if Type_of_Business == 'Business' and State == 'NY' and Borough == 'Staten Island' and Activity == 'Active':
        Staten_Island_count += 1

    if Type_of_Business == 'Business' and State == 'NY' and Borough == 'Queens' and Activity == 'Active':
        Queens_count += 1

    if Type_of_Business == 'Business' and State == 'NY' and Borough == 'Outside NYC' and Activity == 'Active':
        Outside_count += 1

    if Type_of_Business == 'Business' and State == 'NY' and Activity == 'Active':
        New_York_Count += 1

    if Type_of_Business == 'Business' and State == 'NY' and Activity == 'Inactive':
        Inactive_count += 1

# Print the results
print("Below are the statistics of buisness licenses in the state of New york: ")
print(f"There is a total of {New_York_Count:,} active businesses in New York")
print(f"There is a total of {Inactive_count:,} inactive accounts in New York City")
print(f"In Brooklyn, there are {Brooklyn_Count:,} active businesses")
print(f"In Manhattan, there are {Manhattan_count:,} active businesses")
print(f"In Queens, there are {Queens_count:,} active businesses")
print(f"In The Bronx, there are {Bronx_Count:,} active businesses")
print(f"In Staten Island, there are {Staten_Island_count:,} active businesses")
print(f"Outside of New York City, there are {Outside_count:,} active businesses")

#Next get the population numbers from data of New York's population
NYC_population = 8631987
bronx_population = 1468451
Brooklyn_populaition = 2679948
Manhattan_population = 1649809
Queens_population = 2343273
Staten_Island_population = 490333

#Divide the population by the number of businesses to find ratio
NYC_P_to_B = (8631987 / int(New_York_Count))
Bronx_P_to_B = (1468451 / int(Bronx_Count))
brooklyn_P_to_B = (2679948/int(Brooklyn_Count))
Manhattan_P_to_B = (1649809/int(Manhattan_count))
Queens_P_to_B = (2343273/int(Queens_count))
Staten_Island_P_to_B = (490333/int(Staten_Island_count))

#Print the results
print("\n" + "Now we will compare the population of the boroughs to the amount of businesses in those boroughs: ")
print(f"The population of NYC is {NYC_population:,}. The ratio of people to businesses is {NYC_P_to_B:.2f}")
print(f"The population of The Bronx is {bronx_population:,}. The ratio of people to businesses is {Bronx_P_to_B:.2f}")
print(f"The population of Brooklyn is {Brooklyn_populaition:,}. The ratio of people to businesses is {brooklyn_P_to_B:.2f}")
print(f"The population of Manhattan is {Manhattan_population:,}. The ratio of people to businesses is {Manhattan_P_to_B:.2f}")
print(f"The population of Queens is {Queens_population:,}. The ratio of people to businesses is {Queens_P_to_B:.2f}")
print(f"The population of Staten_Island is {Staten_Island_population:,}. The ratio of people to businesses is {Staten_Island_P_to_B:.2f}")

#get years and numbers from file to make line graph
year= [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030, 2040]
Bronx_total = [1451277, 1424815, 1471701, 1168972, 1203789, 1332650, 1385108, 1446788, 1518998, 1579245]
Brooklyn_total = [2738175, 2627319, 2602012, 2230936, 2300664, 2465326, 2552911, 2648452, 2754009, 2840525]
Manhattan_total = [1960101, 1698281, 1539233, 1428285, 1487536, 1537195, 1585873, 1638281, 1676720, 1691617]
Staten_total = [191555, 221991, 295443, 352121, 378977, 443728, 468730, 487155, 497749, 501109]
Queens_total = [1550849, 1809578, 1986473, 1891325, 1951598, 2229379, 2250002, 2330295, 2373551, 2412649]
my_colors = ["blue", "yellow", "red", "purple"]

#created a while loop to ask the user which graph they want to see and instructions to do so
print("\n" + "Along with this data comes two different graphes represnting the population statistcs over time with estamite into the future and a graph showing the amount of businesses per borough: ")
while True:
    user_input = input("Would you like to see further information on the population or the buisnesses? Type 'p' for population or type 'b' for buisness. Close the tab if you want to change your input. Press 'q' to cancel. ").lower()
    if user_input == 'p':
        plt.plot(year, Brooklyn_total, color = "#800000", label = "Brooklyn")
        plt.plot(year, Queens_total, color = "#00C957", label = "Queens")
        plt.plot(year, Manhattan_total, color = "#FFD700",  label = "Manhattan")
        plt.plot(year, Bronx_total, color = "red", label ="Bronx")
        plt.plot(year, Staten_total,color = "#000080", label = "Staten Island")
        plt.title("A line graph showing the population of the boroughs over time from 1950 to an estimate of 2030 and 2040 ")
        plt.xlabel("Year")
        plt.ylabel("Boroughs (in millions)")
        plt.legend()
        plt.show()
        continue
    elif user_input == 'b':
        Business_bar = [Queens_count, Brooklyn_Count, Manhattan_count, Bronx_Count, Staten_Island_count]
        Boroughs = ["Queens", "Brookyln", "Manhattan","Bronx", "Staten Island"]
        plt.bar(Boroughs, Business_bar, color=("#00C957", "#800000", "#FFD700", "red", "#000080"))
        plt.title("Businesses By Area")
        plt.xlabel("Boroughs")
        plt.ylabel("Amount")
        plt.show()
        continue
    elif user_input == 'q':
        break
    else:
        print("Invalid input, try again: ")
        continue