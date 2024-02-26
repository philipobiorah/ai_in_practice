

def truth_table_and():

    truth_table=[]
    for a in [True, False]:
        for b in [True, False]:
            truth_table.append((a,b, a and b))

    return truth_table


print(truth_table_and())


def truth_table_Aimplies():

    truth_table=[]
    for a in [True, False]:
        for b in [True, False]:
            truth_table.append((a,b, not a or b))

    return truth_table


truth_table_Aimplies()



def implies(a, b):
    return (not a) or b

def iff():
    truth_table=[]
    for a in [True, False]:
        for b in [True, False]:
            # A ↔ B is equivalent to (A → B) and (B → A).
            truth_table.append((a, b,  implies(a,b) and implies(b,a)))
    return truth_table

 
print(iff())