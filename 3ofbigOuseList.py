array = [1,2,3,4,5]
#def printUnorderedParis(array):
range1 = [ i for i in len(array)]
range2 = [ i+1 for i in len(array)]
  # for i in range(0,len(array)):
UnorderedParis1 = [ a for a in range1]

        #for j in range(i+1,len(array)):
UnorderedParis2 = [ j for j in range2] 
           
print(UnorderedParis1 + "," + UnorderedParis2)

