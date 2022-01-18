"""
Given n as input, print the numbers that divide n and the numbers that do not divide n. Note that the numbers to be checked are from 1 to n.
Input-> n=9
Output-> 
Divide: 1#3#9# 
Not Divide: 2#4#5#6#7#8#
"""

n = 9
st1 = ""
st2 = ""
for i in range(1,n+1):
  if(n%i==0):
    st1 = st1 + str(i) + "#"
  else:
    st2 = st2 + str(i) + "#"
print(f"Divide:{st1}")
print(f"Not Divide:{st2}")
