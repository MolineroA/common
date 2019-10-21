import math


def common_between_two_lists(a, b):
    '''
    Take two lists, say for example these two:
    a =[1,1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b =[1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    and write a program that returns a list that contains only
    the elements that are common between the lists (without duplicates).
    '''
    return [i for i in set(a) if i in b]


def quantity_a_in_str(my_str):
    '''
    Return the number of times that the letter “a”
    appears anywhere in the given string
    Given string is “I am a good developer.I am also a writer”
    and output should be 5
    '''
    return my_str.count('a')


def power_of_three(num):
    '''
    Write a Python program to check if a given positive integer
    is a power of three
    Input : 9
    Output : True
    '''
    return num == math.pow(3, round(math.log(num) / math.log(3)))


def add_until_a_single_digit(num):
    '''
    Write a Python program to add the digits of a positive integer
    repeatedly until the result has a single digit.
    Input : 48
    Output : 3
    '''
    while len(str(num)) > 1:
        num = sum([int(i) for i in list(str(num))])
    return num


def push_zeros_to_the_end(in_list):
    '''
    Write a Python program to push all zeros to the end of a list.
    Input : [0,2,3,4,6,7,10]
    Output : [2, 3, 4, 6, 7, 10, 0]
    '''
    return list(filter(lambda x: x != 0, in_list)) + list(filter(
        lambda x: x == 0, in_list))


def check_arithmetic_progression(in_list):
    '''
    Write a Python program to check a sequence of numbers is
    an arithmetic progression or not.
    Input : [5, 7, 9, 11]
    Output : True
    '''
    step = in_list[1] - in_list[0]
    for i in range(len(in_list) - 1):
        if not (in_list[i + 1] - in_list[i] == step):
            return False
        return True


def number_not_occur_twice(in_list):
    '''
    Write a Python program to find the number in a list
    that doesn't occur twice.
    Input : [5, 3, 4, 3, 4]
    Output : 5
    '''
    return [i for i in in_list if in_list.count(i) < 2][0]


def find_a_missing_number(in_list):
    '''
    Write a Python program to find a missing number from a list.
    Input : [1,2,3,4,6,7,8]
    Output : 5
    '''
    return [i for i in range(in_list[0], in_list[-1] + 1)
            if i not in in_list]


def count_elements_until_tuple(in_list):
    '''
    Write a Python program to count the elements in a list
    until an element is a tuple.
    Sample Test Cases:
    Input: [1,2,3,(1,2),3]
    Output: 3
    '''
    count_element = 0
    for i in in_list:
        if isinstance(i, tuple):
            break
        count_element += 1
    return count_element


def string_reverse(my_str: str) -> str:
    '''
    Write a program that will take the str parameter being passed
    and return the string in reversed order. For example:
    if the input string is "Hello World and Coders"
    then your program should return the string sredoC dna dlroW olleH.
    '''
    return my_str[::-1]


def convert_number_to_hours(min):
    '''
    Write a program that will take the num parameter being passed
    and return the number of hours and minutes the parameter converts to
    (ie. if num = 63 then the output should be 1:3).
    Separate the number of hours and minutes with a colon.
    '''
    return '{} : {}'.format(min // 60, min % 60)


def largest_word(in_string):
    '''
    Write a program that will take the parameter being passed
    and return the largest word in the string.
    If there are two or more words that are the same length,
    return the first word from the string with that length. Ignore punctuation.
    Sample Test Cases:
    Input:"fun&!! time"
    Output:time
    Input:"I love dogs"
    Output:love
    '''
    for char in in_string:
        if not char.isalnum():
            in_string = in_string.replace(char, ' ')
    return max(in_string.split(), key=len)


def words_in_backwards_order(in_string: str):
    '''
    Write a program (using functions!) that asks the user for a long string
    containing multiple words. Print back to the user the same string,
    except with the words in backwards order.
    For example:
    Input: My name is Michele
    Output: Michele is name My
    '''
    return str(' '.join(in_string.split()[::-1]))


def fibonacci(num):
    '''
    Write a program that asks the user how many Fibonacci
    numbers to generate and then generates them.
    Take this opportunity to think about how you can use functions.
    Make sure to ask the user to enter the number
    of numbers in the sequence to generate.
    '''
    num = int(input('Input number:'))

    def fib(num):
        a, b = 0, 1
        while True:
            yield b + a
            a, b = b + a, a

    fib_num = fib(num)
    return [next(fib_num) for i in range(num)]


def even_nums(a):
    '''
    Let’s say I give you a list saved in a variable:
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
    Write one line of Python that takes this list a and makes a new list
    that has only the even elements of this list in it.
    '''
    return [i for i in a if i % 2 == 0]


def add_up_numbers(num):
    '''
    Write a program that will add up all the numbers from 1 to input number.
    For example:
    if the input is 4 then your program should return 10
    because 1 + 2 + 3 + 4 = 10.
    '''
    num = int(input('Input number:'))
    return sum(list(range(1, num + 1)))


def factorial(num):
    '''
    Write a program that will take the parameter being passed and
    return the factorial of it.
    For example:
    if num = 4, then your program should return (4 * 3 * 2 * 1) = 24.
    '''
    return math.factorial(num)


def replace_letters_in_str(my_str):
    '''
    Write a program that will take the str parameter being passed
    and modify it using the following algorithm.
    Replace every letter in the string with the letter following it
    in the alphabet (ie. c becomes d, z becomes a).
    Then capitalize every vowel in this new string (a, e, i, o, u)
    and finally return this modified string.
    Input: abcd
    Output: bcdE
    '''

    mod_str = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in my_str:
        i = i.lower()
        if 96 < ord(i) < 123:
            if i == 'z':
                i = 'a'
            else:
                i = chr(ord(i) + 1)
        if i in vowels:
            i = i.upper()
        mod_str += i
    return mod_str


def sorted_word(word):
    '''
    Write a program that will take the str string parameter being passed
    and return the string with the letters in alphabetical order
    (ie. hello becomes ehllo).
    Assume numbers and punctuation symbols will not be included in the string.
    Input: edcba
    Output: abcde
    '''
    return ''.join(sorted(word))


def number_compare(a, b):
    '''
    Write a program that will take both parameters being passed
    and return the true if num2 is greater than num1,
    otherwise return the false.
    If the parameter values are equal to each other then return the string -1
    '''
    if b > a:
        return True
    elif a == b:
        return '-1'
    else:
        return False
