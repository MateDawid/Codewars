def tribonacci(signature, n):
    array = []
    array.append(signature[0])
    array.append(signature[1])
    array.append(signature[2])
    if n in range(0,4):
        return signature[:n]
    else:
        for i in range (n-3):
            next = array[i]+array[i+1]+array[i+2]
            array.append(next)
        return array

#test
print(tribonacci([2,3,7],4))
print(tribonacci([2,3,7],5))
print(tribonacci([2,3,7],6))