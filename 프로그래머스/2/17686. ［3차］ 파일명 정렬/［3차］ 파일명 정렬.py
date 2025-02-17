import re

def split_file_name(file_name):
    file_name = file_name.upper()
    match = re.match(r'([A-Z\-. ]+)(\d{1,5})(.*)',file_name)
    head, number, tail = match.groups()
    return (head,number)
    

def solution(files): 
    sfn =  [(split_file_name(i), i) for i in files]
    ans =  sorted(sfn, key= lambda x: (x[0][0],int(x[0][1])))
    return [i[1] for i in ans]
