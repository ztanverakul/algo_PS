import matplotlib as mpl 
mpl.use("Agg")
import matplotlib.pyplot as plt
import math

def P(d):
  d = d/2
  return (d)

def LN(d):
  d = (2 * math.log(d))
  return (d)


num_drinks = [5, 10, 15, 20]
list1 = []
list2 = []

for d in num_drinks:
  list2.append(LN(d))
print()
for d in num_drinks:
  list1.append(P(d))

plt.plot([5, 10, 15, 20], [4, 10, 4, 8], label='p')
plt.plot([5, 10, 15, 20], list1, label='d/2')
plt.plot([5, 10, 15, 20], list2, label='2ln(d)')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)

#plt.xticks(list1, num_drinks)
#plt.xticks(list2, num_drinks)
plt.axis([5, 20, 0, 10])
plt.ylabel('Number of patrons')
plt.xlabel('Number of drinks')
plt.show()
plt.savefig('graph.png')  
