import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import math

#n/4
def N1():
  list = []
  for i in range (1, 51):
    list.append(i/4)
  return (list)

def log2n(n):
  return math.log(n, 2)

#log2(n)
def N2():
  list = []
  for i in range (1, 51):
    list.append(log2n(i))
  return (list)

first = N1()
second = N2()

plt.plot(first, label='n/4')
plt.plot(second, label='log2(n)')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)

plt.axis([1, 50, 0, 20])
plt.ylabel('Run Times')
plt.xlabel('N')

plt.show()
plt.savefig('graph.png')
