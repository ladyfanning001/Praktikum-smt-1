def IsEmptyLoL(S):
    return S == []

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
      
def loltolist(LoL):
  return [LoL]
    
def IsPrima(n,i=2) :
  if n < 2 :
    return False
  elif n == 2 :
    return True
  elif n % i == 0 :
    return False
  elif i*i > n :
    return True
  else :
    return IsPrima(n,i+1)

def AddPrima(LoL):
    if AddPrima(loltolist(LoL)) == []:
        return 0
    elif not firstlist(AddPrima(loltolist(LoL))) == IsPrima(LoL):
        return AddPrima(tailist(loltolist(LoL)))
    else :
        return firstlist(loltolist(LoL))+AddPrima(tailist(loltolist(LoL)))
    
print(AddPrima([1,[5,2,3],10,9,[7],[3,3]]))