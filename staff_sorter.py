import numpy as np
import pandas as pd
import math
import scipy.stats as scp
import matplotlib as plt


data = pd.read_csv("Staff.csv", sep = ";") 

data.boxplot(column = "Actual BD teams", by = "Shift")

##cleaned_data = data.drop(columns = ["DayOfMonth", "Year"])
grouped_mean = data.groupby(["DayOfWeek", "Shift"]).mean()
print(grouped_mean)


teamsAvailable = np.empty([7,3], dtype = float)
teamsAvailable
