import matplotlib.pyplot as plt
import csv
import numpy as np


"""
DEFINITIONS:
delimiter: seperator
"""


"""
Using CSV
x,y=[],[]

with open("example.txt","r") as f:
    plots = csv.reader(f,delimiter=',')
    #plots was the whole list seperated by line
    #each row is seperated by ","
    for row in plots:
        #when they are loaded they usually in strings so we have to convert them
        x.append(int(row[0]))
        y.append(int(row[1]))


plt.plot(x,y,label="Loaded from example.txt")
"""

"""
LOADINIG USING NUMPY
x,y=np.loadtxt("example.txt",delimiter=",",unpack="True")
plt.plot(x,y,label="Loaded from example.txt")
"""

def graph_stock(stock):

    stock_price_url = 'http://'
    
    plt.show()
graph_stock("TSLA")
