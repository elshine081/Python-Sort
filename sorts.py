_lst = [10,29,58,4,100,19,6,224,1200,87,33,33,1,63,1256]

class Sort:
    def bubbleSort(arrayList):
        _count = len(arrayList)-1
        
        for x in range (_count+1):            
            for y in range (_count-x):
                if(arrayList[y]>arrayList[y+1]):
                    arrayList[y], arrayList[y+1]=arrayList[y+1], arrayList[y]
        return arrayList
    
    def quickSort(arrayList):
        _count = len(arrayList)-1

        lower = list()
        higher = list()
        same = list()

        if (_count>0):
            center = arrayList[0]

            for x in arrayList:
                if x>center:higher.append(x)
                elif x<center:lower.append(x)
                else: same.append(x)
            
            finalSortedList = Sort.quickSort(lower) + same + Sort.quickSort(higher)

            return finalSortedList
        else: #only one item left
            return arrayList
    
    def mergeSort(arrayList):
        count = len(arrayList)-1

        if (count>0): #contains more than 1 item and has to be devided
            center = (count+1)//2 #//? it can be odd or even

            firstSec, secondSec = arrayList[:center], arrayList[center:] #divide to 2 lists

            Sort.mergeSort(firstSec)
            Sort.mergeSort(secondSec)

            mainIndex, firstIndex, secIndex = 0,0,0
            firstLen, secLen = len(firstSec)-1, len(secondSec)-1

            while (firstIndex<=firstLen and secIndex<=secLen):
                if (firstSec[firstIndex]>secondSec[secIndex]):
                    arrayList[mainIndex]=firstSec[firstIndex]
                    firstIndex+=1
                else:
                    arrayList[mainIndex]=secondSec[secIndex]
                    secIndex+=1
                mainIndex+=1
            
            while(firstIndex<=firstLen):
                arrayList[mainIndex]=firstSec[firstIndex]
                mainIndex+=1
                firstIndex+=1
            
            while(secIndex<=secLen):
                arrayList[mainIndex]=secondSec[secIndex]
                mainIndex+=1
                secIndex+=1

        return arrayList[::-1]
        
#Usage : 
    #Quick Sort A List:
print ("quick sorted list : ",Sort.quickSort(_lst))
    #Bubble Sort A List:
print ("bubble sorted list : ",Sort.bubbleSort(_lst))
    #Merge Sort A List
print ("merge sorted list : ",Sort.mergeSort(_lst))