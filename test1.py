def unique_sorted(numbers):
    evens = [n for n in numbers if n % 2 == 0]
    return sorted(set(evens), reverse=True)

    
