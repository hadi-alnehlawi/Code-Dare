def number_of_digit(number):
    count=0
    while(number>0):
        count = count + 1
        number = number // 10
    return count

def width_of_cell(A):
    max_A = max(A)
    return number_of_digit(max_A)


def number_of_rows(A,K):
    if len(A) % K == 0:
        return  len(A) // K
    else:
        return (len(A) // K) + 1


def convert_cell_to_list(A,number):
    width = width_of_cell(A)
    print(width)
    result = [ "" for _ in range(width)]
    x = number
    str_numbers = []
    while(x>0):
        str_numbers.append(x % 10)
        x = x // 10
    revert_numbers = [x for x in str_numbers if x != ""]
    revert_numbers = revert_numbers[::-1]
    sub_start = len(result) - number_of_digit(number)
    sub_end = len(result)
    result[sub_start:sub_end] = revert_numbers
    return result



A = [2,289,33,29,900280,3,22,4,100,9,8]

print(convert_cell_to_list(A,280))
