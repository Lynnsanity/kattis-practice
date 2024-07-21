word = input()

kiki_counter = 0
boba_counter = 0
for letter in word:
    if letter == "k":
        kiki_counter += 1
    elif letter == "b":
        boba_counter += 1
    else:
        continue

if kiki_counter > boba_counter:
    print("kiki")
elif kiki_counter < boba_counter:
    print("boba")
elif kiki_counter == boba_counter:
    if kiki_counter == 0 and boba_counter == 0:
        print("none")
    else:
        print("boki")

