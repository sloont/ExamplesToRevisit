#finding the middle one (if odd) or two (if even) items in a list
#if odd number of items return middle item
#if even number of items return average of middle two

def middle_element(lst):
  if len(lst) % 2 == 0:
    one = int(len(lst) / 2 - 1)
    two = int(len(lst) / 2)
    x = (lst[one] + lst[two]) / 2
    return x
  else:
    one = int(len(lst) / 2 - 0.5)
    x = lst[one]
    return x

#sample data
print(middle_element([5, 2, -4, 4, 5]))
