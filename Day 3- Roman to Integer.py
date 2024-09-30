class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Mapping of Roman symbols to their integer values
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        n = len(s)

        for i in range(n):
            current_value = roman_map[s[i]]
            
            # Check if there's a next symbol and apply the subtraction rule
            if i + 1 < n and roman_map[s[i + 1]] > current_value:
                total -= current_value  # Subtract current value
            else:
                total += current_value  # Add current value

        return total

# Example usage:
solution = Solution()
print(solution.romanToInt("III"))      # Output: 3
print(solution.romanToInt("LVIII"))    # Output: 58
print(solution.romanToInt("MCMXCIV"))  # Output: 1994
