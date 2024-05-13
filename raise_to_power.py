# Write a function that takes a base and an exponent as arguments and returns the base raised to the power of the exponent.
def raisepower(bas, exp):
    result = 1
    for i in range(exp):
        result *=bas
    return result

bas = int(input("Enter the Base Number: "))
exp = int(input("Enter the Exponent: "))
print(raisepower(bas, exp))

#easy way
def raisepowerv2(ba, ex):
    return ba**ex

ba = int(input("Enter the Base Number: "))
ex = int(input("Enter the Exponent: "))
print(raisepowerv2(ba, ex))