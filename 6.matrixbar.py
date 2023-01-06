import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter

plt.style.use("fivethirtyeight")

data = pd.read_csv("sample product.csv")

customers = data['Customer']
products = data['Product']

customer_counter = Counter()

# myIter = ['x','y','z','x','x','y','z','z','z','z']
# print(Counter(myIter))

# print(customers)
# print(products)

for cus in customers:
#     print(cus)
    customer_counter.update((cus))
print(customer_counter)

most_cus = []
rate = []

for i in customer_counter.most_common(10):
    most_cus.append(i[0])
    rate.append(i[1])
print(most_cus,rate)
most_cus.reverse()
rate.reverse()
plt.barh(most_cus,rate)

plt.title("Customers")

plt.xlabel("Rate")
plt.ylabel("Customer Initial Name")
plt.tight_layout()
plt.show()
