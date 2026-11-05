# Que-1
# n=5
# for i in range(n):
#     print (i+1)


# Que-
# n=5
# i=n
# for i in range(n-1,-1,-1):
#     print(i+1)

# Que-3
# n=5
# sum=0
# for i in range(n+1):
#     sum+=i
# print(sum)
    
# Que-4
# n=6
# sum=0
# for i in range(n+1):
#     if i%2==0:
#         sum+=i
# print(sum)

# Que-5
# n=3
# for i in range(11):
#     print(n*i)

# s,w,2,x 

# Que-6
# n=54321
# digit=0
# while n>0:
#     digit+=1
#     n=n//10
# print(digit)

# Que-7
# n=1234
# sum=0
# for digit in str(n):
#     sum+=int(digit)
# print(sum)

# que-8
# n=1234
# print(str(n)[::-1])

# Que-9
# n=1221
# if(str(n)==str(n)[::-1]):
#     print("True")
# else:
#     print("False")

# Que-10
# n=8343
# a=str(n)
# print("last digit:",a[-1])
# print("First digit:",a[0])

# Que-11
# base = 2
# exp = 4
# print(exp**base)

# Que-12
# n=5
# fac=1
# for i in range(n):
#     fac*=i+1
# print(fac)

# Que-13
# import math
# a=12
# b=18
# print(math.gcd(a,b))


# s,w,2,x 

# Que-14
# import math 
# a=4
# b=6
# print(math.lcm(a,b))

# Que-15
# n=17
# for i in range(2,n):
#     if n%i==0:
#         print("Not Prime")
#         break
# else:
#     print("Prime")

# Que-16
# n=15
# for i in range(2,n):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)

# que-17
# n=153
# a=str(n)
# sum=0
# for digit in a:
#     sum+=int(digit)**len(a)
# if sum==n:
#     print("True")
# else:
#     print("False")

# Que-18
# n=6
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==n:
#     print("True")
# else:
#     print("False")

# Que-19
# n=1101
# print(int(str(n),2))

# Que-20
# n=13
# a=bin(n)[2:]
# print(a)

# Que-21
# n=3
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     print() 

# Que-22
# n=3
# for i in range(n-1,-1,-1):
#     for j in range(i+1):
#         print("*",end="")
#     print()

# Que-23
# n=3
# for i in range(n):
#     for j in range(2*n-1):
#         if j>=n-1-i and j<=n-1+i:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# Que-24
# n=3
# for i in range(n):
#     for j in range(2*n-1):
#         if j>=n-1-i and j<=n-1+i:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
# for i in range(n-2,-1,-1):
#     for j in range(2*n-1):
#         if j>=n-1-i and j<=n-1+i:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# Que-25
# n=3
# for i in range(n):
#     for j in range(i+1):
#         print(j+1,end="")
#     print()

# Que-26
# n=3
# char=1
# for i in range(n):
#     for j in range(i+1):
#         print(char,end="")
#         char+=1
#     print()

# Que-27
# n=4
# for i in range(n+1):
#     row=[1]*(i+1)
#     for j in range(1,i):
#         row[j]=prev_row[j-1]+prev_row[j]
#     print(row)
#     prev_row=row

# Que-28
# s,w,2,x 
# n=3
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# Que-29
# n=3
# for i in range(n):
#     for j in range(n):
#         if i==j or i+j==n-1:
#             print("1",end="")
#         else:
#             print("0",end="")
#     print()

# Que-30
# n=6
# def fibonacci(n):
#     if(n==0):
#         return 0
#     elif(n==1):
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# print("Fibonacci series:")
# for i in range(n):
#     print(fibonacci(i), end=" ")

# Que-31
# n=7
# def fibonacci(n):
#     if(n==0):
#         return 0
#     elif(n==1):
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# print("end Fibonacci number is:", fibonacci(n))

# Que-32
# n=6
# def collatz(n):
#     print(n, end=" ")
#     if n == 1:
#         return
#     elif n % 2 == 0:
#         collatz(n // 2)
#     else:
#         collatz(3 * n + 1)
# collatz(n)

# Que-33
# n=3
# sum=0
# for i in range(1,n):
#     sum+=1/i
# print(sum)


# s,w,2,x 


