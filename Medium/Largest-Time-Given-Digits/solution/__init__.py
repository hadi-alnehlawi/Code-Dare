class Solution:

    def largestTimeFromDigits(self, arr):
        self.first_digits = []
        self.third_digits = []
        self.fourth_digits = []
        for number in arr:
            self.set_digits(number)

        res = [None, None, None, None]
        if len(self.first_digits) < 2:
            return ""
        elif (not self.third_digits) and (len(self.first_digits) == 2):
            return ""
        elif (len(self.third_digits) == 1) and (len(self.first_digits) == 2):
            res = sorted(self.first_digits, reverse=True)
            res.append(self.third_digits[0])
            res.append(self.fourth_digits[0])
        elif len(self.first_digits) >= 2:
            res = sorted(self.first_digits, reverse=True)
            remaining = self.third_digits + self.fourth_digits
            res = res + sorted(remaining, reverse=True)
        else:
            return ""
        return res

    def set_digits(self, number):
        if number in range(0, 3):
            self.first_digits.append(number)
        elif number in range(3, 6):
            self.third_digits.append(number)
        else:
            self.fourth_digits.append(number)
