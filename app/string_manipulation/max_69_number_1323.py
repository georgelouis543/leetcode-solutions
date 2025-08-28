class Solution:
    def maximum69Number(self, num: int) -> int:
        max_num = num
        num_list = [i for i in str(num)]

        print(num_list)
        print("".join(num_list))

        i = len(num_list) - 1

        while i >= 0:
            temp = str(num_list[i])

            if temp == "6":
                num_list[i] = "9"
                max_num = max(int("".join(num_list)), max_num)

            if temp == "9":
                num_list[i] = "6"
                max_num = max(int("".join(num_list)), max_num)

            num_list[i] = temp
            i -= 1

        print(max_num)
        return max_num