# Que-34
# N=3
# for i in range(2*N-1):
#     for j in range(2*N-1):
#         if i< N:
#             if j>=i and j<2*N-1-i:
#                 print("*",end="")
#             else:
#                 print(" ",end="")
#         else:
#             if j>=2*N-1-i-1 and j<=i:
#                 print("*",end="")
#             else:
#                 print(" ",end="") 
#     print()

# Que-35
# n=145
# sum=0
# def factorial(a):
#     fact=1
#     for i in range(2,a+1):
#         fact*=i
#     return fact
# while n>0:
#     digit=n%10
#     sum+=factorial(digit)
#     n=n//10
# print(sum)



# section-3

# Que-36
# a=[1,2,3,4,5]
# sum=0
# avg=0
# for i in range(len(a)):
#     sum+=a[i]
# avg=sum/len(a)
# print("Sum:",sum)
# print("Average:",avg)

# Que-37
# a=[4,9,1,7,3]
# min=a[0]
# max=a[0]
# for i in range(len(a)):
#     if a[i]<min:
#         min=a[i]
#     if a[i]>max:
#         max=a[i]
# print("Minimum:",min)
# print("Maximum:",max)

# Que-38
# a=[1,35,1,10,34,1]
# first=a[0]
# second=a[0]
# for i in range(len(a)):
#     if a[i]>first:
#         second=first
#         first=a[i]
#     elif a[i]>second and a[i]!=first:
#         second=a[i]
# print("Second largest:",second)


# Que-39
# a=[1,2,3,4,5,6]
# even_count=0
# odd_count=0
# for i in range(len(a)):
#     if a[i]%2==0:
#         even_count+=1
#     else:
#         odd_count+=1
# print("Even :",even_count)
# print("Odd :",odd_count)

# Que-40
# a=[-1, 2, 0, -3, 5, 0]
# neg=0
# pos=0
# zero=0
# for i in range(len(a)):
#     if a[i]<0:
#         neg+=1
#     elif a[i]>0:
#         pos+=1
#     else:
#         zero+=1 
# print("Negative:",neg)
# print("Positive:",pos)
# print("Zero:",zero)

# Que-41
# a= [1, 2, 3, 4]
# print(list(reversed(a)))

# Que-42
# a=[10, 20, 30]
# b=a.copy()
# print(b)

# Que-43
# a=[1, 2,4,5]
# X=3
# K=2
# a.insert(K,X)
# print(a)

# Que-44
# a=[10, 20, 30, 40]
# K=1
# a.pop(K)
# print(a)

# Que-45
# a=[1,2,2,3,1,4]
# dict={}
# for i in a:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# print(dict)

# Que-46
# a=[1,2,2,3,4,4]
# dict={}
# for i in a: 
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# arr=[]
# for key,value in dict.items():
#     if(value==1):
#         arr.append(key)
# print(arr)
    
# que-47
# a= [1, 1, 2, 2, 3]
# dict={}
# for i in a:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# arr=[]
# for key,value in dict.items():
#         arr.append(key)
# print(arr)
# print(len(arr))

# Que-48
# a=[4, 2, 7, 1]
# X = 5
# for i in a:
#     if i==X:
#         index=a.index(i)
#         break
# else:
#     index=-1
# print("Index:",index)


# s,w,2,x
# Que-49
# a=[1, 3, 5, 7, 9]
# tar=7
# st=0
# end=len(a)-1
# while st<=end:
#     mid=(st+end)//2
#     if a[mid]==tar:
#         print("Found at index:",mid)
#         break
#     elif a[mid]<tar:
#         st=mid+1
#     else:
#         end=mid-1
# else:
#     print("Not Found")

# Que-50
# a=[5, 1, 4, 2, 8]
# for i in range(len(a)):
#     for j in range(0, len(a)-i-1):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
# print("Sorted array using bubble sort:", a)

# Que-51
# a=[64, 25, 12, 22, 11]
# for i in range(len(a)): 
#     min_idx = i 
#     for j in range(i+1, len(a)): 
#         if a[j] < a[min_idx]: 
#             min_idx = j 
#     a[i], a[min_idx] = a[min_idx], a[i]
# print("Sorted array using selection sort:", a)

