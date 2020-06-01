def sum_dif_rev(n):
    number = 1
    numbers = []
    while len(numbers) != n:
        reverse = str(number)[::-1]
        if reverse.startswith('0'):
            pass
        else:
            summary = number + int(reverse)
            difference = abs(number-int(reverse))
            if difference == 0:
                pass
            else: 
                if summary%difference == 0:
                    numbers.append(number)
        number+=1    
    return numbers[n-1]

#test
print(sum_dif_rev(45))