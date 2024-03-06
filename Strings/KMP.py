def compute_prefix_function(pattern):
    m = len(pattern)
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = pi[k - 1]
        if pattern[k] == pattern[q]:
            k = k + 1
        pi[q] = k
    return pi

def kmp(text, pattern):
    n = len(text)
    m = len(pattern)
    occurrences = []

    pi = compute_prefix_function(pattern)
    q = 0
    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q - 1]
        if pattern[q] == text[i]:
            q = q + 1
        if q == m:
            occurrences.append(i - m + 1)
            q = pi[q - 1]
    return occurrences

# Example usage:
text = "abracadabra"
pattern = "abra"
print("Occurrences:", kmp(text, pattern))
