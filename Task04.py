# -*- coding: utf-8 -*-
"""
Spyder Editor

"""


# M = L[i(1+i)n] / [(1+i)n-1]
# M = monthly payment
# L = Loan amount
# i = interest rate (for an interest rate of 5%, i = 0.05)
# n = number of payments


M =L =I = N = loanduration = 0 

L = input('How much loan you want?\n')
I = input('Interest rate on the loan?\n')
loanduration = input('In How much Time return back the loan?\n')
#Convert the strings into floating numbers so we can use them in the formula
loanduration = float(loanduration)
L = float(L)
I = float(I)
#Since payments are once per month, number of payments is number of years for the loan
N = loanduration*12
#calculate the monthly payment based on the formula
M = L * I * (1+ I) * N / ((1 + I) * N -1)

