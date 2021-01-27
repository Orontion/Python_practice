import re


def get_valid_input(input_pattern, prompt_text, split_char):
    correct_input = False
    while not correct_input:
        input_string = input(prompt_text)

        print(input_string)

        correct_input = re.match(input_pattern, input_string)

    return list(map(lambda x: int(x), input_string.split(split_char)))


m1_dimensions_input_pattern = '[1-9],[1-9]'
m1_rows, m1_columns = get_valid_input(m1_dimensions_input_pattern, "Please enter matrix 1 dimensions: ", ',')

m2_dimensions_input_pattern = f'{m1_columns},[1-9]'
m2_rows, m2_columns = get_valid_input(m2_dimensions_input_pattern, "Please enter matrix 2 dimensions: ", ',')

m1_rows_input_pattern = f"^\\d+(?:,\\d+){{{m1_columns-1}}}$"
matrix_1 = []
for row in range(m1_rows):
    matrix_1.append(get_valid_input(m1_rows_input_pattern, f"Please enter {row+1} row of matrix 1: ", ','))

print("\r\n\r\nMatrix 1:")
for i in range(len(matrix_1)):
    print(matrix_1[i])

m2_rows_input_pattern = f"^\\d+(?:,\\d+){{{m2_columns-1}}}$"
matrix_2 = []
for row in range(m2_rows):
    matrix_2.append(get_valid_input(m2_rows_input_pattern, f"Please enter {row+1} row of matrix 2: ", ','))

print("\r\n\r\nMatrix 2:")
for i in range(len(matrix_2)):
    print(matrix_2[i])

matrix_result = []
for row in range(m1_rows):
    row_result = []
    for column in range(m2_columns):
        result = 0
        for current_item in range(m1_columns):
            result += (matrix_1[row][current_item] * matrix_2[current_item][column])

        row_result.append(result)

    matrix_result.append(row_result)

print("\r\n\r\nResult:")
for i in range(len(matrix_result)):
    print(matrix_result[i])
