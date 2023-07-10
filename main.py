def broken_search(nums, target) -> int:
    left_border = 0
    right_border = len(nums) - 1
    while left_border <= right_border:
        middle = (left_border + right_border) // 2
        middle_elem = nums[middle]
        left_border_elem = nums[left_border]
        right_border_elem = nums[right_border]

        if middle_elem == target:
            return middle
        if left_border_elem == target:
            return left_border
        if right_border_elem == target:
            return right_border

        if left_border_elem < middle_elem:
            if left_border_elem < target < middle_elem:
                right_border = middle - 1
            else:
                left_border = middle + 1
        else:
            if middle_elem < target < right_border_elem:
                left_border = middle + 1
            else:
                right_border = middle - 1
    return -1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input()
    target = int(input())
    text = input()
    #target = 5
    #text = '0 2 6 7 8 9 10'
    array = text.split(' ')
    array = [int(x) for x in array]
    result = broken_search(array, target)
    print(result)



