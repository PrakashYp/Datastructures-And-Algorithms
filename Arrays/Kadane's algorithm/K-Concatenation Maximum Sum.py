def kConcatenationMaxSum(arr, k):
        MOD = 10**9 + 7

        def kadane(nums):
            curr = 0
            best = 0

            for num in nums:
                curr = max(0, curr + num)
                best = max(best, curr)

            return best

        total_sum = sum(arr)

        if k == 1:
            return kadane(arr) % MOD

        best_two = kadane(arr + arr)

        if total_sum > 0:
            return (best_two + (k - 2) * total_sum) % MOD

        return best_two % MOD

arr= [-1,-2]
k = 7

print(kConcatenationMaxSum(arr,k))


    


