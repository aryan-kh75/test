import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("marks.csv")
print(df)
plt.scatter(df["name"],df["marks"])
plt.show()
plt.bar(df["name"], df["marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Students marks Graph")
plt.show()