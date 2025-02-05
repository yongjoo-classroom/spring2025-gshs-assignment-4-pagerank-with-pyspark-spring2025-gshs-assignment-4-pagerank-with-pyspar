import pytest
from pagerank import compute_pagerank

def test_pagerank():
    links_dict = {
        0: [1, 2],
        1: [2, 6],
        2: [1, 0, 7],
        3: [1, 0],
        4: [1, 2],
        5: [0, 1, 2],
        6: [0, 7],
        7: [0, 1, 3],
    }

    
    result = compute_pagerank(links_dict, iterations=10)
    expected = {0 : 0.1980,
            1: 0.2389,
            2 : 0.2177,
            3 : 0.05604,
            4 : 0.01875,
            5 : 0.01875,
            6 : 0.1203,
            7 : 0.1316}
    
    assert set(result.keys()) == set(expected.keys())
    
    for node in expected:
        assert pytest.approx(result[node], rel=1e-2) == expected[node], f"Mismatch at node {node}"
