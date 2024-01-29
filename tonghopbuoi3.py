                              # TỔNG HỢP LÝ THUYẾT BUỔI 3,CODE LẠI LÍ THUYẾT VÀ GIẢI THÍCH CODE.
                    #    *thầy kiểm tra chỉ cần chép hết tất cả và chạy tới đâu thì bỏ dấu "#" đó là được ạ


                                                     #PYTHON LIST


#integers = [ 1,2 ,3,4]
#print(integers)

#stringlist = ['milk', 'cheese', 'butter']
#print(stringlist)

#mixelist = [1,2,3,4,5,{1.5, 1.6}, {'test'}]
#print(mixelist)

#empty = []
#print(empty)


                                           # TÌM HIỂU VỀ BACKET: [INDEX]


#marketList = [ 'milk' , 'durex' , 'banana']
#print(marketList[1]) #in ra phần tử thứ nhất trong list, bắt đầu từ 0,1,2
#print(marketList[3]) #không có phần tử này trong mảng nên chương trình error


                                          #TÌM HIỂU VỀ: IN OPERATOR


#print('banana' in marketList) #ktra xem có ptu banana trong mảng không nếu có thì in ra true,
#print('socola' in marketList) #không thfi trả về giá trị false false

#print(marketList[-1]) #in ra phần tử thứ -1,-2-,3,-4 nghĩa là phần tử cuối cùng của mảng và in lùi lại đến phần tử đầu tiên 
#print(marketList[-3])

#for i in marketList: 
#    print(i) #cho1 biến i chạy trong cái mảng marketList, và in ra phần tử i mỗi lần lặp

#for i in range(len(marketList)): #cho biến i chạy trong cái khoảng giá trị chiều dài của list
    #marketList[i] = marketList[i]+"+"
#    print(marketList[i]+'+') #in ra phần tử thứ i + dấu '+'
#empty = [1,2] #cho mảng empty
#for i in empty:#chạy i trong mảng empty kiểm tra xem nếu empty rỗng thì không in ra gì
 #   print("i am empty") #nếu có phần tử nào có giá trị thì in ra thông điệp

#myList = [ 'milk','flower','cookie',1,2,3,4,5,6]
#myList[2] = 33 
#myList[1] = 11#chèn giá trị 33 vào phần tử thứ k( k=2)
#myList[-1] = 'end of list' #in giá trị cuối của 1 mảng
#myList[0] = 'firt of list' #in giá trị đầu của 1 mảng
#print(myList) #mức độ phức tạp thuật toán là O(1) 

               
                                 #TÌM HIỂU VỀ HÀM RANDOM:
                              

                                 #TRÒ CHƠI DÂN GIAN: 


#myList2 = [ 'Bầu','Cua','Tôm','Cá','Gà','Nai']
#import random
#random_element1 = random.choice(myList2) #in một phần tử ngẫu nhiên từ mảng
#random_element2 = random.choice(myList2)
#random_element3 = random.choice(myList2)
#print("xúc xắc 1:  ",random_element1)
##random_element = random.choice(myList2) #in một phần tử ngẫu nhiên từ mảng
#print("xúc xắc 2:  ",random_element2)
##random_element = random.choice(myList2) #in một phần tử ngẫu nhiên từ mảng
#print("xúc xắc 3:  ",random_element3)

#myList3 = [ 1, 2, 3, 4, 5, 6]
#random_element4 = random.choice(myList3) 
#random_element5 = random.choice(myList3)
##random_element6 = random.choice(myList3)
#print("xúc xắc 1:  ",random_element4)
#print("xúc xắc 1:  ",random_element5)
#print("xúc xắc 1:  ",random_element6)
#number = [random_element4,random_element5,random_element6 ]
#total = sum(number)
#if total <= 10 :
#    print(f"xỉu : {total}")
#else:
 #   print(f"tài: {total}")
#myList.insert(3,[1,2,3,4]) #lệnh chèn trong ListMethod
#print(myList)

#myList.append(['lenh append']) #lệnh append(thêm) 1 phần tử vào list,nhưng chỉ được thêm ở vị trí cuối cùng
#print(myList)

