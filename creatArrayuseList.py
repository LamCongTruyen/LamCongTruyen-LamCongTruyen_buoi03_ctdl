#from array import *
#arr1 = array('i', [1,2,3,4,5,6,7,8,9,10,11,12,13])#khai báo 1 mảng arr với kiểu dữ liệu 'i' và gán giá trị ban đầu 
#def accessElement(array, index):#tạo hàm truy cập phần tử, với mảng array và index là vị trí của mảng cần xét
#    if index > len(array):#kiểm tra xem có thành phần nào trong mảng nằm ngoài vị trí cẩn xét của mảng hay không
#        print('there is not any element in this index')#in ra không có phần tử nào
#    else:
#        print(array[index])#nếu có thì in ra giá trị của thành phần đó
#accessElement(arr1, 8)#gọi hàm truy cập phần tử với mảng arr và vị trí của mảng cần xét,nếu mảng có giá trị tại thứ tự là 8 thì in ra màn hình giá trị 9


#VIẾT LẠI SỬ DỤNG LIST COMPEHENSION

from array import *
arr1 = array('i', [1,2,3,4,5,6,7,8,9,10,11,12,13])
index = 14
accessElement =[ arr1[index] if index < len(arr1) else 'there is not any element in this index' ]
print(accessElement)