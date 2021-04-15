import numpy as np
import pandas as pd
import math
import scipy.stats as scp
import matplotlib as plt


data = pd.read_csv("Staff.csv", sep = ";") 

data.boxplot(column = "Actual BD teams", by = "Shift")

cleaned_data = data.drop(columns = ["DayOfMonth", "Year"])
grouped_mean = cleaned_data.groupby(["Shift", "Month"]).mean()
cleaned_data.plot(x = "Month", y = "Actual BD teams", kind = "bar")
grouped_mean