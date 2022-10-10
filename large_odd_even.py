# A function to find the largest odd number in an integer array

def largeOdd(array):

    large_odd = array[0]

    for n in array:
        if n > large_odd and n % 2 != 0:
            large_odd = n
    return large_odd


# A function to find the largest even number in an integer array

def largeEven(array):

    large_even = array[0]

    for n in array:
        if n > large_even and n % 2 == 0:
            large_even = n
    return large_even

array = [90, 89, 78, 67, 56, 45, 34, 23, 11, 111, 671, 690]
print()
print("The largest odd number in the array is", largeOdd(array))
print()
print("The largest even number in the array is", largeEven(array))
print()
