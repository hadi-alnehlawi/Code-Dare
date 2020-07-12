def solution(A,K):
    if  K == len(A):
        return A
    else:
        B = [ None for _ in A]
        index = len(A)-K
        B[0:index] = A[K-1:]
        B[K:] = A[0:index]
        return B
