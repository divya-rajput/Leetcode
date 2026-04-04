class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        output = []
        i = 1
        while i <= n:
            ans = ""
            if i % 3 == 0:
                ans = "Fizz"
                if i % 5 == 0:
                    ans += "Buzz"
            elif i % 5 == 0:
                ans = "Buzz"
            else:
                ans = str(i)
            output.append(ans)
            i += 1
        return output