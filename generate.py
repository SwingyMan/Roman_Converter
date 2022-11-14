import os
from tabulate import tabulate
import numpy
os.chdir("out")
y =[]
z =[]
for letter in os.listdir():
    x= open(letter,'r',encoding="utf-8").read()
    y.append(x)
os.chdir("..")
os.chdir("in")
for letter in os.listdir():
    x= open(letter,'r').read()
    z.append(x)
y.reverse()
z.reverse()
table =z,y
i=numpy.transpose(table)
headers =("Input","Output")
os.chdir("..")
p = tabulate(i,headers, tablefmt='html')
o = open("raport.html","w",encoding="utf-8")
o.write(p)
o.close()