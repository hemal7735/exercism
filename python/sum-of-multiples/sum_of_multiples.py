def sum_of_multiples(limit, multiples):
    nums = set()

    for m in multiples:
        if m == 0:
            continue
        curr = m
        while(curr < limit):
            print(f'multiple:{m}, curr: {curr}')
            nums.add(curr)
            curr += m
    
    return sum(nums)

print(sum_of_multiples(10, [3, 5]))
