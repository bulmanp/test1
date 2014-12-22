import pytest
from pb_module1 import hash_fn

def test_hash_fn():
    assert hash_fn("civet") == "c31365cc10efb80ce8035d878645cafc0a00052b4e3cfbf9ac1e811771e97e3c"
if __name__ == '__main__':
    pytest.main()
