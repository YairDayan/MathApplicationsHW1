##### 3 #####

def index_of(n, s):
    # Initialize a list to store the indices of the number in the ID
    arr = []
    # Convert num and id to strings for comparison
    n = str(n)
    s = str(s)

    # Iterate through each character in the ID
    for j in range(len(s)):
        # If the current character matches the number, add the index to the list
        if s[j] == n:
            arr.append(j)

    # Return the list of indices if found, otherwise return an empty list
    if len(arr) == 0:
        return []
    else:
        return arr


ids = input("Enter your ID: ")
number = input("Enter the number: ")
print(index_of(number, ids))
