"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    选择第k个，在para中通过select筛选的函数
    @return string
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    new_para = [item for item in paragraphs if select(item)]
    if k >= len(new_para):
        return ''
    else:
        return new_para[k]
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.
    构造一个select函数，参数为sentence，检查topic的单词是否在sentence之中
    @return function

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    # def helper(sentence):
    #     sentence_list = split(lower(remove_punctuation(sentence)))
    #     for word in topic:
    #         if word in sentence_list:
    #             return True
    #     return False
    # return helper
    return lambda sentence: any(word in split(lower(remove_punctuation(sentence))) for word in topic)
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.
    匹配度检测；以空格为分界，逐个匹配单词；标点符号包含在单词内检测，大小写敏感；
    @return int 匹配的单词数 / 总单词数 * 100

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    # 对照单词数
    ref_amount_words = len(reference_words)
    # 输入单词数
    typed_amount_words = len(typed_words)

    if typed_amount_words == 0:
        # 快捷通道，直接返回0
        return 0.0
    else:
        # 成功匹配的单词数
        correct = 0
        # 逐个比较两个列表中的单词，相同则correct+1
        for i in range(min(typed_amount_words,ref_amount_words)):
            correct += 1 if typed_words[i]==reference_words[i] else 0
        # 根据输入单词数返回正确率
        return correct / typed_amount_words * 100
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string.
    打字速度；五个字符作为一个单词；
    @typed 待计算的字符串
    @elapsed 完成该字符串的时间（秒）
    @return float 每分钟键入单词数
    """
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    # typed_len = len(typed)
    # words_amount = typed_len / 5
    # ratio = 60 / elapsed
    # return words_amount * ratio
    return len(typed) * 12 / elapsed
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    自动校正单词；使用diff_func比较两个单词，返回一个数值；diff需要三个参数
    @return diff_func返回值最小的单词；若该返回值均大于limit，则返回user_word
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    similar = (None,99999999999)
    for i,word in enumerate(valid_words):
        if word == user_word:
            return user_word
        diff = diff_function(user_word,word,limit)
        if diff < similar[1]:
            similar = (word,diff)
    if similar[1] > limit:
        return user_word
    return similar[0]

    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    从头开始比较两个字符串， 返回不相同的字符个数或字符数目之差；limit限制不相同的字符个数，当limit为0时结束迭代直接返回
    """
    # BEGIN PROBLEM 6
    # 根据index迭代
    # if (diff_len:=len(goal) - len(start)) > 0:
    #     short, long = start, goal
    # else:
    #     long, short = start, goal
    # diff = 0
    # for i in range(len(short)):
    #     diff += 0 if short[i] == long[i] else 1
    # return diff + abs(diff_len)

    # 递归
    # 相等快速通道
    if start == goal:
        return 0
    elif limit<1 or not start or not goal:
        # 结束迭代条件，字符串为空或limit为0
        return max(len(goal), len(start))
    else:
        diff = 0
        if start[0] != goal[0]:
            # 比较首字符，若不同则limit-1并记录
            limit -= 1
            diff = 1
        return diff + shifty_shifts(start[1:],goal[1:],limit)

    # END PROBLEM 6


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    assert False, 'Remove this line'

    if ______________: # Fill in the condition
        # BEGIN
        "*** YOUR CODE HERE ***"
        # END

    elif ___________: # Feel free to remove or add additional cases
        # BEGIN
        "*** YOUR CODE HERE ***"
        # END

    else:
        add_diff = ... # Fill in these lines
        remove_diff = ...
        substitute_diff = ...
        # BEGIN
        "*** YOUR CODE HERE ***"
        # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)