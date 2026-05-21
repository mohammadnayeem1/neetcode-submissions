class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        goal = Counter(s1)
        window = Counter()
        window_size = len(s1)  # The window length should match s1's length

        for r in range(len(s2)):
            window[s2[r]] += 1  # Add current character to the window

            # Remove the character that's out of the window (left side) if window size exceeds s1's length
            if r >= window_size:
                left_char = s2[r - window_size]
                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char]

            # Check if current window matches the goal
            if window == goal:
                return True

        return False
