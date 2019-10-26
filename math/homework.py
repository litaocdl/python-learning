###
# Home work for daughter to generate math
###

#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import random

with open('result.txt', 'w') as f1:
 f1.truncate()
 k = 0 
 f1.write("\n=========================================================\n\n\n")
 for i in range(30) :
    k = k + 1
    a = random.randint(50,99)
    b = random.randint(50,99)
    c = random.randint(10,50)
    if a - b > 10 :
       s = '-'
    else :
       s = '+'
    if k % 2 == 0 :
      f1.write('%d + (%d %s %d)  =   \n\n\n'%(c,a,s,b))
    else :
      f1.write('%d + (%d  %s %d) =                '%(c,a,s,b))
 f1.write("\n\n\n=========================================================\n")
