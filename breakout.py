# X O
# XO 
# X O
#print('X 0')
#print('X0 ')
#print('X 0')
row1 = ['_', '_', '_']
row2 = ['_', '_', '_']
row3 = ['_', '_', '_']

for cell in row1: 
    print(cell, end='')
print('\n')
for cell in row2: 
    print(cell, end='')
print('\n')
for cell in row3: 
    print(cell, end='')
    
#print(row1[0],row1[1], row1[2])
#print(row2)
#print(row3)
print()
user1_row = input('User1, please write your row: ')
user1_column = input('User1, please write your column: ')

user1_column_int = int(user1_column)
user1_row_int = int(user1_row)

if user1_row_int == 1:
    selected_cell = row1[user1_column_int - 1]
    row1[int(user1_column) - 1] = 'X'
elif user1_row_int == 2:
    selected_cell = row2[user1_column_int - 1]
else:
    selected_cell = row3[user1_column_int - 1]

print(row1)
print(row2)
print(row3)