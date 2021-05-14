import hog

always_three = hog.make_test_dice(3)
always = hog.always_roll
s0, s1 = hog.play(always(5), always(5), goal=25, dice=always_three)
print(s0,s1)
