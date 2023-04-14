# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
        text = input()
        if 'I' in text:
            return (input().rstrip(), input().rstrip())
        elif 'F' in text:
            name1 = input()
            if not 'a' in name1: 
                name1 = "tests/"+name1
                try:
                    f = open(name1, "r")
                    pattern = f.readline().rstrip()
                    text = f.readline().rstrip()
                    return (pattern, text)
                except EOFError:
                    return None
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    #return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    prime = 997
    multiplier = 13

    def calculate_polynomial_hash(str, prime, multiplier):
        hash_value = 0
        i = len(str) - 1
        while i >= 0:
            x = str[i]
            hash_value = (hash_value * multiplier + ord(x)) % prime
            i -= 1

        return hash_value
    
    def precompute_substring_hashes(text, pattern_length, prime, multiplier):
        text_length = len(text)
        q = [0] * (text_length - pattern_length + 1)
        s = text[-pattern_length:]
        q[text_length - pattern_length] = calculate_polynomial_hash(s, prime, multiplier)
        y = 1
        for _ in range(pattern_length):
            y = (y * multiplier) % prime
        for i in reversed(range(text_length - pattern_length)):
            q[i] = (multiplier * q[i + 1] + ord(text[i]) - y * ord(text[i + pattern_length])) % prime
        return q
    
    pattern_hash = calculate_polynomial_hash(pattern, prime, multiplier)
    text_hashes = precompute_substring_hashes(text, len(pattern), prime, multiplier)

    # and return an iterable variable
    return [i for i, w in enumerate(text_hashes) if w == pattern_hash]


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

