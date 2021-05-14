from hog import play, always_roll, announce_highest, both
from dice import make_test_dice
# this might not technically be a possible game for the current rules, this shouldn't be relevant
f0 = announce_highest(1) # Only announce Player 1 score gains
f1 = f0(12, 0)
f2 = f1(12, 10)
f3 = f2(20, 10)
f4 = f3(22, 20)
f5 = f4(22, 35)
f6 = f5(30, 47) # Player 1 gets 12 points; not enough for a new high
f7 = f6(31, 47)
f8 = f7(32, 77)
f9 = f8(83, 32)
f10 = f9(38, 83)
# The following function call checks if the behavior of f1 changes,
# perhaps due to a side effect other than printing. The only side
# effect of a commentary function should be to print.
f2_again = f1(11, 9)
