class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0)+1
        srt = sorted(freq.keys(), key=lambda num: freq[num], reverse=True)
        return srt[:k]