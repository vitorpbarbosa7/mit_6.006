def create_hash_table(sequence):
    min_val = min(sequence)
    max_val = max(sequence)
    
    hash_table = {key: None for key in range(min_val, max_val + 1)}
    
    for num in sequence:
        hash_table[num] = num

    return hash_table

# Example
sequence = [4, 2, 7, 9, 1]
hash_table = create_hash_table(sequence)

print(hash_table)
