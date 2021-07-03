import re

class Solution:
    def myAtoi(self, s: str) -> int:        
        resp = re.search(r" *[+-]?(\d*)", s)
        if resp:
            t = resp.group(0).strip()
            if t in ["+", "-"]:
                return 0
            if not t.strip():
                return 0
            else:
                number = int(t)
                if number < -2**31:
                    return -2**31
                elif number > 2**31 - 1:
                    return 2**31 - 1
                else:
                    return number
        else:
            return 0