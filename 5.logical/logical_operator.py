
def AND(cond1,cond2):
    if cond1 and cond2:
        return True
    else:
        return False
print(AND(True,False))

def OR(cond1,cond2,cond3):
    if cond1 or cond2 or cond3:
        return True
    else:
        return False
print(OR(False,False, True))

def NOT(cond1):
    if not cond1:
        return True
print(NOT(False))