
#def printUnorderedParis(arrayA, arrayB):
#    for i in range(len(arrayA)):
 #       for j in range(len(arrayB)):
 #           if arrayA[i] < arrayB[j]:
 #               print(str(arrayA[i])+ "," + str(arrayB[j]))
#arrayA = [1,2,3,4,5]
##arrayB = [6,7,8,9,10]
#printUnorderedParis(arrayA, arrayB)

#VIẾT LẠI DÙNG LIST COMPREHENSION


arrayA = [1, 2, 3, 4, 5]
arrayB = [6, 7, 8, 9, 10]
unordered_pairs = [(a, b) for a in arrayA for b in arrayB if a < b]
for pair in unordered_pairs:
    print(f"{pair[0]} , {pair[1]}")





