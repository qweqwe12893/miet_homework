
def hofstadter_f_m(n: int) -> "generator":

    def female(n: int) -> int:

        if n == 0:
            return 1
        return n - male(female(n - 1))


    def male(n: int) -> int:
        if n == 0:
            return 0
        return n - female(male(n - 1))


    for i in range(0, n):
        yield (female(i), male(i))


n = 5

for i in hofstadter_f_m(n):
    print(i)