# Que-52
# a=[12, 11, 13, 5, 6] 
# for i in range(1, len(a)):
#     key = a[i]
#     j = i-1
#     while j >=0 and key < a[j] :
#             a[j + 1] = a[j]
#             j -= 1
#     a[j + 1] = key
# print("Sorted array using insertion sort:", a)


# que-53
# a=[1, 2, 3, 4, 5]
# K=2
# first=a[:K]
# second=a[K:]
# result=second+first
# print("Array after left rotation:",result)

# Que-54
# a=[1, 2, 3, 4, 5]
# K=2
# first=a[-K:]
# second=a[:-K]
# result=first+second
# print("Array after right rotation:",result)

# Que-55
# a=[1,2,3,4,5] 
# for i in range(1,len(a)-1):
#     if a[i]>a[i-1]:
#         continue
#     else:
#         print("False")
#         break
# else:
#     print("True")

# Que-56
# a=[1,2,4,5,6]
# n=6
# for i in range(1,n+1):
#     if i not in a:
#         print("Missing number:",i)
#         break   

# que-57
# a= [4, 1, 2, 1, 2]
# dict={}
# for i in a:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# for key,value in dict.items():
#     if value==1:
#         print("First non-repeating element:",key)
#         break

# Que-58
# a=[3,1,3]
# dict={}
# for i in a :
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# max_freq=0
# for key,value in dict.items():
#     if value>max_freq:
#         max_freq=value
#         element=key
# print("Most frequecy vala element:",element)

# Que-59
# a= [1, 2, 3, 4, 5, 6] 
# arr=[]
# for i in a:
#     if i%2==0:
#         arr.append(i)
# for i in a:
#     if i%2!=0:
#         arr.append(i)
# print(arr)

# Que-60
# arr1=[1,3,5]
# arr2=[2,4,6]
# answer=arr1+arr2
# answer.sort()
# print(answer)

# Que-61
# a= [2, 7, 11, 15]
# tar=9
# dict={}
# ans=[]
# for i in range(len(a)):
#     needed=tar-a[i]
#     if needed in dict:
#         ans.append(dict[needed])
#         ans.append(i)
#         break
#     dict[a[i]]=i
# print(ans)

# Que-62
# a= [-1, 0, 1, 2, -1, -4]
# ans=[]
# a.sort()
# first=a[-1]
# second=a[-1]
# for i in range(len(a)-2):
#     if i>0 and a[i]==a[i-1]:
#         continue
#     left=i+1
#     right=len(a)-1
#     while left<right:
#         sum=a[i]+a[left]+a[right]
#         if sum==0:
#             ans.append([a[i],a[left],a[right]])
#             while left<right and a[left]==a[left+1]:
#                 left+=1
#             while left<right and a[right]==a[right-1]:
#                 right-=1
#             left+=1
#             right-=1
#         elif sum<0:
#             left+=1
#         else:
#             right-=1
# print(ans)

# Que-63
# a=[0, 1, 0, 3, 12]
# ans=[]
# for i in range(len(a)):
#     if a[i]!=0:
#         ans.append(a[i])
# for i in range(len(a)-len(ans)):
#     ans.append(0)
# print(ans)

# que-64
# a=[0,1,1,0,1,0]
# ans=[]
# zero=a.count(0)
# one=a.count(1)
# ans=[0]*zero+[1]*one
# print(ans)

# que-65
# a= [2, 0, 2, 1, 1, 0]
# zero=a.count(0)
# one=a.count(1)
# two=a.count(2)
# ans=[0]*zero+[1]*one+[2]*two
# print(ans)

# que-66
# a=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
# max_sum=a[0]
# current_sum=a[0]
# for i in range(1,len(a)):
#     current_sum=max(a[i],current_sum+a[i])
#     max_sum=max(max_sum,current_sum)
# print("Maximum subarray sum:",max_sum)

# Que-67
# a=[2, 3, -2, 4]
# max_product=a[0]
# current_max=a[0]
# current_min=a[0]
# for i in range(1,len(a)):
#     if a[i]<0:
#         current_max,current_min=current_min,current_max
#     current_max=max(a[i],current_max*a[i])
#     current_min=min(a[i],current_min*a[i])
#     max_product=max(max_product,current_max)
# print("Max product subarray:",max_product)

