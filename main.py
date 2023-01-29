





  # 23
row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]  # 0 X 0
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

"""print(position[0])
print(position[1])"""

"""if position[1] == 1:
    if position[0] == 1:
        row1[0]= 'X'
    elif position[0] == 2:
        row1[1]= 'X'
    elif position[0] == 3:
        row1[2]= 'X'
if position[1] == 2:
    if position[0] == 1:
        row2[0]= 'X'
    elif position[0] == 2:
        row2[1]= 'X'
    elif position[0] == 3:
        row2[2]= 'X'
if position[1] == 3:
    if position[0] == 1:
        row3[0]= 'X'
    elif position[0] == 2:
        row3[1]= 'X'
    elif position[0] == 3:
        row3[2]= 'X'"""


horizontal = int(position[0]) # 2
vertical = int(position[1]) # 3

map[vertical-1][horizontal-1]= "X"

"""selected_row = map[vertical-1]
selected_row[horizontal-1]= "X"""

#print(map[vertical-1])

print(f"{row1}\n{row2}\n{row3}")

