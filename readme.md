# Bubble Sort

## Introduction

Bubble Sort is a simple sort, if not a particularly efficient one, and thus makes a great starting point for our sorting journey.

The function `bubble_sort` has been started for you in `bubble_sort.py`, along with an example test case. That is the only file you'll need to touch for this lab.

## Algorithm Outline

- In the outer loop, perform one pass of the whole list, comparing pairs, for EACH number in your list.
- In the inner loop, you will perform each actual pass, performing the following steps:
  1. Compare each number to the next.
  2. Check if they're in the wrong order.
  3. If they are... swap them!

## Hints

- It's a good idea to save the length of your list into a variable for easy access.
- `range` is really useful in your `for` loops.
- Getting the error `IndexError: list index out of range`? You probably compared the last number with the one after--there is nothing after the last number! (That's what "last" means...)
- In Python, you can swap two values with the following sweet sweet syntax:

```python
x = 5
y = 10
x, y = y, x
print(x) # --> 10
print(y) # --> 5

someList = [1, 2, 3]
someList[0], someList[2] = someList[2], someList[0]
print(someList) # --> [3, 2, 1]
```

## Stretch Goals

### Implement Bubble Sort In JavaScript

It's a bit more verbose, but has some actual added challenge, thanks to not having Python's shortcut for swapping values.

### Implement Selection Sort

Similar structure to Bubble Sort (still requires a nested loop, so O(n^2) time), but with less actual swapping necessary; just once per outer loop!

Each time through the inner loop, you'll find the smallest number, and then move it all the way to the left. An example:

Say you've got a list of `[3, 7, 6, 1, 2]`.

The first pass through the loop, you find the smallest number and swap it with the first element. So the `1` would swap with the `3`, giving you:

`[1, 7, 6, 3, 2]`

Next, you move to the next index (index `1`, where the `7` is located) and perform the same operation, swapping the smallest number to the right with the current index. So the `2` would swap places with the `7`, giving you:

`[1, 2, 6, 3, 7]`

Selection Sort is different enough from Bubble Sort that implementing it is going to require you to get the flow of logic of _both_. Good luck!
