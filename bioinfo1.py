# def patterncountt(text):
#     count = 0
#     k = 2
#     dict = {}

#     for j in range(len(text) - k + 1):
#         for i in range(len(text) - k + 1):
#             if text[j:j + 2] == text[i:i + 2]:
#                 count = count + 1
#                 cle = text[j:j + 2]
#                 dict[cle] = count
#         count = 0
#     return max(dict, key=dict.get)


# print(patterncountt("GATCCAGATCCCCATAC"))





def MostFrequentKMer(Text, k):
    # Dictionary to store k-mer counts
    kmer_counts = {}
    
    # Iterate through the text to extract all k-mers
    for i in range(len(Text) - k + 1):
        kmer = Text[i:i+k]  # Extract k-mer
        if kmer in kmer_counts:
            kmer_counts[kmer] += 1  # Increment count if k-mer already exists
        else:
            kmer_counts[kmer] = 1  # Initialize count for new k-mer
    
    # Find the maximum count
    max_count = max(kmer_counts.values())
    
    # Find all k-mers with the maximum count
    most_frequent_kmers = [kmer for kmer, count in kmer_counts.items() if count == max_count]
    
    return most_frequent_kmers, max_count

# Test case: Find the most frequent 2-mer in the given text
text = "GATCCAGATCCCCATAC"
k = 2
result, count = MostFrequentKMer(text, k)
print(f"The most frequent {k}-mer(s): {result}, appearing {count} times.")

# The most frequent 2-mer(s): ['CC'], appearing 4 times.

