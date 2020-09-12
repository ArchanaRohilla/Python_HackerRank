#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Storing a function in a module
#File: pizza.py
def make_pizza(size, *toppings):
    """Make a pizza."""
    print("\nMaking a " + size + " pizza.")
    print("Toppings:")
    for topping in toppings:
        print("- " + topping)

