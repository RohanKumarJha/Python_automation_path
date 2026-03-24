# Print “Hello, World!”
# print("Hello, world!")

# Swap two numbers without a temporary variable.
# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# print("The first number is :",num1, "and the second number is :",num2)
# print("After swapping")
# num1 = num1 + num2
# num2 = num1 - num2
# num1 = num1 - num2
# print("The first number is :",num1, "and the second number is :",num2)

# Print all even numbers from 1 to 50.
# for i in range(1, 51) :
#     if(i % 2 == 0) :
#         print(i)

# Print all odd numbers from 1 to 50.
# for i in range(1, 51) :
#     if(i % 2 != 0) :
#         print(i)

# Print numbers 1–100, replacing multiples of 3 with “Fizz” and 5 with “Buzz”.
# for i in range(1, 100) :
#     if(i % 3 == 0) :
#         print("Fizz")
#     elif(i % 5 == 0) :
#         print("Buzz")
#     else :
#         print(i)

# Sum all numbers from 1 to N
# n = int(input("Enter the value of n :"))
# sum = 0
# for i in range(1,n+1) :
#     sum += i
# print(sum)

# Find the factorial of a number.
# num = int(input("Enter the number : "))
# fact = 1
# for i in range(1,num+1) :
#     fact *= i
# print(fact)

# Find the sum of digits of a number.
# num = int(input("Enter the number : "))
# sum = 0
# while(num > 0) :
#     digit = num % 10
#     sum += digit
#     num //= 10
# print(sum)

# Reverse a number.
# num = int(input("Enter a number, you want to reverse : "))
# rev_num = 0
# while(num != 0) :
#     digit = num % 10
#     rev_num = rev_num * 10 + digit
#     num //= 10
# print(rev_num)

# Check if a number is a palindrome.
# num = int(input("Enter a number : "))
# actual_num = num
# rev_num = 0
# while(num != 0) :
#     digit = num % 10
#     rev_num = rev_num * 10 + digit
#     num //= 10
# if actual_num == rev_num:
#     print(actual_num, "is palindrome")
# else:
#     print(actual_num, "is not palindrome")

# Print all prime numbers from 1 to 100.
# for i in range(2,101) :
#     flag = True
#     for j in range(2,i) :
#         if(i % j == 0) :
#             flag = False
#             break
#     if flag :
#         print(i)

# Check if a number is prime.
# num = int(input("Enter the number : "))
# flag = True
# for i in range(2,num) :
#     if(num % i == 0) :
#         flag = False
#         break
# if flag :
#     print(num,"is a prime number")
# else :
#     print(num,"is not a prime number")

# Find the GCD of two numbers.
# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# min_num = min(num1, num2)
# while min_num > 0 :
#     if(num1 % min_num == 0) :
#         if(num2 % min_num == 0) :
#             print(min_num)
#             break
#     min_num -= 1

# Find the LCM of two numbers.
# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# max_num = max(num1, num2)
# while True :
#     if(max_num % num1 == 0) :
#         if(max_num % num2 == 0) :
#             print(max_num)
#             break
#     max_num += 1

# Generate Fibonacci series up to N terms.
# n = int(input("Enter the value of n : "))
# first_num = 0
# second_num = 1
# for i in range(0,n) :
#     if i == 0 :
#         print(first_num)
#     elif i == 1 :
#         print(second_num)
#     else :
#         sum = first_num + second_num
#         first_num = second_num
#         second_num = sum
#         print(sum)

# Print the multiplication table of a number.
# num = int(input("Enter the number in which table you want to print : "))
# for i in range(1,11) :
#     print(num,"*",i,"=",num*i)

# Count the number of digits in a number.
# num = int(input("Enter the number : "))
# digits = 0
# while num > 0 :
#     digits += 1
#     num //= 10
# print(digits)

# Check if a year is a leap year
# num = int(input("Enter the year: "))
# if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
#     print(num, "is a leap year")
# else:
#     print(num, "is not a leap year")

# Find the sum of all even numbers in a list.
# number_list = [1,2,3,4,5,6,7,8,9,10]
# sum = 0
# for i in range(0,len(number_list)) :
#     if number_list[i] % 2 == 0 :
#         sum += number_list[i]
# print(sum)

# Find the sum of all odd numbers in a list.
# number_list = [1,2,3,4,5,6,7,8,9,10]
# sum = 0
# for i in range(0,len(number_list)) :
#     if number_list[i] % 2 != 0 :
#         sum += number_list[i]
# print(sum)

# Find the maximum number in a list.
# number_list = [1,2,3,4,5,6,7,8,9,10]
# max_num = float('-inf')
# for i in range(0,len(number_list)) :
#     max_num = max(max_num,number_list[i])
# print(max_num)

# Find the minimum number in a list.
# number_list = [1,2,3,4,5,6,7,8,9,10]
# min_num = float('inf')
# for i in range(0,len(number_list)) :
#     min_num = min(min_num,number_list[i])
# print(min_num)

# Reverse a list without using built-in functions.
# number_list = [1,2,3,4,5,6,7,8,9,10]
# new_list = []
# for i in range(len(number_list)-1, -1, -1):
#     new_list.append(number_list[i])
# print(new_list)

# Print a pattern: triangle of stars.
# for i in range(1,6) :
#     for j in range(1,i+1) :
#         print("*",end="")
#     print()

# Print a square pattern of stars.
# for i in range(1,6) :
#     for j in range(1,6) :
#         if(i==1 or i==5) :
#             print("*",end="")
#         elif(j==1 or j==5) :
#             print("*",end="")
#         else :
#             print(" ",end="")
#     print()

# Print a pyramid pattern of stars.
# col = 5
# for i in range(1, col + 1):
#     for j in range(col - i):
#         print(" ", end="")
#     for j in range(2 * i - 1):
#         print("*", end="")
#     print()

# Find the sum of all elements in a list.
# number_list = [1,2,3,4,5,6,7,8,9,10]
# sum = 0
# for i in range(0,len(number_list)) :
#     sum += number_list[i]
# print(sum)

# Check if a list contains duplicates.
# number_list = [1,2,3,4,5,6,7,8,9,1]
# flag = True
# for i in range(0,len(number_list)) :
#     for j in range(0,len(number_list)) :
#         if(number_list[i] == number_list[j] and i != j) :
#             flag = False
#             break
# if flag == False :
#     print("Duplicate exist")


# Remove duplicates from a list.
# number_list = [1,2,3,4,5,6,7,8,9,1]
# new_list = []
# for i in range(len(number_list)):
#     if number_list[i] not in new_list:
#         new_list.append(number_list[i])
# print(new_list)

# Merge two lists into a single sorted list.
# list1 = [1, 3, 5, 7]
# list2 = [2, 4, 6, 8]
# merged = list1 + list2
# merged.sort()
# print(merged)