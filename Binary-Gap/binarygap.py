'''
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
'''


def solution(N):
    i = 0
    binary_N = bin(N)[2:]
    restult_set = []
    breaker = False
    while i < len(binary_N):
        if binary_N[i] == '1':
            count = 0
            j = i + 1
            while j < len(binary_N):
                if (binary_N[j] == '0') and (j != len(binary_N) - 1 ):
                    count = count + 1
                    j = j + 1
                elif (binary_N[j] == '0') and (j == len(binary_N) - 1 ):
                    breaker = True
                    break
                elif (binary_N[j] == '1') and (j != len(binary_N) - 1 ):
                    restult_set.append(count)
                    i = j
                    break
                else:  #(A[j] == '1') and (j == len(N) - 1 )
                    restult_set.append(count)
                    breaker = True
                    break

        if breaker:
            break

    if not restult_set:
        return 0
    else:
        return sorted(restult_set)[-1]
