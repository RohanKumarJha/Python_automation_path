def fact(num) :
    result = 1
    for i in range(1,num+1) :
        result *= i
    return result

def fact_using_recur(num) :
    if num == 1 :
        return 1
    return num * fact_using_recur(num-1)

def fibonacci(n) :
    first_num = 0
    second_num = 1
    for i in range(n) :
        if i == 0 :
            print(first_num, end = " ")
        elif i == 1 :
            print(second_num, end = " ")
        else :
            sum = first_num + second_num
            print(sum, end = " ")
            first_num = second_num
            second_num = sum

def fibonacci_using_recursion(n) :
    if n == 0 :
        return 0
    if n == 1 :
        return 1
    return fibonacci_using_recursion(n-1) + fibonacci_using_recursion(n-2)

def sum_of_digits(n) :
    sum_of_digits = 0
    while n > 0 :
        sum_of_digits += (n % 10)
        n //= 10
    return sum_of_digits

def sum_of_digits_using_recursion(n) :
    if n == 0 :
        return 0
    digit = n % 10
    n //= 10
    return digit + sum_of_digits_using_recursion(n)

def gcd_of_two_numbers(num1, num2) :
    min_num = min(num1,num2)
    while True :
        if num1 % min_num == 0 and num2 % min_num == 0 :
            return min_num
        min_num -= 1

def lcm_of_two_numbers(num1, num2) :
    max_num = max(num1,num2)
    while True :
        if max_num % num1 == 0 and max_num % num2 == 0 :
            return max_num
        max_num += 1

def rev_str(str) :
    new_str = ""
    for ch in str :
        new_str = ch + new_str
    return new_str

def count_number_of_vowel(str) :
    vowels = "aeiou"
    count = 0
    for ch in str :
        if ch in vowels :
            count += 1
    return count

# Write a function to find factorial of a number.
# print(fact(6))

# Write a recursive function to find factorial.
# print(fact_using_recur(5))

# Write a function to generate Fibonacci series up to N.
# fibonacci(5)

# Write a recursive function for Fibonacci series.
# for i in range(5) :
#     print(fibonacci_using_recursion(i), end = " ")

# Write a function to sum digits of a number.
# print("Sum digit of a number : ",sum_of_digits(1234))

# Write a recursive function to sum digits of a number.
# print("Sum digit of a number : ",sum_of_digits_using_recursion(1234))

# Write a function to find GCD of two numbers.
# print(gcd_of_two_numbers(21,35))

# Write a function to find LCM of two numbers.
# print(lcm_of_two_numbers(70,35))

# Write a function to reverse a string.
# print(rev_str("Rohan Kumar jha"))

# Write a function to check palindrome string.
# str = "Aba"
# rev_str = rev_str(str)
# if str.lower() == rev_str.lower() :
#     print("String is palindrome")

# Write a function to count vowels in a string.
str = "Rohan Kumar Jha"
print("The number of vowels is :",count_number_of_vowel(str))