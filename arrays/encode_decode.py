from typing import List

class Codec:
    """
    Implements string encoding and decoding for a list of strings.
    Each string is encoded as <length>#<string>.
    Example: ["cat", "dog"] -> "3#cat3#dog"
    """

    def encode(self, strings: List[str]) -> str:
        """
        Encodes a list of strings to a single string.
        """
        return ''.join(f"{len(s)}#{s}" for s in strings)

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single encoded string back into a list of strings.
        """
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            j += 1
            res.append(s[j:j + length])
            i = j + length
        return res
    
if __name__ == "__main__":
    codec = Codec()
    original = ["leet", "code", "123", "#test"]
    encoded = codec.encode(original)
    decoded = codec.decode(encoded)
    print(codec.decode(codec.encode(original))) # should be ["leet", "code", "123", "#test"]
    assert decoded == original