from typing import List

def generate_flag_combinations(n: int) -> List[List[bool]]:
    if n == 0:
        return [[]]
    
    smaller_combinations = generate_flag_combinations(n - 1)
    combinations = []
    for combination in smaller_combinations:
        combinations.append(combination + [False])
        combinations.append(combination + [True])
    return combinations

def twoSum(nums: List[int], target: int) -> List[int]:
    maxIdx = len(nums)
    BoolArrArr = generate_flag_combinations(maxIdx)
    for boolArr in BoolArrArr:
        sum = 0
        resultIdx = []
        for i in range(maxIdx):
            if boolArr[i]:
                resultIdx.append(i)
                sum = sum + nums[i]
        if sum == target:
            return resultIdx