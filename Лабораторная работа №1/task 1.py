numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
# Исходный список с пропущенным элементом
numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

missing_index = numbers.index(None)

sum_without_missing = sum(x for x in numbers if x is not None)

count = len(numbers)

mean = sum_without_missing / (count )

mean = round(mean, 2)

numbers[missing_index] = mean

print("Измененный список:", numbers)



