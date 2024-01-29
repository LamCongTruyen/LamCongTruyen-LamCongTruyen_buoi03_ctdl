#def printUnordefredParis(arrayA, arrayB):
#   for i in range(len(arrayA)):
#      for j in range(len(arrayB)):
#         for k in range(0,10):
#            print(str(arrayA[i]) + "," + str(arrayB[j]))
#arrayA = [1,2,3,4,5]
#arrayB = [6,7,8,9,10]
#printUnordefredParis(arrayA, arrayB)

 #VIẾT LẠI DÙNG LIST COMPREHENSION

arrayA = [1,2,3,4,5]
arrayB = [6,7,8,9,10]
unordered_pairs = [(arrayA[i], arrayB[j]) for i in range(len(arrayA)) for j in range(len(arrayB)) for k in range(10)]
for pair in unordered_pairs:
    print(f"{pair[0]}, {pair[1]}")
#Vòng lặp đầu tiên for i in range(len(arrayA)) duyệt qua từng phần tử i trong arrayA.
#Vòng lặp thứ hai for j in range(len(arrayB)) duyệt qua từng phần tử j trong arrayB.
#Vòng lặp thứ ba for k in range(10) tạo ra 10 cặp cho mỗi cặp (arrayA[i], arrayB[j]). Tuy nhiên, giá trị k không được sử dụng trong quá trình tạo cặp
