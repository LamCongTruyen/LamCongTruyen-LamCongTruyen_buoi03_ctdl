
#def powerOf2(n):
#    if n<1:
#        return 0 #O(1)
#    elif n == 1:#O(1
#        print(1)#O(1)
#        return 1#O(1)
#    else:
#        prev = powerOf2(int(n/2))
#        curr = prev * 2#O(1)
#        print(curr)#O(1)
#        return curr#O(1)
#n = 50
#powerOf2(n) 

#VIẾT LẠI DÙNG LIST COMPREHENSION
n = 50
prev = int(n/2)
result_list = [2**i for i in range(prev)]
print(result_list)


    
