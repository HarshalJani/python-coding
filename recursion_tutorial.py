#Problem 1
# You are given "n" as argument which will be an integer.  
# Write a recursive function to print integers from 0 to n.

def print_number(n):
    
    def recursive_print(inter_state, end_state):
        
        print(inter_state)
        
        if inter_state == end_state:
            return
        
        recursive_print(inter_state + 1, end_state)

    recursive_print(0, n)

print_number(2)


#Problem 2
# Given a input "n" which represents a integer. Write a program that has all the combinations of 0, 1
# For example n = 2 
# Output = ["00", "01", "10", "11"]
#[000,001,010,100]

def combination(n):
    output = []
    def recursive_comb(inter_state, inter_res, n): #placetoadd, #totaldigits
        nonlocal output
        if inter_state == n:
            output.append(inter_res)
            # print(inter_res)
            return 

        new_inter_res_zero = inter_res + '0'
        new_inter_res_one = inter_res + '1'
        
        recursive_comb(inter_state + 1, new_inter_res_zero, n)    
        recursive_comb(inter_state + 1, new_inter_res_one, n)    
    
        
    recursive_comb(0, "", n)
    return output
res = combination(2)    
print(res)


#Problem 3
#Given the number N (N >=0), print its factorial.
#Examples:
#Input: 5
#Output: 120
#Explanation: 5! = 5 * 4 * 3 * 2 * 1 = 120

def factorial(n):
    fact = n
    if n == 0:
        return 1
    
    def recursive_fact(inter_state, end_state):
        nonlocal fact
        if inter_state == end_state:
            # print(fact)
            return
        
        fact = fact * (inter_state-1)
        recursive_fact(inter_state-1, 1)
        
    recursive_fact(n, 1)
    return fact
print(factorial(5))


#Problem 4
# Given a number n, print n-th Fibonacci Number. 
# The Fibonacci numbers are the numbers in the following integer sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..


def fibonacci(end_state):
    if end_state <= 1:
        return end_state
    else:
        return fibonacci(end_state - 1) + fibonacci(end_state - 2)

print(fibonacci(9))

#Alternative

def fibonacci(n):
    fib = 0
    def recursive_fib(inter_state, end_state):
        nonlocal fib
        
        if inter_state <= end_state:
            return inter_state
        
        return recursive_fib(inter_state - 1, end_state) + recursive_fib(inter_state - 2, end_state)
        
    return recursive_fib(n, 1)

print(fibonacci(9))






