import random
characters = 'abcdefghijklmnopqrstuvwxyz_!@$&()1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
pw_length = 8
mypw = ''
for i in range(pw_length):
    next_index = random.randrange(len(characters))
    mypw = mypw + characters[next_index]

print(mypw)
