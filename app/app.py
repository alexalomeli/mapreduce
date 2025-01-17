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

#Exercise 2: Change the reducer to calculate the total number (count) of purchases for each category

#!/usr/bin/env python

import sys

count = 0
previous_category = None

for line in sys.stdin:
    category, _ = line.strip().split("\t")

    if previous_category != None and previous_category != category:
        sys.stdout.write("{0}\t{1}\n".format(previous_category, count))
        count = 0

    count += 1
    previous_category = category

sys.stdout.write("{0}\t{1}\n".format(previous_category, count))

#Equivalent SQL Command

#SELECT category, COUNT(*) AS purchase_count
#FROM minipurchases
#GROUP BY category;


#Exercise 3: Change the mapper to raise an error when there are not six elements in the tuple

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 6:
        raise ValueError("Tuple does not have six elements")
    date, time, item, category, sales, payment = data
    sys.stdout.write("{0}\t{1}\n".format(category, sales))

#Equivalent SQL Command

#N/A (This exercise does not have an SQL equivalent since it's about error handling)

#Exercise 4: Change the mapper to calculate the sum only for the categories "Computers", "Cameras", and "Video Games"

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    date, time, item, category, sales, payment = data
    if category in ["Computers", "Cameras", "Video Games"]:
        sys.stdout.write("{0}\t{1}\n".format(category, sales))

#Equivalent SQL Command

#SELECT category, SUM(sales) AS total_sales
#FROM minipurchases
#WHERE category IN ('Computers', 'Cameras', 'Video Games')
#GROUP BY category;

#Exercise 5: Change the reducer to show only categories that have a total count of more than 114 purchases


import sys

for line in sys.stdin:
    category, _ = line.strip().split("\t")
    if int(count) > 114:
        sys.stdout.write("{0}\n".format(category))

#Equivalent SQL Command

#SELECT category
#FROM (
    #SELECT category, COUNT(*) AS purchase_count
    #FROM minipurchases
    #GROUP BY category
#) subquery
#WHERE purchase_count > 114;

#Exercise 6: Change the reducer to calculate the average sales per category

import sys

total_sales = 0
count = 0
previous_category = None

for line in sys.stdin:
    category, sales = line.strip().split("\t")

    if previous_category != None