"""def greet(name):
   print("Hello : ", name)
  
  
greet("Alice")


def square(x):
    return x * x

result = square(5)
print(result)

def count_even(num):
    count = 0
    for i in range(1, num + 1):
        if i % 2 == 0:
            print(i)
            count += 1
    return count

print(count_even(10))"""



"""def cheak_result(mark):
    if mark >= 40:
        return "pass"
    else:
        return "fail"
    
result = cheak_result(int(input("Enter your marks: ")))
print(result)
"""
# Without keyword argument Order matters nhole korbe naaa like this 
# def introduce(name, age):
#     print("name", name , "age",age)
# introduce(25, "Alice") no !!!!
# introduce( name ="Alice",  age = 25) yes !!!
def add(* numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(add(56666,667677,89098,533447,6657565,675685,6575))

def create_uder(**kwargs):
    print((kwargs))

create_uder(name="Alice", age=30, city="New York")



class bankaccount :
    def __init__(self, name , balance):
        self.name = name
        self._balance = balance

    def deposit(self, amount):
        if amount>0:
            self._balance += amount
            
            
    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount

    def get_balance(self):
        return self._balance
    
acc1 = bankaccount("mana", 1000)
print( "1st" , acc1.get_balance())
acc1.deposit(500000)
print( "after deposit 500000" , acc1.get_balance())
acc1.withdraw(200000)
print( "after withdraw 200000" , acc1.get_balance())


class payment:
    def __init__(self, amount, ):
        self.amount = amount   

    def pay(self): 
        print(f"Payment of {self.amount} has been made.")


class creditcardpayment(payment):
    def pay(self):
        print(f"Payment of {self.amount} has been made using credit card" + "  2% fee!")

class upipayment(payment):
    def pay(self):
        print(f"Payment of {self.amount} has been made using UPI.")

p1 = creditcardpayment(1000)
p1.pay()
p2 = upipayment(500)
p2.pay()

           
   
    



