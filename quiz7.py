# Question 1

class Animal:
    def __init__(self, name: str, age: int, food: list) -> None:
        self.name = name
        self.age = age
        self.food = food

    def get_name(self):
        print(f"My name is {self.set_name()}")

    def set_name(self):
        return self.name

    def get_age(self):
        print(f"My age is {self.set_age()}")

    def set_age(self):
        return self.age

    def get_food(self):
        print(f"My food is {self.add_food()}")

    def add_food(self):
        return self.food
    
    def foodEmpty(self):
        return len(self.food) == 0

    def remove_food(self):
        if self.foodEmpty():
            print("There is no food.")
        else:
            self.food.remove()


class Dog(Animal):
    def __init__(self, name: str, age: int, food: list) -> None:
        super().__init__(name, age, food)

    def talk(self):
        return "Dog-sound: WOFF WOFF"


class Cow(Animal):
    def __init__(self, name: str, age: int, food: list) -> None:
        super().__init__(name, age, food)

    def talk(self):
        return "Cow-sound: MUUU"

class Cat(Animal):
    def __init__(self, name: str, age: int, food: list) -> None:
        super().__init__(name, age, food)

    def talk(self):
        return "Cat-sound: MOEW"

class Fish(Animal):
    def __init__(self, name: str, age: int, food: list) -> None:
        super().__init__(name, age, food)

    def talk(self):
        return "Fish-sound: Blub"


d = Dog('Chris', 4, ['Meat', 'Milk', 'Bisquits'])
c1 = Cow('John', 8, ['Grass', 'Peelings'])
c2 = Cat('Jim', 2, ['Bisquits', 'Milk', 'Meat'])
f = Fish('Jolly', 1, ['Worms'])

for instance in [d, c1, c2, f]:
    print(instance.talk())
    print()

# Question 2


def snail(depth):
    total_ascent = 7
    descent = 2

    actual_ascent = total_ascent - descent

    days_taken_out = depth//actual_ascent

    return days_taken_out

print(snail(31))


# Question 3

def largest(array):
    # largest_ = max(array)
    # return largest_
    
    largest_ = 0
    for n in array:
        if n > largest_:
            largest_ = n
    return largest_


array = [45, 89, 67, 23, 91, 92]
print(largest(array))

# Questoin 4

sentence = "Hello world!"
num_upper = 0
num_lower = 0

for char in sentence:
    if char.isupper():
        num_upper += 1
    elif char.islower():
        num_lower += 1

print(f'UPPER CASE: {num_upper}\nLOWER CASE: {num_lower}')


# Question 5

class Dice:

    def __init__(self, player1, player2, score1, score2) -> None:
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2

    def play(self):
        rolls = [1, 2, 3, 4, 5, 6]
        n_rolls = 0
        points = 0

        while True:
            for roll in rolls:
                print("Roll the Dice!")
                if roll == 6:
                    print("Roll again!")
                    points += 1
                    n_rolls += 1
                else:
                    if roll == 6 and n_rolls == 3:
                        print("Pass the Dice! Your turn is over.")





                








# Question 6

class Stack:
    def __init__(self) -> None:
        self.my_stack = []

    def push(self, item):
        self.my_stack.append(item)
        return self.my_stack

    def pop(self):
        if len(self.my_stack) == 0:
            return "Can't delete from empty stack!"
        else:
            self.my_stack.pop()
        return self.my_stack

    def traversal(self):
        return self.my_stack[-1]
        
s = Stack()
print()
print(s.push(1))
print(s.push(2))
print(s.push('one'))
print(s.push('two'))
print()
print(s.pop())
print()
print(s.traversal())
print()

# Question 7

data = [1, 2, 3, 4, 5, 6]
squares = [n*n for n in data]       # Using list comprehension to get a list of squares of numbers

print(squares)
print()

# Question 8

my_queue = []

def enqueue(item):
    my_queue.insert(0, item)
    return my_queue

def dequeue():
    if len(my_queue) > 0:
        my_queue.pop(-1)
        return my_queue

def size():
    return len(my_queue)


print(enqueue(1))
print(enqueue(2))
print(enqueue('one'))
print(enqueue('two'))
print()
print(dequeue())
print()
print(size())
print()

# Question 9


def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        mid = len(array)//2
        left_arr = array[:mid]
        right_arr = array[mid:]

        # Sort the two halves
        mergeSort(left_arr)
        mergeSort(right_arr)

        i = j = k = 0

        # Until we reach either end of either left_arr or right_arr, pick larger among
        # elements left_arr and right_arr and place them in the correct position at A[p..r]
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                array[k] = left_arr[i]
                i += 1
            else:
                array[k] = right_arr[j]
                j += 1
            k += 1

        # When we run out of elements in either left_arr or right_arr,
        # pick up the remaining elements and put in A[p..r]
        while i < len(left_arr):
            array[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            array[k] = right_arr[j]
            j += 1
            k += 1


# Print the array
array = [90, 67, 12, 56, 8, 3, 113, 1]
mergeSort(array)
print(array)


        



