class LogicalCoding:
    def __init__(self):
        pass

    def prime_numbers(self, num):
        prime_num = []
        if num <= 0:
            return "We can not find prime number's in -ve range"
        else:
            if num >= 2:
                for i in range(1, num + 1):
                    count = 0
                    for j in range(1, i + 1):
                        if i % j == 0:
                            count += 1
                    if count == 2:
                        prime_num.append(i)
            return prime_num

    def fibonacci_logic(self, num):
        fin1 = 0
        fin2 = 1
        numbers = []
        if num <= 0:
            return "There is no -ve fibonacci series"
        else:
            numbers.append(fin1)
            numbers.append(fin2)
            for i in range(num + 1):
                fin1, fin2 = fin2, fin1 + fin2
                numbers.append(fin2)
            return numbers

    def palindrome_num(self,num):
        if num < 0:
            return "We can not calculate palindrome for -ve numbers"
        else:
            num1 = num
            dummy = 0
            while num > 0:
                dummy = dummy * 10 + num % 10
                num = int(num/10)
            if num1 == dummy:
                return "Given Number %d is palindrome " % num1
            else:
                return "Given Number %d is not a palindrome " % num1

    def palindrome_str(self, strng):
        strng1 = strng.lower()
        dummy = ''
        while len(strng) > 0:
            dummy = dummy + strng[-1]
            strng = strng[:-1]
        if strng1 == dummy.lower():
            return "Given String %s is palindrome " % strng1
        else:
            return "Given String %s is not a palindrome " % strng1





if __name__ == '__main__':
    logic = LogicalCoding()
    # print(logic.prime_numbers(10))
    # print(logic.fibonacci_logic(10))
    # print(logic.palindrome_num(23232))
    print(logic.palindrome_str("Wow"))
