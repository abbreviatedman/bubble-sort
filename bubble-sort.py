# range is really useful in your for loops
# In Python, you can swap two values with the following sweet sweet syntax:
x = 5
y = 10
x, y = y, x;
print(x) # --> 10
print(y) # --> 5

someList = [1, 2, 3]
someList[0], someList[2] = someList[2], someList[0]
print(someList) # --> [3, 2, 1]
#  Getting the error "IndexError: list index out of range"? You probably compared the last number with the one after--there is nothing after the last number! (That's what "last" means...)
def bubble_sort(arr):
  # save length into a variable for easy access
  n = len(arr)
  # outer loop - one run-through of comparisons for each number.
  for i in range(n):
    # inner loop - for each run-through, hit every element...
    for j in range(n - 1):
      # ...comparing it to the next...
      if arr[j] > arr[j + 1]:
        # ...and swapping them if they're in the wrong order..
        arr[j], arr[j + 1] = arr[j + 1], arr[j]

nums = [3, 5, 6, 8]
bubble_sort(nums)
print(nums)
