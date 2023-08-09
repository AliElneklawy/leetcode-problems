class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        l = []
        prods = []
        products.sort()
        for i, c in enumerate(searchWord):
            products = [p for p in products if len(p) > i and p[i] == c]
            l.append(products[:3])

        return l

