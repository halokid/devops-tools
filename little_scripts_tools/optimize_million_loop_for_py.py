# -*- coding: utf-8 -*-
"""
列表生成

生成器  generator

可迭代对象  iterable

迭代器     iterator

"""


'''
# 列表生成器
list4 = [2*n +1 for n in range(3, 11)]


list3 = [n for n in range(3, 11)]


# 出一个指定的数字列表中值大于20的元素
L = [3, 7, 11, 14, 19, 33, 26, 57, 99]

list5 = []

for x in L:
  if x < 20:
    list5.append(x)


# 使用列表生成式
list6 = [x for x in L if x < 20]
'''

import time
import sys

time_start = time.time()

g1 = [x for x in range(50000000)]

time_end = time.time()
print u"列表生成式返回结果花费时间:  %s" % (time_end - time_start)
print u"列表生成式返回结果占用内存大小:  %s" % sys.getsizeof(g1) 



# 返回一个生成器
'''
def my_range(start, end):
  for x in range(start, end):
    yield x


g2 = my_range(0, 50000000)
'''

time_start = time.time()

g2 = (n for n in range(0, 50000000))

time_end = time.time()
print u"生成器返回结果花费时间:  %s" % (time_end - time_start)
print u"列表生成式返回结果占用内存大小:  %s" % sys.getsizeof(g2) 


i = 0
for k in g2:
  print k
  i += 1
  if i > 10: break

























