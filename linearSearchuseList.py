#import array#khai báo hàm array dùng như 1 thư viện
#myArray1 = array.array('i',[1,2,3,3,5,8,8,8,8,9,10])#khai gán giá trị ban đầu báo kiểu dữ liệu của mảng và 
#def linearSearch(arr,target):#gọi hàm linearSearch với mảng arr và giá trị cần tìm target
#    for i in range(len(arr)):#thực hiện vòng lặp các giá trị trong khoảng giá trị là chiều dài của mảng ar
#        if arr[i] ==  target:#nếu phần tử thứu i của mảng bằng giá trị muốn nhắm đeesn
#            return 1#trả về 1
#        return -1#trả về -1 ngay sau đó nếu điều kiện không thõa
#print(linearSearch(myArray1,2))#in ra màn hình hàm linearSearch với giá trị arr là mảng [1,2,3,4,5] và giá trị cần target là 8

#VIẾT LẠI DÙNG LIST COMPREHENSION

import array#khai báo hàm array dùng như 1 thư viện
arr = array.array('i',[1,2,3,3,5,8,8,8,8,9,10])
target = 8
linearSearch = [ 1 if arr[i] == target else -1 for i in range(len(arr))]
print(linearSearch)
