start=int(input("Enter starting value"))
end=int(input("Enter ending value"))
even_sum = 0
odd_sum = 0
for value in range(start, end):
    if value % 2 == 0:
        even_sum = even_sum + value
    else:
        odd_sum = odd_sum + value

print("Sum of even numbers is =", even_sum)
print("Sum of odd numbers is =", odd_sum)
