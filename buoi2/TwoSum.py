from array import *
nums = array('i', [2,6,3,9,11])

target = 9

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if(nums[i] + nums[j] == target):
            print('['+str(i)+','+str(j)+']')

