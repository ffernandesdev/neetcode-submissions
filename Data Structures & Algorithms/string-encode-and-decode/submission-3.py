class Solution:
    # O(n)
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "&" + s
        return encoded_str

    # O(n)
    def decode(self, s: str) -> List[str]:
        decoded_strs = []

        i = 0
        while i < len(s):
            l = i + 1

            while s[l] != "&":
                l += 1

            offset = int(s[i:l])
            l += 1
            r = l + offset
            decoded_strs.append(s[l:r])
            i = r

        return decoded_strs