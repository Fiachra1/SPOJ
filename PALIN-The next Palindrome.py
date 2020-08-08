#A positive integer is called a palindrome if its representation in the decimal system is the same when read from left to right and from right to left. For a given positive integer K of not more than 1000000 digits, write the value of the smallest palindrome larger than K to output. Numbers are always displayed without leading zeros.

#Input
#The first line contains integer t, the number of test cases. Integers K are given in the next t lines.

#Output
#For each K, output the smallest palindrome larger than K.


def check_next_palindrome(num):
    num=str(int(num)+1)
    num_list = list(num)
    reversed_list=list(num)
    reversed_list.reverse()
    if len(num_list)%2==0:
        half=int((len(num_list))/2)
        while True:
            if num_list[0:half]==reversed_list[0:half]:
                print("".join(num_list))
                break
            else:
                new_num=str(int("".join(num_list))+1)
                num_list=list(new_num)
                reversed_list=list(new_num)
                reversed_list.reverse()
                continue
    else:
        half=int((len(num_list)-1)/2)
        while True:
            if num_list[0:half]==reversed_list[0:half]:
                print("".join(num_list))
                break
            else:
                new_num=str(int("".join(num_list))+1)
                num_list=list(new_num)
                reversed_list=list(new_num)
                reversed_list.reverse()
                continue

test_cases = int(input())
for num_cases in range(test_cases):
    init_num = input()
    check_next_palindrome(init_num)
