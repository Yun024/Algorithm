from string import ascii_lowercase
from string import ascii_uppercase
def solution(my_string):
    alphabet = ascii_uppercase + ascii_lowercase 
    return [my_string.count(i) for i in alphabet]