def find_zero_sum_triplets(arr):
    n = len(arr)
    triplets = []
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplets.append((arr[i], arr[j], arr[k]))
    print(f"Triplets that sum to zero: {triplets}")
    return triplets

nums = [-1, 0, 1, 2, -1, -4]
find_zero_sum_triplets(nums)
