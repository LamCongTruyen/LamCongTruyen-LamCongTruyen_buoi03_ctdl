#def reserse(array):
#    for i in range(0, int(len(array)/2)): #bigO la O(N)-lap qua cac phan tu cua mang Vòng lặp này chỉ cần chạy đến giữa mảng vì khi đảo ngược, các phần tử sẽ được hoán đổi đôi một
#        other = len(array) - i - 1  #bigO laa O(1)-truy cap vao 1 phan tu cu the,biến other lưu phần tử nằm đối xứng với vị trí giữa của mảng
#        temp = array[i]#bigO laa O(1) Lưu giữ giá trị tạm thời của phần tử tại vị trí i
#        array[i] = array[other]#bigO laa O(1) Gán giá trị của phần tử tại vị trí i bằng giá trị của phần tử ở vị trí đối diện other
#        array[other] = temp#bigO laa O(1) Gán giá trị của phần tử tại vị trí other bằng giá trị tạm thời đã lưu giữ ở bước 3.
#    print(array)#bigO laa O(1)
#array = [1,2,3,4,5]
#reserse(array)

#VIẾT LẠI DÙNG list slicing

list = [1, 2, 3, 4, 5]
reversed_list = list[::-1] #::-1 được sử dụng để tạo một slice của mảng với bước -1, tức là đảo ngược mảng.
print(reversed_list)



