def square_root_bisection(number, tolerance = 0.01, max_iterations=10):
    if number < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    elif number == 0 or number == 1:
        print(f'The square root of {number} is {number}')
        return number
    else:
        low = 0
        high = number + 1
        mid = 0
        counter = 1
        
        while (high - low) > tolerance:
            mid = (low + high) / 2.0
            test = mid**2
            
            if counter >= max_iterations:
                print(f'Failed to converge within {max_iterations} iterations')
                return None
            
            if test == number:
                print(f'The square root of {number} is approximately {mid}')
                return mid
            elif test < number:
                low = mid
            elif test > number:
                high = mid
                
            counter += 1

        print(f'The square root of {number} is approximately {mid}')
        return mid