# que-68
# a = [7, 1, 5, 3, 6, 4]
# min_price = a[0]
# max_profit = 0
# for i in range(1, len(a)):
#     if a[i] < min_price:
#         min_price = a[i]
#     else:
#         profit = a[i] - min_price
#         max_profit = max(max_profit, profit)
# print("Maximum profit:", max_profit)

# que-69
# a= [7, 1, 3, 5, 6, 4]
# min_price=a[0]
# total_profit=0
# for i in range(1, len(a)):
#     if a[i]<min_price:
#         min_price=a[i]
#     else:
#         profit=a[i]-min_price
#         total_profit+=profit
#         min_price=a[i]
# print("Total profit:",total_profit)


# que-70
# a= [1, 2, 3,4,1, 1]
# peak=a[0]
# for i in range(1,len(a)):
#     if a[i]>a[i-1] and a[i]>a[i+1]:
#         peak=a[i]
# print(peak)

# que-71
# a = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# def trap(height):
#     if not height:
#         return 0
#     left, right = 0, len(height) - 1
#     left_max, right_max = height[left], height[right]
#     water = 0
#     while left < right:
#         if left_max < right_max:
#             left += 1
#             left_max = max(left_max, height[left])
#             water += left_max - height[left]
#         else:
#             right -= 1
#             right_max = max(right_max, height[right])
#             water += right_max - height[right]
#     return water
# print(trap(a)) 

# que-72
# a = [2, 1, 5, 1, 3, 2]
# K = 3
# def max_sum_subarray(arr, K):
#     if len(arr) < K:
#         return 0    
#     window_sum = sum(arr[:K])
#     max_sum = window_sum    
#     for i in range(len(arr) - K):
#         window_sum = window_sum - arr[i] + arr[i + K]
#         max_sum = max(max_sum, window_sum)
#     return max_sum

# print(max_sum_subarray(a, K))  

# Que-73
# a= [12, -1, -7, 8, -15, 30, 16, 28]
# K = 3 
# from collections import deque
# def first_negative_in_window(arr, k):
#     q = deque()  
#     result = []    
#     for i in range(k):
#         if arr[i] < 0:
#             q.append(i)            
#     result.append(arr[q[0]] if q else 0)        
#     for i in range(k, len(arr)):
#         if q and q[0] <= i - k:
#             q.popleft()            
#         if arr[i] < 0:
#             q.append(i)            
#         result.append(arr[q[0]] if q else 0)
#     return result
# print(first_negative_in_window(a, K))


# Que-74
# a= [-7, 1, 5, 2, -4, 3, 0] 
# for i in range(1, len(a)): 
#     left = a[:i]
#     right = a[i+1:]
#     if sum(left) == sum(right):
#         print(f"equilibrium index found at: {i}")
#         break

# Que-75
# a=[16, 17, 4, 3, 5, 2]
# def find_leaders(arr):
#     size = len(arr)
#     if size == 0:
#         return []        
#     max_from_right = arr[size - 1]
#     leaders = [max_from_right]    
#     for i in range(size - 2, -1, -1):
#         if arr[i] >= max_from_right:
#             max_from_right = arr[i]
#             leaders.append(max_from_right)            
#     leaders.reverse()
#     return leaders

# ans = find_leaders(a)
# print(ans)  

# que-76
# a = [100, 4, 200, 1, 3, 2]
# def longest_sequence(nums):
#     if not nums:
#         return 0
#     nums.sort()
#     longest = 1
#     current_streak = 1
#     for i in range(1, len(nums)):
#         if nums[i] == nums[i-1]:
#             continue
#         if nums[i] == nums[i-1] + 1:
#             current_streak += 1
#         else:
#             if current_streak > longest:
#                 longest = current_streak
#             current_streak = 1
#     if current_streak > longest:
#         longest = current_streak
#     return longest

# ans = longest_sequence(a)
# print(ans)


# Que-78
# a = [1, 2, 3, 4]
# def product_except_self(nums):
#     length = len(nums)
#     ans = [1] * length
#     left = 1
#     for i in range(length):
#         ans[i] = left
#         left *= nums[i]
#     right = 1
#     for i in range(length - 1, -1, -1):
#         ans[i] *= right
#         right *= nums[i]
#     return ans

# ans = product_except_self(a)
# print(ans)

