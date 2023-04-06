row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

position = list(position)
X = int(position[0])
Y = int(position[1])
selection = map[X - 1][Y - 1] = "'x'"

print(f"{row1}\n{row2}\n{row3}")