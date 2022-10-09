def find_2d_peak(nums: list, l=0, r=0):
    def get_max_in_column(column):
        index_with_max_value = 0
        max_value = 0
        for index, value in enumerate(column):
            if value[0] >= max_value:
                max_value = value[0]
                index_with_max_value = index
        return index_with_max_value

    if r - l == 1:
        return get_max_in_column(nums)

    if r - l == 2 or len(nums) == 2:
        # r = 2
        first_column = [[i[l]] for i in nums]
        i = get_max_in_column(first_column)
        if nums[i][l] > nums[i][r - 1]:
            return [i, l]
        else:
            second_column = [[i[r - 1]] for i in nums]
            i = get_max_in_column(second_column)
            return [i, r - 1]

    middle = len(nums) // 2

    middle_column = [[i[middle]] for i in nums]
    max_value_index = get_max_in_column(middle_column)

    if nums[max_value_index][middle - 1] < nums[max_value_index][middle] > nums[max_value_index][middle + 1]:
        return [max_value_index, middle]

    if nums[max_value_index][middle - 1] > nums[max_value_index][middle]:
        r = middle
        return find_2d_peak(nums, l, r)

    if nums[max_value_index][middle + 1] > nums[max_value_index][middle]:
        l = middle + 1
        r = len(nums)
        return find_2d_peak(nums, l, r)

    return []


a = [
    [ 1, 5, 3],
    [10, 2, 4],
    [ 7, 8, 2],
]

b = [
    [1, 0],
    [7, 3],
]

c = [
    [ 1, 5, 3, 0, 13],
    [10, 2, 4, 3,  1],
    [ 7, 8, 2, 6,  7],
    [22, 11,5, 12, 17],
    [20, 4, 1, 2,  1],
]

result = find_2d_peak(a)
print(result)