# Que-79
# arr = [1, 1, 1]
# def subarray_sum(nums, k):
#     count = 0
#     curr_sum = 0
#     prefix_sums = {0: 1}
#     for num in nums:
#         curr_sum += num
#         if (curr_sum - k) in prefix_sums:
#             count += prefix_sums[curr_sum - k]
#         prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
#     return count

# K = 2
# ans = subarray_sum(arr, K)
# print(ans)

# Que-80
# a = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# def max_area(height):
#     left = 0
#     right = len(height) - 1
#     max_water = 0
#     while left < right:
#         width = right - left
#         current_water = min(height[left], height[right]) * width
#         if current_water > max_water:
#             max_water = current_water
#         if height[left] < height[right]:
#             left += 1
#         else:
#             right -= 1
#     return max_water

# ans = max_area(a)
# print(ans)

# section-5

# que-81
# a=[[1, 2], [3, 4]]
# sum=0
# for i in range(len(a)):
#     for j in range(len(a[0])):
#         sum+=a[i][j]
# print(sum)

# Que-82
# A = [[1, 2], [3, 4]]
# B = [[5, 6], [7, 8]]
# C = []
# for i in range(len(A)):
#     row = []
#     for j in range(len(A[0])):
#         row.append(A[i][j] + B[i][j])
#     C.append(row)
# print(C)

# Que-83
# A = [[1, 2], [3, 4]]
# B = [[1, 0], [0, 1]]
# C=[]
# for i in range(len(A)):
#     row = []
#     for j in range(len(B[0])):
#         total = 0
#         for k in range(len(B)):
#             total += A[i][k] * B[k][j]
#         row.append(total)
#     C.append(row)
# print(C)

# Que-84
# A = [[1, 2, 3],
#      [4, 5, 6]]
# result = []
# for i in range(len(A[0])):
#     row = []
#     for j in range(len(A)):
#         row.append(A[j][i])
#     result.append(row)
# print(result)

# Que-85
# A = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# n = len(A)
# main_sum = 0
# anti_sum = 0
# for i in range(n):
#     main_sum += A[i][i]
#     anti_sum += A[i][n - 1 - i]
# print("Main =", main_sum)
# print("Anti =", anti_sum)

# Que-86
# A=[[1, 2], [2, 1]]
# a=A[0]
# a1=A[1]
# if list(reversed(a))==a1:
#     print("True")
# else:
#     print("False")

# Que-87
# A=[[1,0],[0,1]]
# n=len(A)
# is_identity=True
# for i in range(n):
#     for j in range(n):
#         if i==j and A[i][j]!=1:
#             is_identity=False
#         elif i!=j and A[i][j]!=0:
#             is_identity=False
# print(is_identity)

# Que-88
# A=[[1,2],[3,4]]
# B=[]
# C=[]
# N=len(A)
# for i in range(N):
#     total=0
#     for j in range(len(A[0])):
#         total+=A[i][j]
    
#     B.append(total)
# for j in range(len(A[0])):
#     total=0
#     for i in range(len(A)):
#         total+=A[i][j]
#     C.append(total)
# print(B)
# print(C)

# Que-89
# A=[[1, 2], [3, 4]]
# n=len(A)
# for i in range(n):
#     for j in range(i+1,n):
#         A[i][j],A[j][i]=A[j][i],A[i][j]
# for i in range(n):
#     A[i].reverse()
# print(A)

# Que-90
# A=[[1, 2], [3, 4]]
# n=len(A)
# for i in range(n):
#     for j in range(i+1,n):
#         A[i][j],A[j][i]=A[j][i],A[i][j]
# for j in range(n):
#     for i in range(n//2):
#         A[i][j],A[n-1-i][j]=A[n-1-i][j],A[i][j]
# print(A)

# Que-91
# A=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# B=[]
# while A:
#     B+=A.pop(0)
#     if A and A[0]:
#         for row in A:
#             B.append(row.pop())
#     if A:
#         B+=A.pop()[::-1]
#     if A and A[0]:
#         for row in A[::-1]:
#             B.append(row.pop(0))
# print(B)

# Que-92
# A= [[1, 4, 7], 
#     [2, 5, 8],
#     [3, 6, 9]]
# tar=5
# i=0
# j=len(A[0])-1
# while i<len(A) and j>=0:
#     if A[i][j]==tar:
#         print("Found at",(i,j))
#         break
#     elif A[i][j]>tar:
#         j-=1
#     else:i+=1
# else:
#     print("Not found")

