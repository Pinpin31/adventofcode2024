lst = []
safe = 0

def strictly_increasing_with_interval(lst, interval):
    prev_val = None

    for val in lst:
        if prev_val is not None:
            if val - prev_val > interval or val - prev_val < 1:
                return False
        prev_val = val
    
    print("increase")
    return True

def strictly_decreasing_with_interval(lst, interval):
    prev_val = None

    for val in lst:
        if prev_val is not None:
            if prev_val - val > interval or prev_val - val < 1:
                return False
        prev_val = val

    print("decrease")
    return True


def strictly_monotonic_with_interval(lst):
    return strictly_increasing_with_interval(lst,3) or strictly_decreasing_with_interval(lst,3)

def is_safe(lst):
    return strictly_monotonic_with_interval(lst)

with open("day2.input") as file:
    for line in file:
        print(line)
        lst = list(map(int,line.split()))
        if is_safe(lst):
            safe += 1
        else:
          for i in range(len(lst)):
              new_lst = lst.copy()
              new_lst.pop(i)
              print(new_lst)
              if is_safe(new_lst):
                  safe +=1
                  continue
print(safe)

