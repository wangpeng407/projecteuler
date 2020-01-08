#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''
from __future__ import  division

def division_TorF(num, div):
    temp_div = [int(i) for i in div]
    min_val = sorted([num % i for i in temp_div])[0]
    if min_val == 0:
        return True
    else:
        return False

def search_numbers_multiples(start = 1, end = 100, *multiples):
    return filter(lambda x: division_TorF(x, multiples), range(start, end))

# print((search_numbers_multiples(1, 1000, 3, 5)))


'''
problem 2
Each new term in the Fibonacci sequence is generated by adding 
the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed 
four million (4,000,000), find the sum of the even-valued terms.
'''

def fibonacci_series(max = 100):
    a, b = 1, 2
    res = [a, b]
    if max <= a:
        return res[0]
    elif max <= b:
        return res
    while(1):
        a,b = b, a+b
        if b > max:
            return res
        else:
            res.append(b)

# print((filter(lambda x: x % 2 ==0, (fibonacci_series(max = 4e10)))))

'''
problem 3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''
from math import sqrt, floor, ceil
def isprime(n):
    res = []
    if n == 2 or n == 3:
        return 1
    else:
        for i in range(2, int(ceil(sqrt(n)))+1):
            if n % i == 0:
                res.append(0)
            else:
                res.append(1)
    if 0 in res:
        return 0
    else:
        return 1

def find_prime_factor(num):
    res = []
    temp_num = num
    for i in range(2,int(ceil(sqrt(num)))+1):
        if isprime(i) and num % i == 0:
            res.append(i)
            temp_num /= i
            if temp_num == 1:
                pass
                # print("Max prime factor is {}".format(i))
        else:
            continue
    return res

# print(find_prime_factor(600851475143))


'''
problem 4
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_palindromic_number(num):
    str_num = str(num)
    rev_str_num = str_num[::-1]
    if len(str_num) % 2 != 0:
        return False
    p1 = str_num[0:int(len(str_num)/2)]
    p2 = rev_str_num[0:int(len(str_num)/2)]
    if p1 == p2:
        return True
    else:
        return False

num_ij = {}
for i in range(100, 1000):
    for j in range(100, 1000):
        if is_palindromic_number(i * j):
            num_ij[i*j] = '{} * {}'.format(i, j)
            # print("{} = {} * {}".format(i * j, i, j))

# print(sorted(num_ij.keys(), reverse=True)[0])


'''
problem 5
2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of 
the numbers from 1 to 20?
'''
from functools import reduce

def search_divisors(num, temp=[]):
    assert num > 1, "First argument must > 1"
    if isprime(num):
        temp.extend([1, num])
        return temp
    else:
        prime_divisors = find_prime_factor(num)
        temp.append(prime_divisors[0])
        next_divs = int(num / prime_divisors[0])
        if isprime(next_divs):
            temp.append(next_divs)
            return temp
        else:
            return search_divisors(next_divs, temp)

def least_common_multiples(aval, bval):
    a_div = search_divisors(aval, temp=[])
    b_div = search_divisors(bval, temp=[])
    a_div_dict = dict([(i, a_div.count(i)) for i in set(a_div)])
    b_div_dict = dict([(j, b_div.count(j)) for j in set(b_div)])
    all_key = set(a_div + b_div)
    temp = {}
    for k in all_key:
        a_div_dict[k] = a_div_dict[k] if(k in a_div_dict) else 0
        b_div_dict[k] = b_div_dict[k] if(k in b_div_dict) else 0
        temp[k] = a_div_dict[k] if (a_div_dict[k] > b_div_dict[k]) else b_div_dict[k]
    res = []
    for k,v in temp.items():
        for i in range(1,v+1):
            res.append(k)
    multiples = reduce(lambda x,y:y*x, res)
    return multiples

print(reduce(lambda x,y:least_common_multiples(x,y), range(2,20)))
