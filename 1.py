def multiple (x,y=10):
    print (x*y)
    return x*y
a = multiple(4)
print(a)




def check_numders(x,y):
    if x+y<100:
        return "100 kishi"
    else:
        return "100 den ulken "
print(check_numders(50,51)) 



def find_max(list1):
    max_number = list1[0]
    for i in list1:
        if i > max_number:
            max_number = i
    return max_number

print(find_max([1,94,7,28,3])) 