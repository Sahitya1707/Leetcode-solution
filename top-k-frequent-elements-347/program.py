class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a hashmap to count the frequency of each number
        my_dict = {}
        # iterate through the list and count occurrences
      
        for num in nums:
            #  if num not in the hashmap, initialize it with 1, otherwise increment the count
            if num not in my_dict.keys():
                my_dict[num] = 1
            else:
                my_dict[num] += 1
        # sort the dictionary by frequency and get the top k elements
        counts_list = sorted(my_dict.items(), key=lambda x:x[1], reverse=True)
        #soreted elments in hashmap are in descending order of frequency
        sorted_count = dict(counts_list[:k])
        return [num for num in sorted_count] # return the keys of the top k frequent elements








        '''
        my though process
        
        Given an array of integers and an integer k, return the k most frequent elements in the array.
        nums - array[int]
        k - int
        k (most frequest array within the array)
        output can be any array
        is there any time and space complexity? should be better then O(n log n)
        means i can do one for loop 


        


        create a hashmap
        store the number as key and repitation as value
        


        '''