import math

L = [1,2,3,4,5,6,7,8,]
start = 0
end = len(L) - 1
target = 11

def bin_search(L,start,end,target):
    if(start>end):
        return False
    mid = math.floor((start + end) / 2) # mid here is the index or midpoint of the array, not the actual mid value
    if L[mid] == target:
        return True
    if L[mid] > target:
        return bin_search(L,start, mid - 1, target)
    else:
        return bin_search(L,mid+1, end, target)


print(bin_search(L,start, end, target))