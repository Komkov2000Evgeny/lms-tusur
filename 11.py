#1
def fractional_number_generator(n):
    from random import uniform
    for _ in range(n):
        yield uniform(0,n)
        
print(list(fractional_number_generator(3)))

#2
from itertools import chain
print(list(chain([1, 2], [3, 4])))

#3
def responses_creator(item_ids):
    return [dict(item_id = item_id) for item_id in item_ids]
    
print(responses_creator([0,1,2,3]))