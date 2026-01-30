import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('JAIPUR_1.CSV')
print(data.head())

plt.figure()
plt.plot(data["date"].head(15), data["rainfall"].head(15))
plt.xlabel("Date")
plt.ylabel("Rainfall")
plt.title("Rainfall overtime")
plt.show()