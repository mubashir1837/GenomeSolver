# Problem: Frequency Map of k-mers
# You are given a string Text and an integer k. Your task is to write a function FrequencyMap() that generates a frequency map of all possible substrings (k-mers) of length k appearing in the string Text.

# Input:
# A string Text of length n (1 ≤ n ≤ 10^6).
# An integer k (1 ≤ k ≤ n).
# Output:
# A dictionary where the keys are all distinct k-mers of length k in the string Text and the values are all initialized to 0.


def FrequencyMap(Text, k):
    freq = {}
    
    # Loop through each substring of length k in the Text
    for i in range(len(Text) - k + 1):
        k_mer = Text[i:i + k]
        
        # If the k-mer is not in the dictionary, initialize its value to 0
        if k_mer not in freq:
            freq[k_mer] = 0
            
    return freq

# Test the function with the example input
Text = "CGATATATCCATAG"
k = 3
print(FrequencyMap(Text, k))
# Output: {'CGA': 0, 'GAT': 0, 'ATA': 0, 'TAT': 0, 'ATC': 0, 'TCC': 0, 'CCA': 0, 'CAT': 0, 'TAG': 0}

Text = "ATCATTGGA"
k = 3
result = FrequencyMap(Text, k)
print(result)

Text = "GATCCAGATCCCCATAGGATCCAGATCCCCATAC"
k = 2
result = FrequencyMap(Text, k)
print(result)

# The function correctly generates a frequency map with all distinct k-mers of length k in the given string Text, with their values initialized to 0.

