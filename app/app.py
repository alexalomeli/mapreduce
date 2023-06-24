#Exercise 1: Change the mapper to calculate the sum for each category (not payment type)

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    date, time, item, category, sales, payment = data
    sys.stdout.write("{0}\t{1}\n".format(category, sales))

#Equivalent SQL

#SELECT category, SUM(sales) AS total_sales
#FROM minipurchases
#GROUP BY category;

