# finds the cube root of a number
# by kinda long division
# algorithm described here:
# http://www.mathpath.org/Algor/cuberoot/algor.cube.root.htm

import sys

number = sys.argv[1]
try:
  precision = int(sys.argv[2])
except IndexError:
  precision = 3
# number = '399849302.8593' # cube root = 736.71375927
# number = 12812904
# 1. split the number on the decimal point
# this will work correctly even with numbers
# entered as .843920 with no leading zero
n_parts = number.split('.')

# 2. split number into groups of three, from units to left
# and from tenths to right
queue = []
pos = n_parts[0]
i = -1
s = ''
while -1 * i < len(pos) + 1:
  s = pos[i] + s
  i -= 1
  if len(s) == 3 or abs(i)-1 == len(pos):
    queue = [s] + queue
    s = ''

if len(n_parts) == 2:
  queue.append('.')
  dec = n_parts[1]
  i = 0
  s = ''
  while i < len(dec):
    s += dec[i]
    i += 1
    if len(s) == 3:
      queue.append(s)
      s = ''
    elif i == len(dec):
      while len(s) < 3:
        s += '0'
      queue.append(s)

root = ''

# 3. take first number in queue, and find the largest
# number whose cube does not exceed it
n = 0
limit = queue.pop(0)
remainder = 0
while n**3 <= float(limit):
  n += 1
root += str(n-1)
remainder = int(limit) - int(root)**3


# 4. apply algorithm to the rest of the numbers
def algorithm(a_list,b):
  a_list = [i for i in a_list if i != '.']
  a1 = int(''.join(str(i) for i in a_list))
  a2 = int(''.join(str(i) for i in a_list + [b]))
  return (30 * a1 * a2 + b**2) * b

while len(queue) > 0:
  digits = queue.pop(0)
  if digits == '.':
    root += digits
    continue
  limit = int(str(remainder) + str(digits))
  n = 0
  while algorithm(list(root),n) <= limit:
    n += 1
  remainder = limit - algorithm(list(root),n-1)
  # remainder = int(''.join([d for d in str(remainder) if d != '.']))
  root += str(n-1)

if remainder > 0 and root.count('.') == 0:
  root += '.'

# 5. If an exact answer is not reached,
# continue by adding zeros
while remainder > 0 and len(root.split('.')[1]) < precision:
  digits = '000'
  limit = int(str(remainder) + str(digits))
  n = 0
  while algorithm(list(root),n) <= limit:
    n += 1
  remainder = limit - algorithm(list(root),n-1)
  root += str(n-1)


print root