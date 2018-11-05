Домашнее задание к третьей лекции Козлов Марк
def v(x):
    return(round(x))


x = float(input("x="))

print(v(x))





def lucky(x):
    l_number = list(str(x))
    result = False
    if len(l_number) == 6:
        summ_1 = int(l_number[0])+int(l_number[1])+int(l_number[2])
        summ_2 = int(l_number[3])+int(l_number[4])+int(l_number[5])
        if summ_1 == summ_2:
            result = True
    return result





