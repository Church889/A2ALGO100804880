#A2
#ALGORITHMS
#Samuel. M. Joseph
#100804880
#Date:07/24/2024



import winsound
#used winsound instead of simpleaudio because it was just easier.


def annoyingSound():
    freq=2000
    dur=10
    winsound.Beep(freq,dur)
    

def mergeSort(arr):
    # If the length of the array is less than or equal to 1, return the array
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    sideLeft = arr[:mid]
    sideRight = arr[mid:]


    sortLeft = mergeSort(sideLeft)
    sortRight = mergeSort(sideRight)

    #mergeing the sored halfs the sorted halves
    return merge(sortLeft, sortRight)

def merge(left, right):
    sortedArray=[]
    i=j=0

    #merge the two halves while maintaining order
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            sortedArray.append(left[i])
            i+=1
        else:
            sortedArray.append(right[j])
            j+=1
        annoyingSound()
     

    while i<len(left):
        sortedArray.append(left[i])
        i+=1
        annoyingSound()

    while j<len(right):
        sortedArray.append(right[j])
        j+=1
        annoyingSound()

    print("STEPS",sortedArray)
    return sortedArray

#ARRAY
array = [11,1,30,2,51,6,29,7,67,15,118,4,89,23]


sortedArray = mergeSort(array)
print("FULLY SORTED:",sortedArray)
