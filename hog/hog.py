"""CS 61A Presents The Game of Hog."""

from dice import six_sided, four_sided, make_test_dice
from ucb import main, trace, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.
FIRST_101_DIGITS_OF_PI = 31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679

######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.
    投掷某数量的骰子，骰子点数和为得分；若存在一个骰子点数为1，则返回值为1（Pig Out规则）；返回数值

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome. 骰子模拟函数
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    total = 0
    # 循环固定次数的骰子模拟函数
    for i in range(num_rolls):
        cur_value = dice()
        #当total为-1时，表示Pig Out情况，并跳过当次循环
        if total != -1:
            #当某一次骰子点数为1，将total标记为-1
            if cur_value == 1:
                total = -1
            else:
                total += cur_value
    return total if total >=0 else 1
    # END PROBLEM 1


def free_bacon(score):
    """Return the points scored from rolling 0 dice (Free Bacon).
    在pi中，取某一位数+3作为得分；返回数值

    score:  The opponent's current score.
    """
    assert score < 100, 'The game should be over.'
    pi = FIRST_101_DIGITS_OF_PI

    # Trim pi to only (score + 1) digit(s)
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    pi //= 10**(100-score)

    # END PROBLEM 2

    return pi % 10 + 3


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player.
    模拟执行一回合，计算得分；当num_rolls参数为0时，则使用Free Bacon规则；返回数值

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if not num_rolls:
        return free_bacon(opponent_score)
    else:
        return roll_dice(num_rolls,dice)
    # END PROBLEM 3


def extra_turn(player_score, opponent_score):
    """Return whether the player gets an extra turn.
    判断是否能执行一个额外回合；返回布尔值
    """
    return (pig_pass(player_score, opponent_score) or
            swine_align(player_score, opponent_score))


def swine_align(player_score, opponent_score):
    """Return whether the player gets an extra turn due to Swine Align.
    Swine Align规则
    若你和对手的得分的最大公约数大于等于10，则你执行一个额外回合；返回布尔值

    player_score:   The total score of the current player.
    opponent_score: The total score of the other player.

    >>> swine_align(30, 45)  # The GCD is 15.
    True
    >>> swine_align(35, 45)  # The GCD is 5.
    False
    """
    # BEGIN PROBLEM 4a
    "*** YOUR CODE HERE ***"
    def find_gcd(small,big):
        if small > big:
            small, big = big, small
        for cur in range(small, 0, -1):
            if small%cur==0 and big%cur==0:
                return cur

    if player_score==0 or opponent_score==0: return False
    cur_gcd = find_gcd(player_score,opponent_score)
    return cur_gcd >= 10

    # END PROBLEM 4a


def pig_pass(player_score, opponent_score):
    """Return whether the player gets an extra turn due to Pig Pass.
    Pig Pass规则
    若当前你的得分比对手小1或2，则进行额外回合；返回布尔值

    player_score:   The total score of the current player.
    opponent_score: The total score of the other player.

    >>> pig_pass(9, 12)
    False
    >>> pig_pass(10, 12)
    True
    >>> pig_pass(11, 12)
    True
    >>> pig_pass(12, 12)
    False
    >>> pig_pass(13, 12)
    False
    """
    # BEGIN PROBLEM 4b
    "*** YOUR CODE HERE ***"
    if 0 < opponent_score-player_score < 3:
        return True
    else:
        return False
    # END PROBLEM 4b


def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.
    切换当前选手指示值

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who


def silence(score0, score1):
    """Announce nothing (see Phase 2)."""
    return silence