# Que-93
# A = [[1, 1, 1],
#      [1, 0, 1],
#      [1, 1, 1]]
# row=set()
# col=set()
# for i in range(len(A)):
#     for j in range(len(A[0])):
#         if A[i][j]==0:
#             row.add(i)
#             col.add(j)
# for i in range(len(A)):
#     for j in range(len(A[0])):
#         if i in row or j in col:
#             A[i][j]=0
# print(A)


# Que-94
# A=[[1,2,3],
#    [4,5,6],
#    [7,8,9]]
# r=len(A)
# c=len(A[0])
# for j in range(c):
#     print(A[0][j],end=" ")
# for i in range(1,r):
#     print(A[i][c-1],end=" ")
# for j in range(c-2,-1,-1):
#     print(A[r-1][j],end=" ")
# for i in range(r-2,0,-1):
#     print(A[i][0],end=" ")

# Que-95
# A=[[0,1,1],
#    [1,1,1],
#    [0,0,1]]
# max_count=0
# r=-1
# for i in range(len(A)):
#     count=0
#     for j in range(len(A[0])):
#         if A[i][j]==1:
#             count+=1
#     if count>max_count:
#         max_count=count
#         r=i
# print("Row",r)

# Que-96
# A=[[0,0,3],
#    [0,0,0],
#    [1,0,0]]
# count=0
# total=len(A)*len(A[0])
# for i in range(len(A)):
#     for j in range(len(A[0])):
#         if A[i][j]==0:
#             count+=1
# if count>total/2:
#     print(True)
# else:
#     print(False)

# Que-97
# A=[[1,2],
#    [3,4]]
# r=len(A)
# c=len(A[0])
# B=[]
# for a in range(r+c-1):
#     diagonal=[]
#     for i in range(r):
#         j=a-i
#         if j>=0 and j<c:
#             diagonal.append(A[i][j])
#     B.append(diagonal)
# print(B)

# Que-98
# A=[[1,2,3],
# [4,5,6],
# [7,8,9]]

# r=len(A)
# c=len(A[0])
# for i in range(r):
#     min_value=min(A[i])
#     j=A[i].index(min_value)
#     max_value=max(A[k][j] for k in range(r))
#     if min_value==max_value:
#         print(min_value)
#         break
# else:
#     print("No Saddle point")

# Que-99
# board=[
#     ["5","3",".",".","7",".",".",".","."],
#     ["6",".",".","1","9","5",".",".","."],
#     [".","9","8",".",".",".",".","6","."],
#     ["8",".",".",".","6",".",".",".","3"],
#     ["4",".",".","8",".","3",".",".","1"],
#     ["7",".",".",".","2",".",".",".","6"],
#     [".","6",".",".",".",".","2","8","."],
#     [".",".",".","4","1","9",".",".","5"],
#     [".",".",".",".","8",".",".","7","9"]]
# for i in range(9):
#     r=[]
#     c=[]
#     for j in range(9):
#         if board[i][j]!=".":
#             if board[i][j]in r:
#                 print(False)
#                 break
#             r.append(board[i][j])
#         if board[j][i]!=".":
#             if board[j][i] in c:
#                 print(False)
#                 break
#             c.append(board[j][i])
#     else:
#         continue
#     break
# else:
#     for i in range(0,9,3):
#         for j in range(0,9,3):
#             box=[]
#             for r in range(i,i+3):
#                 for c in range(j,j+3):
#                     if board[r][c]!=".":
#                         if board[r][c] in box:
#                             print(False)
#                             exit()
#                         box.append(board[r][c])
#     print(True)


# Que-100
# n=3
# A=[[0]*n for i in range(n)]
# num=1
# top=0
# bottom=n-1
# left=0
# right=n-1
# while num<=n*n:
#     for j in range(left,right+1):
#         A[top][j]=num
#         num+=1
#     top+=1
#     for i in range(top,bottom+1):
#         A[i][right]=num
#         num+=1
#     right-=1
#     if top<=bottom:
#         for j in range(right,left-1,-1):
#             A[bottom][j]=num
#             num+=1
#         bottom-=1
#     if left<=right:
#         for i in range(bottom,top-1,-1):
#             A[i][left]=num
#             num+=1
#         left+=1
# print(A)
        