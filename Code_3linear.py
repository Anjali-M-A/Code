#Script for Linear Sequential Search Algorithm


def LinearSearch(list,key):
    for i in range (len(list)):      #range is i=0 to len(list)
        if key == list[i]:          #key will be compared to the 1st elelment of list
            print("key element is found at index",i)
            return i
    else:
            print("not found")
            


list= [2,3,4,5,6,7]   #len(list) is 5
key =1
print(list)
LinearSearch(list,key)