#newList = ['mở trộng list']#lệnh extend(mở rộng) thêm list bằng cách thêm 1 mảng vào ở cuối list
#myList.extend(newList)
#print(myList)

                    # 3 HÀM TRÊN ĐỀU CÓ MỨC PHỨC TẠP THUẬT TOÁN LÀ O(1)


#print(myList[0:2])
#print(myList[0:4]) #in ra các phần tử từ 0 đến n-1
#print(myList[:4])  #in đến ptu n-1
#print(myList[3:]) #in ra các ptu từ n+1 đến hết
#print(myList[:]) #in tất cả ptu


                           #TÌM HIỂU VỀ 3 LỆNH POP, DELETE, REMOVE


#myList = [ 'milk','flower','cookie',1,2,3,4,5,6]

#myList.pop(1) #đưa phần tử thứ 1 cất vào ngăn xếp, giống như lệnh pop trong assembly
#print(myList)

#del myList[0:2] #xóa 2 phần tử từ 'milk' đến 'flower', ( 0 đến n-1)
#print(myList)
#del myList[0:4] #xóa 3 phần tử tiếp theo từ "cookie" đến "3"
#print(myList)

#myList.remove(1) #xóa đi phần tử vụ thể ví dụ như "1" trong list
#print(myList)


                      #TÌM HIỂU VỀ LỆNH SEARCHING FOR AN ELEMENT IN THE LIST
 

                                       #DÙNG LẠI LIST: myList


#target = 'cookie'  #khai báo phần tử nhắm tới
#if target in myList:  #kiểm tra xem phần tử đó có nằm trong thư viện đã khai báo hay không
 #   print(f"{target} is in the myList") #nếu có in ra thông điệp
#else: #ngược lại thì in ra thông điệp khác
 #   print (f"{target} is not in the myList")

#a = [1,1]
#b = [2,3,7,8,9,'J', 'Q', 'K', 'A']
#c = [4,5,6]
#a = a * 4 # a bằng số phần tử a nhân với 4
#d = b + c #d bằng list b cộng list c
#print(a)
#print(d)
#print(len(b)) #hàm len là hàm tính toán chiều dài của 1 list hoặc mảng
#print(min(c)) #hàm min tìm giá trị nhỏ nhất của list,điều kiện là list là các phấn tử nguyên
##print(max(c)) #hàm tìm giá trị lớn nhất
#print(sum(c)) #hàm tính tổng 
#print(sum(c)/len(c)) #hàm tính trung bình cộng

#total = 0 #khởi tạo giá trị ban đầu 
#count = 0 # khởi tạo biến đếm 
#while(True): #trong khi điều kiện đúng
 #   inp = input("enter a number: ") #biến inp bằng giá trị nhập từ bàn phism
 #   if inp == "done" : break #nếu  inp bằng done thì thoát, gõ done để thoát
 #   value = float(inp) #biến value bằng giá trị và có kiểu giá trị như biến inp
 #   total = total + value #giá trị total bằng giá trị ban đầu + gái trị vừa nhập
  #  count = count + 1 #tăng biến đếm lên 1, nhằm đến số phần tử đã nhập
  #  average = total / count #gtri trung bình bằng tổng các ptu chia cho số phtu
    
#print ("Average:" , average) #in ra màn hình

#a = "Chúc mừng năm mới họcviện PTIT"
#b = list(a) #lệnh list liệt kê(tách riêng) ra các kí tự của mảng a
#print(b) #['C', 'h', 'ú', 'c', ' ', 'm', 'ừ', 'n', 'g', ' ', 'n', 'ă', 'm', ' ', 'm', 'ớ', 'i', ' ', 'h', 'ọ', 'c', ' ', 'v', 'i', 'ệ', 'n', ' ', 'P', 'T', 'I', 'T']

#c = a.split() #lệnh split liệt kê từng phần tử trong mảng cách nhau 1 dấu space
#print(c)


                            #TÌM HIỂU VỀ LIST COMPREHENSION


