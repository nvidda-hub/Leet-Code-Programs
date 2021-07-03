from collections import defaultdict


class Solution:

    def in_order_traversal(self, root, cache: dict):
        if not root:
            return
        cache[root.val] = cache[root.val] + 1
        self.in_order_traversal(root.left, cache)
        self.in_order_traversal(root.right, cache)
        return

    def find_mode(self, root) -> list[int]:
        if not root:
            return []
        cache = defaultdict(int)
        self.in_order_traversal(root, cache)
        max_freq = max(cache.values())
        result = [k for k,v in cache.items() if v == max_freq]
        return result
