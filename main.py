def isPrime(x):
    '''
    Determina daca un numar este prim.
    :param x: Un numar intreg.
    :return: True, daca x este prim sau False in caz contrar.
    '''
    if x < 2:
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True


def test_IsPrime():
    assert isPrime(-1) is False
    assert isPrime(0) is False
    assert isPrime(1) is False
    assert isPrime(2) is True
    assert isPrime(3) is True
    assert isPrime(4) is False
    assert isPrime(5) is True


def allPrime(l):
    '''
    Determina daca toate numerele dintr-o lista sunt prime.
    :param l: Lista de numere intregi.
    :return: True, daca toate numerele din l sunt prime sau False, in caz contrar.
    '''
    for x in l:
        if not isPrime(x):
            return False
    return True


def test_allPrime():
    assert allPrime([]) is True
    assert allPrime([10, 4, 5]) is False
    assert allPrime([10, 20]) is False
    assert allPrime([3, 5, 7]) is True


def allPrimeDigits(l):
    '''
    Determina daca toate numerele dintr-o lista sunt numere a caror cifre sunt prime.
    :param l: Lista de numere intregi.
    :return: True, daca toate numerele din l sunt numerea caror cifre sunt prime sau False in caz contrar.
    '''
    for x in l:
        while x != 0:
            if not isPrime(x % 10):
                return False
            x //= 10
    return True


def test_allPrimeDigits():
    assert allPrime([]) is True
    assert allPrime([10, 4, 5]) is False
    assert allPrime([10, 20]) is False
    assert allPrime([3, 5, 7]) is True
    assert allPrimeDigits([3, 11, 17, 22]) is False
    assert allPrimeDigits([27, 33, 23]) is True


def get_longest_all_primes(lst: list[int]) -> list[int]:
    '''
    Determina cea mai lunga subsecventa de numere prime.
    :param lst: lista de numere intregi
    :return: cea mai lunga subsecventa de nr. prime din l
    '''
    longestMax = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if allPrime(lst[i:j + 1]) and len(lst[i:j + 1]) > len(longestMax):
                longestMax = lst[i:j + 1]
    return longestMax


def test_get_longest_all_primes():
    assert get_longest_all_primes([]) == []
    assert get_longest_all_primes([1, 2, 3]) == [2, 3]
    assert get_longest_all_primes([11, 10, 12]) == [11]
    assert get_longest_all_primes([10, 20, 3, 10]) == [3]
    assert get_longest_all_primes([10, 20, 3, 5, 10]) == [3, 5]


def get_longest_prime_digits(lst: list[int]) -> list[int]:
    '''
    Determina cea mai lunga subsecventa de numere a caror cifre sunt prime.
    :param lst: Lista de numere intregi.
    :return: Returneaza cea mai lunga subsecventa de numere a caror cifre sunt prime.
    '''
    longestMax = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if allPrimeDigits(lst[i:j + 1]) and len(lst[i:j + 1]) > len(longestMax):
                longestMax = lst[i:j + 1]
    return longestMax


def test_get_longest_prime_digits():
    assert get_longest_prime_digits([]) == []
    assert get_longest_prime_digits([1, 2, 3]) == [2, 3]
    assert get_longest_prime_digits([11, 10, 12]) == []
    assert get_longest_prime_digits([10, 20, 3, 10]) == [3]
    assert get_longest_prime_digits([10, 20, 3, 5, 10]) == [3, 5]


def all_tests():
    test_allPrime()
    test_get_longest_all_primes()
    test_IsPrime()
    test_get_longest_prime_digits()
    test_allPrimeDigits()


def printMenu():
    print("1. Citire date")
    print("2. Determinare cea mai lungă subsecvență cu proprietatea 1.")
    print("3. Determinare cea mai lungă subsecvență cu proprietatea 2.")
    print("4. Iesire")


def citireLista():
    all_tests()
    l = []
    givenString = input("Dati lista, cu elemente separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l


def main():
    all_tests()
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            list = []
            list = citireLista()
        elif optiune == "2":
            print(get_longest_all_primes(list))
        elif optiune == "3":
            print(get_longest_prime_digits(list))
        elif optiune == "4":
            break
        else:
            print("Optiune gresita! Reincercati!")


main()
