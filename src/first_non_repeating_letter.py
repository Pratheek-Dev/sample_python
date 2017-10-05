# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 20:30:08 2017

@author: Pratheek Devaraj

"""

def first_non_repeating_letter(str):
    """
    This function returns the first non repeating letter in a string. This method does not use Counter function.
    
    Input: string 
    Output: string of first non repeating letter. If all repeating, return empty string

    """
    #Convert string to lower-case string
    str_lower = str.lower()
    
    #create a list with character and index for each character in string
    #enumerate returns a tuple for each letter format 
    list_str_lower = enumerate(str_lower)
    
    #traverse through dictionary 
    for i, letter in list_str_lower:
        if str_lower.count(letter) == 1:
            return str[i]
        
    #return empty string if all are repeating letters
    return ""
      

import unittest
# Note: the class must be called Test
class Test(unittest.TestCase):
  def test_should_handle_simple_tests(self):
    self.assertEqual(first_non_repeating_letter("a"), "a")
    self.assertEqual(first_non_repeating_letter("stress"), "t")
    self.assertEqual(first_non_repeating_letter("moonmen"), "e")
    
unittest.main()