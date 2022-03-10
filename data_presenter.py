import matplotlib.pyplot as plt
import numpy as np

open_file = open("CupcakeInvoices.csv")
# Loop through all the data and print each row.
# for line in open_file:
#     print(line)
# Loop through all the data and print the type of cupcakes purchased.
# for line in open_file:
#     print(list[2])
# Loop through all the data and print out the total for each invoice (Note: this data is not provided by the csv, you will need to calculate it. Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. Research how to do this.).
# for line in open_file:
#     list = line.split(",")
#     print(int(list[3]) * float(list[4]))
# Loop through all the data, and print out the total for all invoices combined.
# invoiceTotal = 0.0
# for line in open_file:
#     list = line.split(",")
#     sum = int(list[3]) * round(float(list[4]), 2)
#     invoiceTotal += sum
# print(invoiceTotal)

# PART 3
vanillaTotal = 0
chocolateTotal = 0
strawberryTotal = 0
for line in open_file:
    list = line.split(",")
    if list[2] == "Vanilla":
        vanillaTotal += int(list[3]) * round(float(list[4]), 2)
    elif list[2] == "Chocolate":
        chocolateTotal += int(list[3]) * round(float(list[4]), 2)
    elif list[2] == "Strawberry":
        strawberryTotal += int(list[3]) * round(float(list[4]), 2)

types = np.array(["Vanilla", "Chocolate", "Strawberry"])
totals = np.array([vanillaTotal, chocolateTotal, strawberryTotal])

plt.bar(types, totals)
plt.show()
open_file.close()