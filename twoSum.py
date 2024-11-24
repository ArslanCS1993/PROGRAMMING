def twoSum(nums, target):
    storage = {}
    for index, number in enumerate(nums):
        complement = target - number
        if complement in storage:
            return [storage[complement], index]
        storage[number] = index
    return None
