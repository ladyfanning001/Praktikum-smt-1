def IsEmptyLoL(S):
    return S==[]

def IsAtom2(S):
    return type(S) != list

#YG DIPAKE ISATOMNYA
def IsAtom(S):
    return isinstance(S,list) and len(S) == 1 and not isinstance(S[0],list)

def IsList(S):
    return not IsAtom(S)

def konsolol(L,S):
    if not IsEmptyLoL(S):
        return [L]+ S
    else :
        return [L]
    
def KonsiLol(L,S):
    if not IsEmptyLoL(S):
        return S + [L]
    else :
        return [L]
    
def firstlist(S):
    if not IsEmptyLoL:
        return S[0]
    else :
        return []
    
def tailist(S):
    if not IsEmptyLoL(S):
        return S[1:]
    else :
        return []
    
def lastlist(S):
    if not IsEmptyLoL(S):
        return S[-1]
    else :
        return []

def headluist(S):
    if not IsEmptyLoL(S):
        return S[0]
    else :
        return []
    
list1 = [1,2,[5]]
list2 = [[1,2],[3,4]]
    