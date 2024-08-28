#!/usr/bin/env python3

def return_evens(num_list):
#   evens= list()
#   for n in num_list:
#     if n % 2 == 0:
#       evens.append(n)
#   else: 
#     print(evens)
#   return evens 
    evens = [n for n in num_list if n % 2 ==0]
    return evens

def make_exclamation(sentence_list):
    add_exclamation  = [n + "!" for n in sentence_list ]
    return add_exclamation 
        

# new_list = [optional_operation(item) for item in old_list if optional_condition == True]