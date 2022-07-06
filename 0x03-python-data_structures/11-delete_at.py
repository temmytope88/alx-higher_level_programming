#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
  new_list = []
  if idx < 0 or idx >= (len(my_list)):
    return my_list
  else:
    for x in range (len(my_list)):
      if x == idx:
        continue;
      new_list.append(my_list[x])
  my_list = new_list 
  return my_list
my_list = [1, 2, 3, 4, 5]
idx = 3  
new_list = delete_at(my_list, idx)
print(my_list)

      