def max_length_smallest_highest_value_sequence(data):
    # Define a custom key function for the max function
    def custom_key(item):
        length, sequence = item
        return (length, -sequence[0])  # Tuple for comparison, negate the value

    # Find the item with the maximum length and smallest highest value
    max_item = max(data, key=custom_key)

    return max_item[0], max_item[1]  # Return the sequence

# Example usage:
data = [[4, [4, 3, 2, 1]], [4, [20, 3, 4, 5]]]
max_length, result_sequence = max_length_smallest_highest_value_sequence(data)
print(max_length)
print(result_sequence)