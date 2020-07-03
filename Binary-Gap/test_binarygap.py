from binarygap import solution

def test_solution_5():
    N = 5
    assert solution(N) == 1

def test_solution_51712():
    N = 51712
    assert solution(N) == 2

def test_solution_561892():
    N = 561892
    assert solution(N) == 3

def test_solution_66561():
    N = 66561
    assert solution(N) == 9

def test_solution_6291457():
    N = 6291457
    assert solution(N) == 20

def test_solution_74901729():
    N = 74901729
    assert solution(N) == 4

def test_solution_1376796946():
    N = 1376796946
    assert solution(N) == 5

def test_solution_1610612737():
    N = 1610612737
    assert solution(N) == 28
