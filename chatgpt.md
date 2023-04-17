# First use 

## we tried to use it to calculate the score the result is not good so we build it from scratch

## prompt : 
```
i have dictionary with key and value i need to get count where value =2
``` 

## output code

```
my_dict = {"a": 1, "b": 2, "c": 2, "d": 3, "e": 4, "f": 4}

count = 0
for value in my_dict.values():
    if value == 2:
        count += 1
print("Number of values that occur exactly twice in the dictionary:", count)

```