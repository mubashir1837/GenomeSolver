# #To find the most frequent k-mers in a string Text, we would like to create a mapping like the example below for Text equal to "CGATATATCCATAG" and k equal to 3, where we map each k-mer appearing in  Text to its number of occurrences in  Text.  We call this structure a frequency map; once we have constructed a frequency map given  Text and k, we will be able to find the most frequent word  by finding the k-mer whose number of occurrences achieves a maximum.

# ATA --> 3
# ATC --> 1
# CAT --> 1
# CCA --> 1
# CGA --> 1
# GAT --> 1
# TAT --> 2
# TCC --> 1
# TAG --> 1
# Fortunately, Python allows us to easily implement a frequency map by providing a built-in data structure called a dictionary.  You can think of a dictionary as a set of keys (first column in the figure above), where each key refers to a value (second column in the figure above). You can learn about dictionaries (and a related structure called a list) in the following exercises.

Text = "CGATATATCCATAG"
k = 3
kmer_counts = {}
for i in range(len(Text) - k + 1):
    kmer = Text[i:i+k]
    if kmer in kmer_counts:
        kmer_counts[kmer] += 1
    else:
            kmer_counts[kmer] = 1
print(kmer_counts)
# Output: {'CGA': 1, 'GAT': 1, 'ATA': 3, 'TAT': 2, 'ATC': 1, 'TCC': 1, 'CCA': 1, 'CAT': 1, 'TAG': 1}
