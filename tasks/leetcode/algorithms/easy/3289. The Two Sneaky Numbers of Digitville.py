from collections import Counter
from typing import List

def getSneakyNumbers(nums: List[int]) -> List[int]:
    pset = set()
    answer = []
    for val in nums:
        if val in pset:
            answer.append(val)
        else:
            pset.add(val)
    return answer


nums = [7,1,5,4,3,4,6,0,9,5,8,2]
print(getSneakyNumbers(nums))