name = ["a", "b", "c", "d", "e"]
profit = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [100, 11, 12], [13, 14, 15]]

def best_store(names, profits):
    max_name = ""  # Store with the highest profit
    max_profit = 0  # Highest profit value

    # Loop through stores to calculate total profit and find the maximum
    for i in range(len(names)):
        total_profit = sum(profits[i])  # Calculate total profit for the current store
        if total_profit > max_profit:  # Check if it's bigger than the current maximum profit
            max_name = names[i]       # Update the store name
            max_profit = total_profit # Update the maximum profit value

    return max_name, max_profit

print(best_store(name, profit))