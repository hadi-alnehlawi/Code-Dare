class TabularArray():

    def __init__(self,A,K):
        self.A = A
        self.K = K
        self.separator_cell = ("-" * self.width_of_cell()) + "+"


    def number_of_digit(self,number):
        count=0
        while(number>0):
            count = count + 1
            number = number // 10
        return count

    def width_of_cell(self):
        max_A = max(self.A)
        return self.number_of_digit(max_A)

    def number_of_rows(self):
        if len(self.A) % self.K == 0:
            return  len(self.A) // self.K
        else:
            return (len(self.A) // self.K) + 1

    def number_of_lines(self):
        return (2 * self.number_of_rows() ) + 1


    def convert_cell_to_list(self,number):
        width = self.width_of_cell()
        result = [ " " for _ in range(width)]
        x = number
        str_numbers = []
        while(x>0):
            str_numbers.append(x % 10)
            x = x // 10
        revert_numbers = [x for x in str_numbers if x != ""]
        revert_numbers = revert_numbers[::-1]
        sub_start = len(result) - self.number_of_digit(number)
        sub_end = len(result)
        result[sub_start:sub_end] = revert_numbers
        result.append("|")
        result = [str(x) for x in result]
        return result


    def draw_number(self):
        result = "|"
        width = self.width_of_cell()
        cell = ""
        for i in range(1,self.K+1):
            cell = "x" * width
            cell += "|"
            result += cell
        return result

    def draw_separator(self):
        result = "+"
        width = self.width_of_cell()
        for i in range(1,self.K+1):
            result += self.separator_cell
        return result

    def draw(self):
        result = ""
        index = 0
        number_of_line = self.number_of_lines()
        number_cell_in_last_line = len(self.A) % self.K
        for i in range(number_of_line):
            if ( (self.K > len(self.A)) and (i == 0) ) or ((i == (number_of_line -1)) and (number_cell_in_last_line != 0)):
               result += "+" + number_cell_in_last_line *  self.separator_cell
            elif (i % 2 == 0) and (i != (number_of_line -1)):
                result += self.draw_separator()
            elif ((i % 2 == 0) and (i == (number_of_line -1))):
                result += self.draw_separator()
            else:
                result +=  "|"
                for j in range(self.K):
                    if index < len(self.A):
                        number_list = self.convert_cell_to_list(self.A[index])
                        item = "".join(number_list)
                        result += item
                        index += 1
                    else:
                        break
            result += "\n"
        return result


if __name__ == "__main__":    
    A = []
    for i in range(1,15):
        A.append(i)
    print("A = ",A)
    for i in range(1,(len(A)-1)):
        print("K = ",i)
        print(TabularArray(A,i).draw())
