# coding=gbk

import string
import matplotlib.pyplot as plt  
import numpy as np
 
if __name__ == '__main__':    
    file = open(E:machine_learningdatasetshousing_datahousing_data_ages.txt, 'r')
    linesList = file.readlines()
#     print(linesList)
    linesList = [line.strip().split(,) for line in linesList]
    file.close()    
    print(linesList:)
    print(linesList)
#     years = [string.atof(x[0]) for x in linesList]
    years = [x[0] for x in linesList]
    print(years)
    price = [x[1] for x in linesList]
    print(price)
    plt.plot(years, price, 'b*')#,label=$cos(x^2)$)
    plt.plot(years, price, 'r')
    plt.xlabel(years(+2000))
    plt.ylabel(housing average price(*2000 yuan))
    plt.ylim(0, 15)
    plt.title('line_regression & gradient decrease')
    plt.legend()
    plt.show()