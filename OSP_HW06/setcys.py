def  set1():
    list1 = list(map(int,input("input the 1th list:").split()))
    list2 = list(map(int,input("input the 2nd list:").split()))
    set1 = set(list1)
    set2 = set(list2)
    union = set(set1|set2)
    intersection = set(set1&set2)
    unionl = list(union)
    intersectionl = list(intersection)
    unionl.sort()
    intersectionl.sort()
    print("union: ",unionl)
    print("intersection:",intersectionl)

