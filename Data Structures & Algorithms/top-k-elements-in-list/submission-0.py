class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        sortfreq= sorted(freq.items(), key=lambda x:x[1], reverse=True)
        return [i[0] for i in sortfreq[:k]]