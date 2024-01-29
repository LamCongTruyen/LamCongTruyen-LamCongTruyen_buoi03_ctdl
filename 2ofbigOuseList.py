array = [1,2,3,4,5]
#def printParis(array):#gọi hàm 

    #for i in array : #bigO la O(n^2), duyệt qua từng phần tử i trong mảng
paris1 = [i for i in array]

      #  for j in array: # bigO la O(n),duyệt qua từng phẩn tử j trong mảng
paris2 = [j for j in array]


print(str(paris1)+","+str(paris2)) #bigO la O(1), in cawjo gái trị i và j
