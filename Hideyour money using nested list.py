#Exercise no 10 -to hideyour money using nested list

row1 = ['🦋','🦋','🦋']
row2 = ['🦋','🦋','🦋']
row3 = ['🦋','🦋','🦋']
matrix = [row1,row2,row3]
print(f"{row1} \n{row2} \n{row3}")
position = input("Enter the position where your want to hide something: ")
row_number = int(position[0])
column_number = int(position[1])
row_selected = matrix[row_number-1]
row_selected[column_number-1] = 'x'
print(f"{row1} \n{row2} \n{row3}")