#prev_list = [1,2,3] #khai báo list
#new_list =[] #khai báo 1 list rỗng
#for i in prev_list: #cho biến i chạy trong list
 #   multiply_2 = i * 2 # biến multi bằng
 #   new_list.append(multiply_2) #thêm 1 phtu vào trong cuối new_List giá trị bằng i *2
#print(new_list) #in ra [2, 4, 6]

#Ta có cách viết rút gọn sau nhằm giảm độ phức tạp thuật toán xuống mức tối thiểu:
#prev_list2 = [4,5,6]
#new_list2 = [ i * 2 for i in prev_list2] #newlist bằng i*2 trong đó biến i chạy trong prevlist
#print(new_list2) #in ra [8,10,12]
#new_list3 = [ i + 2 for i in prev_list2] #ở đây ta cx có thể dùng các phép toán học 
#print(new_list3)
#new_list4 = [ i - 1 for i in prev_list]
#print(new_list4) 

                                       #VÍ DỤ KHÁC

#language = "python is better C for learn CTDL"
#new_list = [letter for letter in language] #newlisst bằng kí tự chạy lần lượt từ kí tự đầu đến cuối list language
#print(new_list)
                      #đây là cách viết nếu ko dùng list comprehension
#new_list = []
#for i in language:
#    letter = i
#    new_list.append(letter) #lệnh append là lệnh thêm 1 phần tử cuối vào 1 list hoặc mảng
#print(new_list)


                #TÌM HIỂU VỀ PYTHON SEQUENCES( CÁC CHUỖI CƠ BẢN TRONG PYTHON )

                     #LIST:

#prev_list = [-1,-2,-3,4,5,6]
#new_list = [ number for number in  prev_list if number < 0]#list mới thì bằng number khi cho number chạy trong mảng prevlist nếu biến number nhận giá trị <0
#print(new_list) #ở đây kiểu dữ liệu prevlist nhận được hoặc đc nhập phải là integer chứ k đc chứa float

#ví dụ tìm nhiệt độ trung bình và số ngày có nhiệt độ lớn hơn nhiệt độ trung bình
#numDay= int(input("how many day's temprature?")) #nhập vào số ngày cần tính nhiệt độ trung bình
#total = 0 #khởi tạo giá trị biến đếm
#temp = []#khởi tạo mảng số ngày
#for i in range(numDay): #khởi tạo từ vị trí thứ 0 chạy trong khoảng giá trị của cái biến numDay từ 0 đến 4
#    nextDay = int(input("Day" + str(i+1) + "high temp: ")) #nhập dữ liệu cho hàm nextday
 #   temp.append(nextDay) #đưa giá trị hàm nextday và cuối list temp đã khai báo rỗng ở trên
#    total += temp[i] #tăng biến đếm tổng số ngày total = total(0) + temp[i] - i chạy từ 1 đến giá trị lớn nhât của range numday

#avg = round(total/numDay, 2) #biến giá trị trung bình bằng tổng số ngày chia cho số ngày và hàm round là hàm sử dụng để làm tròn 2 chữ số thập phân
#print("\nAverage = " + str(avg)) #in ra

#above = 0 #số ngày lớn hơn nhiệt độ trung bình là 0
#for i in temp: #cho biến i chạy trong khoảng giá trị biến temp
 #   if i>avg: #nếu i lớn hơn giá trị trung bình
#        above +=1 #biến đếm số ngày lớn hơn nhiệt độ trung bình cộng thêm 1
#print(str(above)+ "day's above average" ) #in ra


                                     #DICTIONARY

#my_dict  = dict() #tạo 1 từ điển trống
#print(my_dict)        
#my_dict2 = {}
#print(my_dict2)
#eng_sp = [('one','uno'),( 'two' , 'dos' ),( 'three' , 'tres')] # tạo một từ điển có cách danh sách các bộ tuple có tên eng_sp,trong đó mỗi tuple có hai phần tử đại diện cho hai tiếng
#eng_sp3 = dict(eng_sp) #ác tuple được xem như các cặp khóa-giá trị, với phần tử đầu tiên của mỗi tuple là khóa và phần tử thứ hai là giá trị.
#print(eng_sp3)


                          #CODE LẠI CÁC BÀI BUỔI 2 BẰNG LIST HAY LIST Comprehension





















