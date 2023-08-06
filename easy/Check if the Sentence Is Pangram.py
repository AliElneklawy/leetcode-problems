class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet_lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        for i in sentence:
            if i in alphabet_lowercase:
                alphabet_lowercase.remove(i)

        return len(alphabet_lowercase) == 0
