def fibonacci(n):
    if n <= 1:
        return n

    sequence = [0, 1] 
    
    for i in range(2, n+1):
        next_value = sequence[i-1] + sequence[i-2]
        sequence.append(next_value)
            
    return sequence[n]