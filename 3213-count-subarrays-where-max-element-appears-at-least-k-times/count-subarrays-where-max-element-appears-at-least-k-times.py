class Solution:
	def countSubarrays(self, nums: List[int], k: int) -> int:

		result = 0

		start_index = 0

		max_num = max(nums)

		max_elements_in_window = 0

		for end_index in range(len(nums)):

			if nums[end_index] == max_num:

				max_elements_in_window = max_elements_in_window + 1

			while max_elements_in_window == k:

				if nums[start_index] == max_num:

					max_elements_in_window = max_elements_in_window - 1

				start_index = start_index + 1

			result = result + start_index

		return result
		
