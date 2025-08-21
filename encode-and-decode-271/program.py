class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for st in strs:
            str_len = len(st)
            encoded_str += str(str_len) + "#" + st 
        return encoded_str

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            delimeter_index = s.find('#', i)
            string_length = int(s[i:delimeter_index])
            start_index = delimeter_index + 1
            end_index =  start_index + string_length
            string = s[start_index:end_index]

            result.append(string)
            i= end_index
        return result