def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,
         goal=GOAL_SCORE, say=silence):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.
    模拟游戏中的一回合，并判断是否需要进行额外回合，并计算分数；返回两个数值

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first.
    strategy1:  The strategy function for Player 1, who plays second.
    score0:     Starting score for Player 0
    score1:     Starting score for Player 1
    dice:       A function of zero arguments that simulates a dice roll.
    goal:       The game ends and someone wins when this score is reached.
    say:        The commentary function to call at the end of the first turn.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    # 执行回合直到其中一个玩家胜利
    while score0<goal and score1<goal:
        # 根据who，决定当前执行回合的玩家
        if who == 0:
            cur_strategy, cur_score, opponent_score = strategy0, score0, score1
        else:
            cur_strategy, cur_score, opponent_score = strategy1, score1, score0
        # 投骰子的结果
        cur_score += take_turn(cur_strategy(cur_score, opponent_score), opponent_score, dice)
        # 更新玩家分数
        if who == 0:
            score0 = cur_score
        else:
            score1 = cur_score
        # 执行额外回合
        say = say(score0,score1)
        if extra_turn(cur_score, opponent_score):
            continue
        # 交换回合
        who = other(who)
    # END PROBLEM 5
    # (note that the indentation for the problem 6 prompt (***YOUR CODE HERE***) might be misleading)
    # BEGIN PROBLEM 6
    "*** YOUR CODE HERE ***"
    # END PROBLEM 6
    return score0, score1


#######################
# Phase 2: Commentary #
#######################


def say_scores(score0, score1):
    """A commentary function that announces the score for each player.
    报道分数；返回该函数
    """
    print("Player 0 now has", score0, "and Player 1 now has", score1)
    return say_scores


def announce_lead_changes(last_leader=None):
    """Return a commentary function that announces lead changes.
    当反超时，报道分数；返回函数

    >>> f0 = announce_lead_changes()
    >>> f1 = f0(5, 0)
    Player 0 takes the lead by 5
    >>> f2 = f1(5, 12)
    Player 1 takes the lead by 7
    >>> f3 = f2(8, 12)
    >>> f4 = f3(8, 13)
    >>> f5 = f4(15, 13)
    Player 0 takes the lead by 2
    """
    def say(score0, score1):
        if score0 > score1:
            leader = 0
        elif score1 > score0:
            leader = 1
        else:
            leader = None
        if leader != None and leader != last_leader:
            print('Player', leader, 'takes the lead by', abs(score0 - score1))
        return announce_lead_changes(leader)
    return say


def both(f, g):
    """Return a commentary function that says what f says, then what g says.
    混合报道

    NOTE: the following game is not possible under the rules, it's just
    an example for the sake of the doctest

    >>> h0 = both(say_scores, announce_lead_changes())
    >>> h1 = h0(10, 0)
    Player 0 now has 10 and Player 1 now has 0
    Player 0 takes the lead by 10
    >>> h2 = h1(10, 8)
    Player 0 now has 10 and Player 1 now has 8
    >>> h3 = h2(10, 17)
    Player 0 now has 10 and Player 1 now has 17
    Player 1 takes the lead by 7
    """
    def say(score0, score1):
        return both(f(score0, score1), g(score0, score1))
    return say


def announce_highest(who, last_score=0, running_high=0):
    """Return a commentary function that announces when WHO's score
    increases by more than ever before in the game.
    报道某玩家的历史最高单回合得分；返回一个函数

    NOTE: the following game is not possible under the rules, it's just
    an example for the sake of the doctest

    >>> f0 = announce_highest(1) # Only announce Player 1 score gains
    >>> f1 = f0(12, 0)
    >>> f2 = f1(12, 9)
    9 point(s)! The most yet for Player 1
    >>> f3 = f2(20, 9)
    >>> f4 = f3(20, 30)
    21 point(s)! The most yet for Player 1
    >>> f5 = f4(20, 47) # Player 1 gets 17 points; not enough for a new high
    >>> f6 = f5(21, 47)
    >>> f7 = f6(21, 77)
    30 point(s)! The most yet for Player 1
    """
    assert who == 0 or who == 1, 'The who argument should indicate a player.'
    # BEGIN PROBLEM 7
    "*** YOUR CODE HERE ***"
    # 闭包函数
    def announce_change(score0, score1):
        nonlocal last_score, running_high
        cur_score = score0 if who == 0 else score1
        if (diff:=cur_score - last_score) > running_high:
            print('{} point(s)! The most yet for Player {}'.format(diff, who))
            return announce_highest(who,cur_score,diff)
        # 返回新的闭包函数，每一步都可以复用
        return announce_highest(who,cur_score,running_high)

    return announce_change
    # END PROBLEM 7


