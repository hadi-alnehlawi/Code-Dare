class Solution:
    def __init__(self):
        pass

    def repeated_strings(self, s: str) -> bool:
        leng_str = len(s)
        res = []
        final = []
        for i in range(2,leng_str):
            if leng_str % i == 0 :
                res.append(i)
            else:
                continue
        if len(res) == 0: 
            print("\nNo repeated strings")
            return False
        else:
            for num in res:
                start = 0
                end = num
                dividers = leng_str // num
                myList = []
                for i in range(dividers):
                    myList.append(s[start:end])
                    start = start + num
                    end = end + num
                    i = i + num
                is_contained = all(x==myList[0] for x in myList)
                if is_contained:
                    final.append(myList)
                    print(myList)
                else:
                    continue
            return True if len(final) > 0 else False

if __name__ == "__main__":
    s = "abcabcabcabc"
    solution = Solution()
    print(solution.repeated_strings(s))