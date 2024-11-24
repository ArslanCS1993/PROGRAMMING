def isValid(s):
    # Initialize an empty list to use as a stack for tracking opening brackets
    stack = []

    # Create a mapping of closing brackets to their corresponding opening brackets
    mapping = {")": "(", "}": "{", "]": "["}

    # Iterate over each character in the input string 's'
    for char in s:
        # Check if the character is a closing bracket (exists in mapping)
        if char in mapping:
            # If the stack is not empty, pop the top element; otherwise, assign a placeholder '#'
            top_element = stack.pop() if stack else "#"

            # Check if the popped element matches the expected opening bracket for the current closing bracket
            if mapping[char] != top_element:
                # If it doesn't match, return False (the string is not valid)
                return False
        else:
            # If the character is an opening bracket, push it onto the stack
            stack.append(char)

    # After processing all characters, return True if the stack is empty (all brackets matched), otherwise return False
    return not stack


# initialize an empty list to track
