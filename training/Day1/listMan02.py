#!/usr/bin/env python3
# sort, sorted
# sort will sort the original list
# sorted will create a copy of the sorted list

l1 = [10, 5, 9, 1, 7, 3, 4, 2, 6, 8, 1, 2, 3, 8, 9]

asc_res = sorted(l1)
print(f"Ascending order :{asc_res}")

desc_res = sorted(l1, reverse=True)
print(f"Descending order :{desc_res}")

l1.sort()
print(f"Ascending order :{l1}")

print("-" * 40)

l2 = [10, 'zebra', 5, 'apple', 9, 'yellow', 1, 'blue', 7, 'queen', 3, 'cream', 4, 'green',
      2, 'orange', 6, 'white', 8, 'dog', 11, 22, 33, 101, 1111, 202, 222, 203, 33, 301, 335]
print(f"l2 :{l2}")

res = sorted(l2, key=ascii)
print(f"after sorting l2 :{res}")

l3 = [90, 'a', 92, 100]
res = sorted(l3, key=ascii)
print(l3)
print(res)

cities = ('vishakapatnam', 'madurai', 'bangalore', 'thiruvananthapuram', 'pune', 'delhi',
          'kanyakumari', 'hyderabad', 'chennai', 'mysore')

print(cities)

res = sorted(cities, key=len)
print(f"Sorted in Ascending :{res}")

months = ('dec', 'mar', 'nov', 'aug', 'feb', 'oct', 'may', 'jul', 'apr', 'jun', 'sep', 'jan')

# sort these months
def srtdMon(mon):
    mnt = ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec')
    return mnt.index(mon)

res = sorted(months, key=srtdMon)
print(months)
print(res)
