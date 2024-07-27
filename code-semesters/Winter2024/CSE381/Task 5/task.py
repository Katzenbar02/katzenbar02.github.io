def tallest_tower_height(blocks):
    n = len(blocks)

    # Sort the blocks in non-increasing order of their dimensions
    blocks.sort(reverse=True)

    # Initialize the dp table with the height of each block as the base case
    dp = [block[1] for block in blocks]

    # Dynamic programming to find the maximum height
    for i in range(1, n):
        for j in range(i):
            # Check the conditions for stacking block i on top of block j
            if (blocks[i][0] < blocks[j][0] and blocks[i][2] < blocks[j][2]) or \
               (blocks[i][0] < blocks[j][2] and blocks[i][2] < blocks[j][0]):
                dp[i] = max(dp[i], dp[j] + blocks[i][1])

    # Return the maximum height of the towers
    return max(dp)

# Example usage:
blocks = [(1, 2, 3), (3, 2, 1), (2, 3, 4), (4, 3, 2)]
result = tallest_tower_height(blocks)
print("Maximum tower height:", result)
