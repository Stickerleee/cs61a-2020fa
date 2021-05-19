HW_SOURCE_FILE=__file__


def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.
    返回x中数字8的个数，函数中不能使用赋值语句

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if x < 10:
        return 1 if x == 8 else 0
    if x % 10 ==8:
        return num_eights(x // 10) + 1
    else:
        return num_eights(x // 10)

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    # iteration
    # index, k, cur = 1, 1, 1
    # while index < n:
    #     cur += k
    #     index += 1
    #     if index % 8 == 0 or num_eights(index):
    #         k = -k
    # return cur

    # 也不能用赋值语句，只能使用嵌套函数的参数代替赋值语句
    def func(target,index=1,cur=1,k=1):
        if index == target:
            return cur
        if index % 8 == 0 or num_eights(index):
            return func(target,index+1,cur-k,-k)
        else:
            return func(target,index+1,cur+k,k)
    return func(n)



def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        return 0
    # 小于最大值的数值数目
    result = n % 10 - 1
    def helper(n, before):
        nonlocal result
        if n < 10:
            # 从结果中减去最小值
            result -= n
            return
        if (cur:=n % 10) < before:
            result -= 1
        return helper(n // 10, cur)
    helper(n // 10, result + 1)
    return result if result > 0 else 0


def next_largest_coin(coin):
    """Return the next coin. 
    >>> next_largest_coin(1)
    5
    >>> next_largest_coin(5)
    10
    >>> next_largest_coin(10)
    25
    >>> next_largest_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def count_coins(total):
    """Return the number of ways to make change for total using coins of value of 1, 5, 10, 25.
    不能使用迭代
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])                                          
    True
    """
    "*** YOUR CODE HERE ***"
    coins = [1, 5, 10, 25]
    # 动态规划法
    # dp = [[0 for _ in range(total + 1)] for _ in range(4)]
    #
    # # 初始化dp表
    # for j in range(total + 1):
    #     dp[0][j] = 1 if j % coins[0] == 0 else 0
    # # i为使用的币种数目，从两种币种开始循环，j为组成的金额
    # for i in range(1,len(coins)):
    #     for j in range(total+1):
    #         if j < coins[i]:
    #             # 若当前金额比当前币种面值小，则直接返回i-1的值
    #             dp[i][j] = dp[i-1][j]
    #         else:
    #             # 若当前金额比当前币种面值大，依次减去当前币种面值，返回dp[i-1][j]+dp[i][j-1*coins[i]]+...+dp[i-1][j-k*coins[i]]
    #             # 简化为下列等式
    #             dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i]]
    #
    # return dp[len(coins)-1][total]

    # 递归
    # helper函数
    def helper(amount,total):
        '''
        @amount：币种数目
        @total：目标金额数
        @return：找零方法数目
        '''
        if amount == 1:
            return 1
        if total < coins[amount-1]:
            return helper(amount-1,total)
        else:
            return helper(amount-1,total) + helper(amount,total-coins[amount-1])

    return helper(4,total)


from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'

