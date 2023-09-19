"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x<= 1:
      return x
    else:
      ra = foo(x-1)
      rb = foo(x-2)
      return ra + rb

def longest_run(mylist, key):
    curr = 0
    max = 0

    for i in mylist:
      if mylist[i] == key:
        curr += 1
      else:
        if curr > max:
          max = curr
        curr = 0
    return max
  
class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
  #think the below is not a viable solution bc we have to use divide and conquer and the
  #class Result which means this will be dividing our list into left & right, searching
  #each half for the key, and combining the results.
    #curr = 0
    #max = 0
  
    #base: if list only has one 1 and its the key
    #if len(mylist) == 0:
      #return 0
    #recursive:
    #curr = 1
    #for i in range(0, len(mylist)):
    #  if mylist[i] == key:
    #    curr += 1
    #  else:
    #    break
  #bases will be if list is 0 or 1 since then we dont have to divide it
    if len(mylist) == 0:#if list is empty, 
      return Result(0, 0, 0, False) #left right and total r 0 and thus key is not found
    elif len(mylist) == 1: #if theres only 1 item
      if mylist[0] == key: #and that one item is the key
        return Result(1, 1, 1, True)#left right & total are 1 elem and key is elem
      else: #otherwise the 1 elem is not the key
        return Result(1, 1, 1, False)#left right & total are 1 but key isn't elem
    #start of recursive case
    else:
      halves = len(mylist) // 2 #divide it in half
      left = longest_run_recursive(mylist[:halves], key)#left is the first hlf
      right = longest_run_recursive(mylist[halves:], key)#right is second half
      
      if mylist[halves] == mylist[halves-1] == key: #if both halves are the same and key
        whole = left.left_size + right.right_size#total is both sizes together
        is_entire_range = left.is_entire_range and right.is_entire_range #"
        
      else:#otherwise
        if left.longest_size > right.longest_size:#if left has more keys in a row
          whole = left.longest_size#the total is lefts longest chain
        else:#otherwise right has more keys
          whole = right.longest_size#and we return the right sides longest
        is_entire_range = False#saying that the entire thing is not the keys
      return Result(left.left_size, right.right_size, whole, is_entire_range)
      #use Results to return the answer

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
    assert longest_run([8, 6, 7, 9, 8, 8, 10, 2], 8) == 2
    assert longest_run([1, 2, 2, 3, 4, 5, 5, 5, 5, 6], 5) == 4


