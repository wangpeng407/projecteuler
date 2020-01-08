#!/usr/bin/python
# -*- coding: utf-8 -*-
from functools import reduce
from math import sqrt
import sys


'''
problem 6 Sum square difference
'''

def square_sum(nums):
    return (reduce(lambda x,y:x+y, nums))**2

def sum_square(nums):
    return reduce(lambda x,y:x+y**2, nums)

# print(square_sum(range(1,101)) - sum_square(range(1,101)))

'''
problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.
What is the 10 001st prime number?
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
                return 0
                break
            else:
                res.append(1)
    if 0 in res:
        return 0
    else:
        return 1
def largest_prime_factor(maxl = 100):
    i = 1
    prime_list = []
    while(1):
        i += 1
        if isprime(i):
            prime_list.append(i)
        if len(prime_list) == maxl:
            return(prime_list[-1])
            break
# print(largest_prime_factor(maxl=10001))

'''
problem 8 Largest product in a series
'''

str_num = '''
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450'''

str_num_series = "".join(str_num.strip().split("\n"))

def num_multies(num_str):
    num_series = [int(i) for i in list(num_str)]
    return reduce(lambda x,y:x*y, num_series)

def max_product(str_word, word_len = 13):
    res = [num_multies(str_word[i:i+word_len]) for i in range(len(str_word)) if i+4 <= len(str_word)]
    return max(res)

# print(max_product(str_num_series, word_len=13))

'''
problem 9 Special Pythagorean triplet
'''
for i in range(1,1000):
    for j in range(1, 1000):
        if j <= i:
            continue
        c = sqrt(i**2 + j**2)
        s = i + j + c
        if c / int(c) == 1 and s == 1000:
            print('{} {} {} {}'.format(i,j,c,i*j*c))
            break


'''
problem 10 Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

def sum_prime(maxl=100):
    return sum(filter(isprime, range(2,maxl)))

print(sum_prime(2000000))
