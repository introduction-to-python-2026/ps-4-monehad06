def split_before_each_uppercases(formula):
    start = 0
    result = []
    for end in range(1, len(formula)):
        if formula[end].isupper():
            result.append(formula[start:end])
            start = end
    result.append(formula[start:])
    return result
def split_at_digit(formula):
    digit_location = 1
    for char in formula[1:]:
        if char.isdigit():
            break
        digit_location += 1

    if digit_location == len(formula):
        return formula, 1

    return formula[:digit_location], int(formula[digit_location:])
