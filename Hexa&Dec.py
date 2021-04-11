# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 21:11:28 2021

@author: Raza_Jutt
"""

def hexaToDec(hexval):
    length = len(hexval)
    base = 1
    dec_val = 0
    for i in range(length - 1, -1, -1):
        if hexval[i] >= '0' and hexval[i] <= '9':
            dec_val += (ord(hexval[i]) - 48) * base
            base = base * 16
        elif hexval[i] >= 'A' and hexval[i] <= 'F':
            dec_val += (ord(hexval[i]) - 55) * base
            base = base * 16
    return dec_val

def decToHexa(n):
    hexaDeciNum = ['0'] * 100
    i = 0
    s=""
    while(n != 0):
        temp = 0
        temp = n % 16
        if(temp < 10):
            hexaDeciNum[i] = chr(temp + 48)
            i = i + 1
        else:
            hexaDeciNum[i] = chr(temp + 55)
            i = i + 1
        n = int(n / 16)
    j = i - 1
    while(j >= 0):
        s = s+(hexaDeciNum[j])
        j = j - 1
    return s
