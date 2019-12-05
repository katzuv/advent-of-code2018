def get_numbers_from_input():
    with open('../inputs/2.txt') as input_file:
        numbers = [int(number) for number in input_file.read().split(',')]
    return numbers


def program_output(program):
    numbers = program[:]
    for i in range(0, len(numbers), 4):
        opcode = numbers[i]
        if opcode == 99:
            break
        first = numbers[numbers[i + 1]]
        second = numbers[numbers[i + 2]]
        output_index = numbers[i + 3]
        if opcode == 1:
            numbers[output_index] = first + second
        elif opcode == 2:
            numbers[output_index] = first * second
    return numbers[0]


def main():
    numbers = get_numbers_from_input()
    numbers[1] = 12
    numbers[2] = 2
    output = program_output(numbers)
    print(f'Value at position 0: {output[0]}')



if __name__ == '__main__':
    main()
