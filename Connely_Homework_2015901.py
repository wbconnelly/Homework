# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 22:19:11 2015

@author: William
"""

# read in the Chipotle data
import csv
chipotle = open("chipotle.tsv")
with open("chipotle.tsv", mode = "rU") as chipotle_r:
    file_nested_list = [row for row in csv.reader(chipotle_r, delimiter = '\t')]
    
# seperate into header and data
header = file_nested_list[0]
data = file_nested_list[1:]

qty_list =[]
price_list = []
i = 0
for row in data:
    x = float(data[i][4].strip("$"))
    y = int(data[i][1])
    price_list.append(x)
    qty_list.append(y)
    i = i +1


total_qty = sum(qty_list)
order_tot_price = sum(price_list)

# average price excluding the quantity column sum
average_order_price = order_tot_price/len(price_list)
        # $7.46

# average price including the quantity column sum
avg_ord_pr = order_tot_price/total_qty
        #6.94


# make a list of unique soft drinks
z = 0
soda_list = []
soda = "canned"
for row in data:
    if soda in data[z][2].lower():
        if data[z][3] not in soda_list:
            soda_list.append(data[z][3])
    z = z +1

# Soda List is: 
# ['[Sprite]',
# '[Dr. Pepper]',
# '[Mountain Dew]',
# '[Diet Dr. Pepper]',
# '[Coca Cola]',
# '[Diet Coke]',
# '[Coke]',
# '[Lemonade]',
# '[Nestea]']


# Calculate the average number of toppings per burrito
q = 0
burrito_list = []
burrito = "burrito"
for row in data:
    if burrito in data[q][2].lower():
        burrito_list.append(float(len(data[q][3].split(','))))
    q = q +1    

avg_toppings = sum(burrito_list)/len(burrito_list)
# avg_toppings = 5.395

# Create a dictionary where the keys are the Chip orders and the 
# values are the number of orders

chips_orders = []
c = 0
for row in data:
    if "chips" in data[c][2].lower():
        chips_orders.append(data[c][2])
    c = c +1

from collections import Counter
chips_total = Counter(chips_orders)
chips_total.keys()
chips_total.values()
    # chips_total = Counter({'Chips and Guacamole': 479, 'Chips': 211, 
    #'Chips and Fresh Tomato Salsa': 110, 'Side of Chips': 101, 
    #'Chips and Tomatillo Red Chili Salsa': 48, 'Chips and Tomatillo Green 
    #Chili Salsa': 43, 'Chips and Tomatillo-Green Chili Salsa': 31, 
    #'Chips and Roasted Chili Corn Salsa': 22, 'Chips and Tomatillo-Red 
    #Chili Salsa': 20, 'Chips and Roasted Chili-Corn Salsa': 18, 
    #'Chips and Mild Fresh Tomato Salsa': 1})





"""
data[2].split('\t')

chip = [row for row in csv.reader(chipotle, delimiter='\t')]
chip[12][4]"""