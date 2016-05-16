# Uses python3
import sys

def mergeSort(b, left, ave, right):
    counter = 0
    inversions = 0
    left_side, right_side = b[left:ave], b[ave:right]
    l_index, r_index, b_index = 0, 0, left
    while l_index < len(left_side) and r_index < len(right_side):
        l = left_side[l_index]
        r = right_side[r_index]
        if l <= r:
            b[b_index] = l
            inversions += counter
            l_index += 1
        else:
            b[b_index] = r
            counter += 1
            r_index += 1
        b_index += 1
    while l_index < len(left_side):
        l = left_side[l_index]
        b[b_index] = l
        b_index += 1
        l_index += 1
        inversions += counter
    while r_index < len(right_side):
        r = right_side[r_index]
        b[b_index] = r
        b_index += 1
        r_index += 1
    return inversions

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    number_of_inversions += mergeSort(b,left,ave,right)
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_number_of_inversions(a, a, 0, len(a)))