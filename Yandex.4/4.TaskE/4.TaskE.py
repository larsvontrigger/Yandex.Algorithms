
numofblocks = int(input())
blocks = []
for _ in range(numofblocks):
    wid, hit = map(int, input().split())
    blocks.append((wid, hit))

# Sort blocks: first by width ascending, then by height descending if widths are equal
blocks.sort(key=lambda x: (x[0], -x[1]))

dp = [0] * numofblocks

# Initialize DP array with the heights of each block
for i in range(numofblocks):
    dp[i] = blocks[i][1]

# Calculate the maximum height for each block
for i in range(1, numofblocks):
    for j in range(i):
        if blocks[i][0] > blocks[j][0]:
            dp[i] = max(dp[i], dp[j] + blocks[i][1])


max_height = max(dp)
print(max_height)
