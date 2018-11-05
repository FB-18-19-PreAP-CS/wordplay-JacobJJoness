import re
#def read_file():
#    with open('word.txt')as file:
#        count_the = 0
#        for line in file:
#            for word in line.strip().split():
#                    count_the += 1
#        print(count_the)
        
        
def twenty_O_mo():
    with open('words.txt') as file:
        for line in file:
            for word in line.strip().split():
                if len(word) >=20:
                    print(word)
                    
def no_e():
    num = 0
    noe=0
    with open('words.txt') as file:
        for line in file:
            for word in line.strip().split():
                num+=1
                if not has_no_e(word):
                    noe+=1
    c = ((noe/num)*100)
                    
    print(f'{c} % of the words do not have e.')
    

                    
def has_no_e(word):
    '''this finds words with out the letter e
    >>> has_no_e('taco')
    True
    >>> has_no_e('tortilla')
    True
    >>> has_no_e('jones')
    False
    
    
    '''
    if 'e' not in word:
        return True
    else:
        return False
            
        
def avoid(forbidden,word):
    '''
    >>> avoid('abc','abcd')
    False
    
    >>> avoid('abc','jacob')
    False
    
    >>> avoid('abc','logn')
    True
    '''
    for letter in word:
        if letter in forbidden:
            return False
    return True
        
def avoid_count():
    forbidden_let = input('Enter list of letters')
    count_avoid = 0
    with open('words.txt') as file:
        for line in file:
            for word in line.strip().split():
                if avoid(forbidden_let, word):
                        count_avoid +=1
    print(count_avoid)
                        
                        
def uses_only(letters, words):
     '''
    >>> uses_only('abc','abcd')
    False
    
    >>> uses_only('abc','acb')
    False
    
    >>> uses_only('abc','logn')
    True
    '''
    for letter in word:
        if letters.lower() not in word.lower():
            return False
        return True
    
    
def how_many_uses():
    count = 0
    letter_lst = input('Enter 5 letters')
    with open('words.txt') as file:
        for line in file:
            for word in line.strip().split():
                if uses_only(letter_lst,word):
                    count+=1
    print(count)
                   
                
                
                
    
        
        
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    how_many_uses()