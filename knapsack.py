def knapsack(weights, values, capacity):
    n = len(weights)
    # Create a 2D array to store the max value at each n and capacity
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the dp table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Max of including or excluding the item
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                # Item can't be included
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# Example usage
weights = [1, 3, 4, 5]
values = [10, 40, 50, 70]
capacity = 8

max_value = knapsack(weights, values, capacity)
print("Maximum value in Knapsack:", max_value)
