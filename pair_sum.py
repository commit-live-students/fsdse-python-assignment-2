def pairSum(list, k):
    if len(list)<2 and len(list) >1000:
        return
    seen=set()
    output=set()
    for num in list:
        target = k-num
        if target not in seen:
            seen.add(num)
        else:
            output.add( (min(num, target), max(num, target)) )
    return output