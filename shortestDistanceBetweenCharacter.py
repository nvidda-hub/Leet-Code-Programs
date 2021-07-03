class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:

        print(s, c)
        idxs = []

        for i in range(len(s)):
            if s[i] == c:
                idxs.append(i)

        distances = [1] * len(s)
        for i in idxs:
            distances[i] = 0

        print(distances)

        left = idxs[0]
        right = idxs[0]

        for i in range(len(distances)):

            if i > right:
                left = right
                idxs = idxs[1:]

                if len(idxs) > 0:
                    right = idxs[0]

            distances[i] = min(abs(left - i), abs(right - i))

        return distances