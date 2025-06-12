import pytest
from modules.count_cases import count_cases

def test_count_cases_with_short_sentence():
    string = "Hello, my name is Andres"

    result = count_cases (string)

    assert result == 2

def test_count_cases_with_long_sentence():
    string = "tOdAy iS aN ExCePtIoNaL DaY tO LeArN sOmEtHiNg NeW aBoUt ThE UnIvErSe, wHeThEr iT's PhYsIcS, pSyChOlOgY, oR sImPlY hOw tO bE a KiNdEr PeRsOn"

    result = count_cases (string)

    assert result == 56

def test_count_cases_with_numbers():
    string = 32353457356875494578

    with pytest.raises (TypeError):
        count_cases (string)
