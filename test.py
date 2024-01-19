# nums=[3,3]
# target=6
# nums.sort()
# output=[]


# if target %2!=0:
#     all=[-1 for x in range(0,target+1)]
#     for i in range(0,len(nums)):
#         if nums[i]<target :
#             all[nums[i]]=i
#     for i in range(0,int(target/2)):
#         if all[i]!=-1 and all[target-i]!=-1:
#             output.append(all[i])
#             output.append(all[target-i])
#     print (output)

# else :
#     half=-1;
#     all=[-1 for x in range(0,target+1)]
#     for i in range(0,len(nums)):
#         if nums[i]<target:
#             all[nums[i]]=i
#     output=[]
#     for i in range(0,int(target/2)):
#         if all[i]!=-1 and all[target-i]!=-1:
#             output.append(all[i])
#             output.append(all[target-i])
#     if len(output)==2:
#         print (output)
#     else :
#         for i in range(0,len(nums)):
#             if nums[i]==int(target/2):
#                 output.append(i)
#         print (output)



nums=[3,3]
res_nums=sorted(nums)
print(res_nums)

for i in range(0,len(nums)-2):
    print (i)
    if res_nums[i]==res_nums[i+1] : print (1)
print (0)
