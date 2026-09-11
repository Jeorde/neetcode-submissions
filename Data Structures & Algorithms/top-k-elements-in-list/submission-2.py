class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num, count in freq.items():
            bucket[count].append(num)

        result = []
        current = len(nums)

        while len(result) < k:
            for num in bucket[current]:
                result.append(num)

                if len(result) == k:
                    return result

            current -= 1