class TabularArray():

    def __init__(self,A,K):
        self.A = A
        self.K = K


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
        cell = ""
        for i in range(1,self.K+1):
            cell = "-" * width
            cell += "+"
            result += cell
        return result

    def draw(self):
        result = ""
        index = 0
        for i in range(self.number_of_lines()):
            if i % 2 == 0:
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
