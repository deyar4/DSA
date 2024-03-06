# Brute-Force Approach (Algorithm 2.1)

def brute_force(T: str, P: str):
    occurrences = []
    i = 0

    while i <= len(T) - len(P):
        if T[i:i+len(P)] == P:
            occurrences.append(i + 1)  # Add 1 to convert 0-based index to 1-based index
        i += 1

    return occurrences


text = "abracadabra"
pattern = "abra"

occurrences = brute_force(text, pattern)

print("Occurrences of pattern in text:", occurrences)


