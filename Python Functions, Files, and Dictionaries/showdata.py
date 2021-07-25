
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("WeekFive/resulting_data.csv")
fig,ax=plt.subplots()
my_scatter_plot=ax.scatter(df[" Net Score"],df["Number of Retweets"])
plt.show()