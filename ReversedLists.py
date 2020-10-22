# returns true if equal len lists are mirror images of each other(reversed)

def reversed_list(lst1, lst2):
  for i in range(len(lst1)):
    x = (i + 1)* -1
    if lst1[i] == lst2[x]:
      continue
    else:
      return False
      break
  return True

