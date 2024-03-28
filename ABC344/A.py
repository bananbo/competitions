def remove_between_pipes(s):
    # Find the indices of the two '|' characters
    first_pipe_index = s.index('|')
    second_pipe_index = s.index('|', first_pipe_index + 1)

    # Remove the characters between the '|' characters and the '|' characters themselves
    result = s[:first_pipe_index] + s[second_pipe_index + 1:]

    return result

# Example usage
s = input()
output = remove_between_pipes(s)
print(output)