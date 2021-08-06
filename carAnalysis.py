import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Import the cars.csv data: cars
    cars = pd.read_csv('mtcars.csv')
    car = cars['model'].str.split(' ', n = 1, expand = True)
    cars = cars.assign(car_brand=car[0]) # Assign a new column named car_brand
    cars = cars.assign(car_model=car[1]) # Assign a new column named car_brand
    cars.index = cars ['model'] # Set index to car name
    del cars ['model']  # Delete model column

    plt.scatter(cars['mpg'], cars['hp'])
    plt.savefig("scatterDiagram_mpg_hp.png")

    ax = cars[['car_model', 'hp']].plot(kind='bar', title = "Horse Power Comparison", figsize=(15, 15), legend=True, fontsize=12)
    my_fig = ax.get_figure()            # Get the figure
    my_fig.savefig ("Horse_power_comparison.png")   #Save to file

    ax = cars['hp'].plot(kind='hist', title="Range in HP", figsize=(10, 10),legend=True, fontsize=12)
    my_fig = ax.get_figure()        # get the figure
    my_fig.savefig("Car_Range_HP,png")  #save to file

if __name__ == '__main__':
 main()