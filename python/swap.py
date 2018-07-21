def solution(A):
    # write your code in Python 3.6
    idx1 = -1
    idx2 = 0
    
    for i in range(1,len(A)):
        if A[i-1] >= A[i]:
            #print A[i-1] , "-", A[i]
            if idx1 == -1:
                idx1 = i-1
                idx2 = i
            else:
                idx2 = i
    swap(A, idx1, idx2)
    
    if idx1 == -1 or (idx2+1<len(A) and A[idx2]<A[idx2+1]):
        return True
    else:
        return False


def swap(A, i, j):
    
    right = A[i]
    
    A[i] = A[j]
    A[j] = right
    

A=[10, 20, 40, 30, 50, 60]
print (solution(A))
A =[1,3,5,3,4]
print (solution(A))
A =[1,3,5]
print (solution(A))

  