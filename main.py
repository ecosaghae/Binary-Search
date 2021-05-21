"""
Hey guys, welcome back. Today I will be showing you how the binary search algorithm works.
Binary search is very useful because of the speed
Binary search algorithm is to look through an already sorts list and determine whether an item is in that list
in this example, we are looking for the number 9 in this list.
8 is the midpoint. If the number is that we are looking for is higher then we choose to only look through the
items to the right of the midpoint. If it's lower, then we chose the items to the left.
"""
# [2, 4, 5, 7, 8, 9, 13, 17, 21]

# first, we will def binary search, which takes 2 arguments. we will give it some list called l and the item we are
# looking for. l would be this list on line 1 and will will allow our user to pick the number they want to find
def binary(l, item):
    # to find the midpoint of each iteration, we need to know the beginning and ending index. we do this by saying
    low_index = 0  # we start with the first element
    high_index = len(l) - 1  # end with the last element # set to whatever the last index is

    # lets get our midpoint
    # as long as the low is lower than the high then
    while low_index <= high_index:
        # the midpoint should be middle position between our begin index and and the rest of the items in our sequence
        # set midpoint to basically the average. low + high divided by 2. we want to round down how many times this list is divided by 2
        #  and one way to do that is just adding another slash. the // mean how many times does 2 go into the quantity of low + high. Really just rounding down
        midpoint = (low_index + high_index) // 2
        # compare value of midpoint to the value we are searching for
        midpoint_value = l[midpoint]  # This will return value rather that position of midpoint
        # if midpoint is equal to the number we are searching for, just return value
        if midpoint_value == item:
            return midpoint

        # The number we are searching for will be to the left of the midpoint
        # so is the item less than midpoint, if it is then we want to search the left hand side
        elif item < midpoint_value:
            # set a high high index midpoint is set to minus 1 because we don't want to search the midpoint since we
            # know it doesnt equal the item
            high_index = midpoint - 1  # Ending position will be the element directly to the left of the midpoint

        # The number we are searching for will be to the right if greater than midpoint
        else:
            # only need to check items to the right of thr midpoint and repositioning our beginning index
            # we don't want to look at the midpoint since its not the item we are looking for so go one over
            low_index = midpoint + 1


list_a = [2, 4, 5, 7, 8, 9, 13, 17, 21]
item = int(input('Enter a number from [2, 4, 5, 7, 8, 9, 13, 17, 21]: '))
print(binary(list_a, item))

'''

length == 1000
sorted_list = set()

while len(sorted_list) < length:
    sorted_list.add(random.randint(-3 * length, 3 * length))
sorted_list = sorted(list(sorted_list))

target_list = [random.randint(-3 * length, 3 * length) for _ in range(length)]

start = time.time()
end = time.time()
print("naive time is:", (end - start), 'seconds')
start = time.time()
end = time.time()
print("Binary search time is:", (end - start), 'seconds')

item = int(input('Enter a number from [2, 4, 5, 7, 8, 9, 13, 17, 21]: '))

I hope you guys have learned something new about basic computer science. We can search how much more 
effeictive binary search is
'''
