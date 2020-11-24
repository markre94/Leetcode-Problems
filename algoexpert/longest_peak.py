def longestPeak(array):
    peak_max = 0
    i = 1
    while i < len(array) - 1:
        peak_val = 0
        if not check_if_is_peak(array[i-1], array[i], array[i+1]):
            i += 1
            continue

        peak_idx = i
        left = peak_idx - 1
        right = peak_idx + 1

        while array[peak_idx] > array[left] and left >= 0:
            peak_val += 1
            peak_idx -= 1
            left -= 1

        peak_idx = i
        while array[right] < array[peak_idx] and right < len(array) - 1:
            peak_val += 1
            peak_idx += 1
            right += 1

        if peak_max <= peak_val:
            peak_max = peak_val

        i += 1
    return peak_max


def check_if_is_peak(left, mid, right):
    return left < mid and mid > right


# print(longestPeak(array=[1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))
print(longestPeak(array=[1, 2, 3, 0]))