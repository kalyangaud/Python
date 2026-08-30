#Understanding the sparation of elements from array list 
def separate_elements(array):
    even_numbers = []
    odd_numbers = []
    for sublist in array:
        for element in sublist:
            if element % 2 == 0:
                even_numbers.append(element)
            else:
                odd_numbers.append(element)
    return even_numbers, odd_numbers
data = [
    [10, 15, 22, 33],
    [8, 19, 26, 31],
    [7, 12, 18, 25]
]
evens, odds = separate_elements(data)
print("Original nested array:", data)
print("Even numbers:", evens)
print("Odd numbers:", odds)