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
        return None
            
        
def avoid(forbidden,word):
    for letter in word:
        if letter in forbidden:
            return False
        else:
            return True
                
                
                
    
        
        
        
if __name__ == '__main__':
    avoid('abcde','lever')