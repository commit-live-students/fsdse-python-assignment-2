pair = [2, 5, 4, 3, 8, 7, 6, 1, 10, -1]
num = 9

def pairSum(all_numbers, num):
    pair = []
    if len(all_numbers) < 2:
        return
    for index, element in enumerate(all_numbers):
        for next_element in all_numbers[index+1:]:
            if element + next_element == num:
                return [(element, next_element)]
