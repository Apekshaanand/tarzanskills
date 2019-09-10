number 1=int(input("Enter the input :"))
number 2=int(input("Enter the input :"))
def add(number 1 ,number 2):
    sum = number 1+number 2
    return sum
def sub(number 1,number 2):
    sub = number 1-number 2
    return sub
def multiplication(number 1,number 2):
    product = number 1*number 2
    return product
def division(number 1,number 2):
    division = number 1/number 2
    return division

operation= input("")

while True:
    if operation=='add':
        print(add())
    elif operation=='sub':
        print(sub())
    elif operation=='multiplication':
        print(multiply())
    elif operation=='division':
        print(division())
        break