#######################
# Phase 3: Strategies #
#######################


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy


def make_averaged(original_function, trials_count=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    when called.
    循环调用设定的函数，并求均值；返回一个函数

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.0
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    def get_averaged(*args):
        result = 0
        for i in range(trials_count):
            # 透传新的参数到original_function
            result += original_function(*args)
        return result / trials_count

    return  get_averaged

    # END PROBLEM 8


def max_scoring_num_rolls(dice=six_sided, trials_count=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over TRIALS_COUNT times.
    Assume that the dice always return positive outcomes.
    执行策略：单次得分的最大期望值
    调用（1到10个）dice骰子trials_count次，计算其均值，并返回取最大均值时的骰子数

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    max_score = 0
    result =0
    # 分别取1到10个骰子
    for i in range(1,11):
        # total = 0
        # for n in range(trials_count):
        #     total += roll_dice(i, dice)
        total = sum(roll_dice(i, dice) for n in range(trials_count))
        if (new_score:=total/trials_count )> max_score:
            # 找出最大均值
            max_score = new_score
            result = i
    return result
    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if True:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)

    if False:  # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if False:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False:  # Change to True to test extra_turn_strategy
        print('extra_turn_strategy win rate:', average_win_rate(extra_turn_strategy))

    if False:  # Change to True to test final_strategy
        print('final_strategy win rate:', average_win_rate(final_strategy))

    "*** You may add additional experiments as you wish ***"



def bacon_strategy(score, opponent_score, cutoff=8, num_rolls=6):
    """This strategy rolls 0 dice if that gives at least CUTOFF points, and
    rolls NUM_ROLLS otherwise.
    执行策略：若使用Free Bacon规则的得分大于等于cutoff时，则使用该规则（返回0），否则返回num_rolls；
    返回值：计划使用的骰子数目
    """
    # BEGIN PROBLEM 10
    return 0 if free_bacon(opponent_score) >= cutoff else num_rolls
    # END PROBLEM 10


def extra_turn_strategy(score, opponent_score, cutoff=8, num_rolls=6):
    """This strategy rolls 0 dice when it triggers an extra turn. It also
    rolls 0 dice if it gives at least CUTOFF points and does not give an extra turn.
    Otherwise, it rolls NUM_ROLLS.
    执行策略：优先获取额外回合
    若使用free_bacon规则能获取额外回合，则返回0；如不能获取额外回合，则使用bacon_strategy；
    返回值：计划使用的骰子数目
    """
    # BEGIN PROBLEM 11
    if extra_turn(free_bacon(opponent_score) + score, opponent_score):
        return 0
    else:
        return bacon_strategy(score, opponent_score, cutoff, num_rolls)
    # END PROBLEM 11


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.
    执行策略：
    1.检测使用bacon能否直接获得胜利；
    2.若分差为2，直接使用7个骰子；
    3.优先获取额外回合；
    4.若分差大于30，则使用7个骰子追赶；
    5.令cutoff为max_scoring_num_rolls=7，执行bacon_strategy，获得较高的分数；
    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 12
    bacon = free_bacon(opponent_score)
    cutoff = 8
    num_rolls = 7
    if score + bacon >= 100:
        return 0
    elif opponent_score - score == 2:
        return 7
    elif score - opponent_score >= 30:
        return extra_turn_strategy(score,opponent_score,100,num_rolls)
    else:
        return extra_turn_strategy(score,opponent_score,cutoff,num_rolls)

    # END PROBLEM 12

##########################
# Command Line Interface #
##########################

# NOTE: Functions in this section do not need to be changed. They use features
# of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()