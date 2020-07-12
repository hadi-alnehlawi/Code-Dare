
class Equi():
    def __init__(self,A):
        self.A = A

    def calculate(self,index,diection):
        # if ((i == 0) or (i == (len(self.A)-1) and (sum(self.A) == 0)
        if diection == "right":
            right = [ x for x in self.A[index+1:] ]
            return sum(right)
        else:
            left = [ x for x in self.A[0:index]]
            return sum(left)
