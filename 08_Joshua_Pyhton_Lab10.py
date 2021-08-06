import pandas as pd
# Create a python series using list to add, subtract, multiply and divide another panda series
ps1 = pd.Series([1, 3, 5, 7, 9])
ps2 = pd.Series([2, 4, 6, 8, 10])
# Create another python series to add, subtract, multiply and divide from previous series
ps = ps1 + ps2
print(ps)

ps = ps2 - ps1
print(ps)

ps = ps2 *ps1
print(ps)

ps = ps2 / ps1
print(ps)

# Compare the elements in the above series (compare will output Boolean result)
print(ps2 == ps1)
print(ps2 > ps1)
print(ps2 < ps1)



# Create a panda series with dictionary:
dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
psd = pd.Series(dict)
print(psd)





# Create a numPy Array first before converting it to panda Series:
import numpy as np
np_array = np.array([10, 20, 30, 40, 50])
print(np_array)

ps_numArray = pd.Series(np_array)
print(ps_numArray)


# Convert a panda series object to numeric:
s1 = pd.Series([10, '20', 'python', '48', '50'])
print(s1)

s2 = pd.to_numeric(s1, errors='coerce')
print(s2)

# Add new data to the s2 series:
s2 = s2.append(pd.Series([60, 70]))
print(s2)

# Sort the value of s2 series to sorted_s2:
sorted_s2 = s2.sort_values()
print(sorted_s2)

# Re-index sorted_s2 series:
sorted_s2.index = [1, 2, 3, 4, 5, 6, 7]
print(sorted_s2)




# Calculate the mean, median and standard deviation of the sorted list:
sorted_s2.mean()
sorted_s2.median()
sorted_s2.std()

# Convert the above series to a list:
var1 = s2.values.tolist()
print(var1)
type(var1)

# Convert the above list to numpy array:
npArray = np.array(var1)
print(npArray)
type(npArray)

# Combine a series of list to panda series and store only the distinct color:
import pandas as pd
colorList = pd.Series([
    ['Red', 'Blue', 'Yellow'],
    ['Red', 'White'],
    ['Black']])
print(colorList)

s = colorList
s = s.apply(pd.Series).stack().reset_index(drop=True)
print(s)




# Create a dataframe using a single list or list of list:
list  = [1, 2, 3, 4, 5]
df = pd.DataFrame(list)
print(df)


listOflist = [['Mike', 5], ['Peter', 10], ['Thomas', 15]]
df = pd.DataFrame(listOflist,columns=['Name', 'Age'])
print(df)

#Create a dataframe using a dictionary data structure:
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
        "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Bloemfontein"],
        "area": [8.516, 17.10, 3.286, 9.597, 1.221],
        "population": [200.4, 143.5, 1252, 1357, 52.98] }

brics = pd.DataFrame(dict)
print(brics)

# Change or set the index for brics.
# Set the index for brics
brics.index = ["BR", "RU", "IN", "CH", "SA"]

# Print out brics with new index values
print(brics)


# Using Dataframe to read CSV file:
# Import the cars.csv data: cars
cars = pd.read_csv('mtcars.csv')

#print out cars
print(cars)

# Using head() to read first 5 rows and tail() to read last 5 rows:
cars.head()

# Use columns to read only the columns header:
cars.columns

# Display the original index:
cars.index # Print original indexes

# Create another dataframe by spliting the Car Brand and Model
car = cars['model'].str.split(' ', n = 1, expand=True)
print(car)

# Assign the new car brand and models back to the original dataframe.
cars = cars.assign(car_brand=car[0]) # assign a new column named car_brand
print(cars)
cars = cars.assign(car_model=car[1]) # assign a new column car_brand
print(cars)
cars[cars['car_brand'] == 'Mazda'] # search for car_brand belonging to Mazda
print(cars)

# Change the index to Car mode
cars.index = cars ['model'] # Set indexes to car name
print(cars)
del cars['model']             # Delete the model column
print(cars)                  #print new indexes





cars.iloc[:,:6].describe()      # Summarize the first 6 columns

# Display the Car new info for 10 records:
print(cars.head(10))

# Find the mean for the dataframe columns:
print(cars.mean())


# Using matplotlib to plot a graph relationship between mile per gallon (mpg) to horse power(hp):
import matplotlib.pyplot as plt
#plt.scatter (cars['mpg'], cars['hp'])
#plt.show();     #or plt.savefig("name.png")


# Using matplotlib to plot a bar chart to shows the horse power of each car model.
#fig = plt.figure
#ax = cars[['car_model', 'hp']].plot(kind='bar', title="Horse Power comparison")
#plt.show()

# Plot a histogram to show the category of Horse Power in most cars.
fig = plt.figure
ax = cars['hp'].plot(kind='hist', title="Range in HP", figsize=(10, 10), legend=True, fontsize=12)
plt.show()

# Saving the histogram diagram in a png format in the current directory of program executed.
my_fig = ax.get_figure()        # Get the figure
my_fig.savefig("Car_Range_HP.png")  #Save to file

# Write the following code to find the most fuel-efficient car in the data file and present the result in bar chart in ascending order.
ps = cars['mpg'].sort_values()
index = np.arange(len(ps.index))
plt.xlabel('Models', fontsize=10)
plt.ylabel('Models', fontsize=5)
plt.xticks(index, ps.index, fontsize=10, rotation=90)
plt.title('Miles per gallon of Cars')
plt.bar(ps.index, ps.values)
plt.show();     #or plt.savefig("name.png")







