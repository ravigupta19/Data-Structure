n = int(input())
def numFriendsGreeted(a,b,max):
    count = 0
    for i in range(a,max+1,b):
        count += 1
    return count
for _ in range(n):
    user_input = list(map(int, input().split()))
    print(user_input)
    print(numFriendsGreeted(user_input[0],user_input[1],user_input[2]))

