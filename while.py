"""i = 1

while i < 10:
    print(i)
    i += 1"""
"""i = 1 
while i < 20:
    if i % 2 != 0:
        print(i)
    i += 1"""
"""i = 5

while i >= 1:
    print(i)
    i -= 1
 num    """
"""num = 34963969379359389856894653895639639698346598689969
count = 0  
while num > 0:
    num //= 10
    count += 1  
print("The number of digits is:", count)"""
# Reverse digits of a number
"""age = [1, 2, 3, 4, 5]
print(age)
total = sum(age)
print(total)"""
"""age = [1, 2, 3, 4, 5]
total = 0 
for i in age:
    total += i
print(total)
i =+ 1
"""
"""numbers = [1234, 1221, 987, 234, 12345, 5838, 5832, 153, 18, 112233, 122334, 4312]
target = 5832  # The number we want to find

for i in numbers:    
    print("Checking:", i)  
    if i == target:
        print("Target found:", i)
        break"""
     
import copy

a = (1, 2, 3, 4, 5 )
b = copy.deepcopy(a)
                            # This is very important because it is aks commonly in interviews
b[2].append(6)
print(a)
print(b)