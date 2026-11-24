# We need too return YES if we can divide and NO if not 
w = int(input())
 # we need to make sure that the divided parts need to be greater than 2
print("YES" if (w%2==0 and w>2) else "NO")

#Time Complexity: O(1)
#Space Complexity: O(1)

"""if (w%2==0 and w>2):
    print("YES")
else:
    print("NO")"""