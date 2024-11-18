class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        decrypt = [0] * len(code)
        if k > 0:
            for i in range(len(code)):
                val = 0
                for j in range(1, k + 1):
                    val += code[(i + j) % len(code)]
                decrypt[i] = val
        elif k < 0:
            for i in range(len(code)):
                val = 0
                for j in range(1, abs(k) + 1):
                    val += code[(i - j) % len(code)]
                decrypt[i] = val
        return decrypt


        