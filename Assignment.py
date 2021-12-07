import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests

# Print out the Plane code and Plane name from the below use of API
request=requests.get('https://api.travelpayouts.com/data/planes.json')

print(request.status_code)

print(request.text)

data=request.json()

for p in data:
    print(str('Plane code ') + p['code'] + str(' is ') + p['name'])
# ---------------------------------------------------------------------

# Import a CSN file into a Pandas DataFrame - view the head of the DataFrame
filename = 'Fleet Data.csv'
data = pd.read_csv(filename)
# print a few rows of the dataframe for sanity check
print(data.head())

# Replace missing values to be zero and name it to 'data_no_empty'
data_no_empty = data.fillna(0)
print(data_no_empty.head())

# Grouping by parent airline company calculating the current total number of aircraft
data_grouped = data_no_empty.groupby("Parent Airline")["Current"].sum()
print(data_grouped)

# Subsetting to find all the Airbus A320 operators
data_A320 = data_no_empty[data_no_empty["Aircraft Type"] == "Airbus A320"]
print(data_A320)

# Sorting airlines by current A320 size in descending order
data_A320_sorted = data_A320.sort_values("Current", ascending=False)
print(data_A320_sorted)


# Grouping by parent airline company calculating the current total number of aircraft
data_grouped_type = data_no_empty.groupby(["Parent Airline", "Aircraft Type"])["Current"].sum()
print(data_grouped_type)
print(data_grouped_type.shape)


# Indexing using Airline
data_airline_ind = data_no_empty.set_index("Airline")
print(data_airline_ind)

# Subsetting using loc to look for Air Hong Kong
print(data_airline_ind.loc["Air Hong Kong"])


# Creating list of dictionaries to make a dataframe for Airbus / Boeing aircraft type
list_of_dicts = [
    {"Aircraft Type": "Airbus A300", "Manufacturer": "Airbus"},
    {"Aircraft Type": "Airbus A310", "Manufacturer": "Airbus"},
    {"Aircraft Type": "Airbus A318", "Manufacturer": "Airbus"},
    {"Aircraft Type": "Airbus A319", "Manufacturer": "Airbus"},
    {"Aircraft Type": "Airbus A320", "Manufacturer": "Airbus"},
    {"Aircraft Type": "Airbus A320-200", "Manufacturer": "Airbus"},
    {"Aircraft Type": "Airbus A321", "Manufacturer": "Airbus"},
    {"Aircraft Type": "Airbus A321neo", "Manufacturer": "Airbus"},
    {"Aircraft Type": "Airbus A330", "Manufacturer": "Airbus"},
    {"Aircraft Type": "Airbus A340", "Manufacturer": "Airbus"},
    {"Aircraft Type": "Airbus A350", "Manufacturer": "Airbus"},
    {"Aircraft Type": "Airbus A350 XWB", "Manufacturer": "Airbus"},
    {"Aircraft Type": "Airbus A350-900", "Manufacturer": "Airbus"},
    {"Aircraft Type": "Airbus A380", "Manufacturer": "Airbus"},
    {"Aircraft Type": "Boeing 717", "Manufacturer": "Boeing"},
    {"Aircraft Type": "Boeing 727", "Manufacturer": "Boeing"},
    {"Aircraft Type": "Boeing 737", "Manufacturer": "Boeing"},
    {"Aircraft Type": "Boeing 737-800", "Manufacturer": "Boeing"},
    {"Aircraft Type": "Boeing 747", "Manufacturer": "Boeing"},
    {"Aircraft Type": "Boeing 757", "Manufacturer": "Boeing"},
    {"Aircraft Type": "Boeing 767", "Manufacturer": "Boeing"},
    {"Aircraft Type": "Boeing 777", "Manufacturer": "Boeing"},
    {"Aircraft Type": "Boeing 777-300", "Manufacturer": "Boeing"},
    {"Aircraft Type": "Boeing 787", "Manufacturer": "Boeing"},
    {"Aircraft Type": "Boeing 787 Dreamliner", "Manufacturer": "Boeing"}
]
all_airbus_boeing = pd.DataFrame(list_of_dicts)
print(all_airbus_boeing)

# Print the aircraft type vs manufacturer dataframe using iterrows:
for lab, row in all_airbus_boeing.iterrows():
    print(lab)
    print(row)


# Merge the manufacturer dataframe to the Fleet Data dataframe and create a new dataframe for only Airbus and Boeing

fleet_manufacturer = data_no_empty.merge(all_airbus_boeing, on='Aircraft Type')
print(fleet_manufacturer)

# Create visualisations

# group by aircraft type to see the current popularity of different aircraft types
type_by_company = fleet_manufacturer.groupby(["Aircraft Type"])["Current"].sum()
type_by_company.plot(kind="bar", title='Total Number of Aircraft Type Currently in the Fleet of All Top 100+ Airlines')
plt.show()

# current market share between Airbus and Boeing
type_by_manufacturer = fleet_manufacturer.groupby(["Manufacturer"])["Current"].sum()
type_by_manufacturer.plot(kind="pie", title='Current Market Share between Airbus and Boeing')
plt.show()

# future market share between Airbus and Boeing
future_type_by_manufacturer = fleet_manufacturer.groupby(["Manufacturer"])["Orders"].sum()
future_type_by_manufacturer.plot(kind="pie", title='Future Market Share between Airbus and Boeing')
plt.show()

# group by aircraft type to see the mean of the number of orders by number of the aircraft type users

orders_by_type = fleet_manufacturer.groupby(["Aircraft Type"])["Orders"].mean()
orders_by_type.plot(kind="bar", title='Mean of All Ordered Aircraft by Aircraft Type')
plt.show()





# Build a numpy array using columns 4-7 of the Fleet Data csv file, filling missing data as 0

data_array = np.genfromtxt(filename, delimiter= ',',skip_header= 1, filling_values= 0,usecols= [3,4,5,7])
# Print the data_array as sanity check
print("Numpy array as below")
print(data_array)

print("Numpy array from rows 1 - 10 as below")
print(data_array[:10])

# print out the shape of the data_array
print(data_array.shape)

# Use Numpy to calculate the total orders for each airline and each aircraft type
np_current_no = data_array[:,0]
np_future_order = data_array[:,1]
np_phased_out = data_array[:,2]
np_existing_order = data_array[:,3]

total_corrected = np_current_no + np_future_order + np_phased_out

past_future_total = np_existing_order + total_corrected
# Use Numpy to find out the mean of all aircraft in order
print(np.mean(past_future_total))



# Define a custom function
def greet(reader):
    print("Thank you for reading " + reader + ". Have a nice day.")

# Function call
greet('Mr. J')