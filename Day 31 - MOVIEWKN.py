# cook your dish here
def choose_movie():
    import sys
    
    input = sys.stdin.read
    data = input().strip().splitlines()
    
    T = int(data[0])
    results = []
    index = 1
    
    for _ in range(T):
        n = int(data[index])
        lengths = list(map(int, data[index + 1].split()))
        ratings = list(map(int, data[index + 2].split()))
        
        best_index = -1
        max_value = -1
        max_rating = -1
        
        for i in range(n):
            current_value = lengths[i] * ratings[i]
            current_rating = ratings[i]
            
            if (current_value > max_value or
                (current_value == max_value and current_rating > max_rating) or
                (current_value == max_value and current_rating == max_rating and (best_index == -1 or i < best_index))):
                max_value = current_value
                max_rating = current_rating
                best_index = i
        
        results.append(best_index + 1)  # Convert to 1-based index
        index += 3  # Move to the next test case
    
    for result in results:
        print(result)

# Call the function to execute
choose_movie()
