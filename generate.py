import os
import sys
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
o = open(sys.argv[1],"w",encoding="utf-8")
header = "<h1>Raport wygenerowano o: "+sys.argv[1].strip(".html")+"</h1>"
o.write(header)
o.write(p)
o.close()