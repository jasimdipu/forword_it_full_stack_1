class Solution:

    def cal_sum(self, lst: str) -> int:
        temp = []
        for x in lst:
            if type(x) == int or x.isdigit():
                temp.append(x)
                print(temp)
            if x == "C":
                temp.pop()
            if x == "D":
                temp.append(str(int(temp[-1]) * 2))
            if x == "+":
                temp.append((int(temp[-1])))
        result = sum([int(i) for i in temp if type(i) == int or i.isdigit()])
        return result


