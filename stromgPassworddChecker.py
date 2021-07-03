class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        low, up, digit = 0, 0, 0

        last = '_'
        repeats = []
        for i in range(n):
            x = password[i]
            if x == last:
                repeats[-1] += 1
            else:
                last = x
                repeats.append(1)

            if ord('a') <= ord(x) <= ord('z'):
                low += 1
            if ord('A') <= ord(x) <= ord('Z'):
                up += 1
            if ord('0') <= ord(x) <= ord('9'):
                digit += 1

        types = 0  # types  to be needed
        if low == 0:
            types += 1
        if up == 0:
            types += 1
        if digit == 0:
            types += 1
        print(types, n, repeats)

        if n < 6:
            return max(6 - n, types)
        elif n <= 20:
            swaps = sum([x // 3 for x in repeats])
            return max(swaps, types)
        else:
            surplus = n - 20
            m = len(repeats)
            for i in range(m):
                if surplus >= 1 and repeats[i] % 3 == 0:
                    repeats[i] -= 1
                    surplus -= 1
            for i in range(m):
                if surplus >= 2 and repeats[i] >= 3 and repeats[i] % 3 == 1:
                    repeats[i] -= 2
                    surplus -= 2
            for i in range(m):
                if surplus > 0 and repeats[i] >= 3:
                    removed = min(repeats[i] - 2, surplus)
                    repeats[i] -= removed
                    surplus -= removed
            swaps = sum([x // 3 for x in repeats])
            print(surplus, swaps, repeats)
            return n - 20 + max(swaps, types)