import math, random, datetime
# Abselote Value
number=-999
numbabs = abs(number)
print(numbabs)

# Round
number1=5.8765
numbrund=round(number1)
print(numbrund)

# Power of
numpo = 3
nupo=pow(numpo, 2)
print(nupo)

# Max & Min
Dijits= 300, 600, 769, 1568, 4596
print(max(Dijits))
print(min(Dijits))

# Add
x=sum(Dijits)
print(x)

# Sqrt
mun=144
y=math.sqrt(mun)
print(y)

# Divide reminder
print(math.remainder(9,2))

# generate random 1-100
random.randint(1,100)

# Date generation
date=datetime.date(2022,4,13)
print(date)
print(date.year)
print(date.month)
print(date.day)

# Time generation
time=datetime.time(15,47,56)
print(time)
print(time.hour)
print(time.minute)
print(time.second)

# today
now=datetime.datetime.today()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

# date or time to string
print(date.strftime('%A %B %Y'))
print(time.strftime('%I %M %S'))
