def is_easy_to_pronounce(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    max_consonants = 0
    current_consonants = 0
    
    for char in s:
        if char not in vowels:
            current_consonants += 1
            if current_consonants >= 4:
                return "NO"
        else:
            current_consonants = 0
    
    return "YES"

def main():
    T = int(input())
    results = []
    
    for _ in range(T):
        N = int(input())
        S = input().strip()
        results.append(is_easy_to_pronounce(S))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()

