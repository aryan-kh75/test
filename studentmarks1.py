import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Studentmarks.csv")

print(df)

# plt.pie(df["Total marks"], labels = df["Name"], autopct='%1.1f%%')
# plt.title("Total marks distribution among students")
# plt.show()
plt.bar(df["Name"], df["Total marks"], df["Average marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Students marks Graph")
plt.show()