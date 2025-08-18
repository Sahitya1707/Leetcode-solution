class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
           '''
        Create a hashmap (dictionary) to group words by their sorted character string.
        For each word, sort its characters and use the sorted string as the key.
        Store the original word in a list mapped to that key.
        Finally, return all grouped lists of anagrams.

        Time Complexity: O(N * K log K)
        - N: number of strings in strs
        - K: maximum length of a string in strs
        Sorting each string takes O(K log K), and we do this for each string.
        '''
        if not strs:
            return [[""]]
        my_dict = {}
       

        for i,item in enumerate(strs):
            sortedString = "".join(sorted(item))
            if sortedString in my_dict.keys():
                my_dict[sortedString].append(item)
            else:
               my_dict[sortedString] = [item]
               

            
        return list(my_dict.values())