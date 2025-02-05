import pytest
from pagerank import compute_pagerank

def test_pagerank():
    links_dict = {
    0: [1, 2],
    1: [2, 6],
    2: [1, 0, 7],
    3: [1, 0, 4],
    4: [1, 2, 5],
    5: [0, 1, 2],
    6: [0, 7],
    7: [0, 1, 3],
    }

    
    result = compute_pagerank(links_dict, iterations=10)
    
    expected = {
   0: 0.18976748524854603,
   1: 0.2305641186257404,
   2: 0.2152287356126763,
   6: 0.11674009557914725,
   7: 0.12934582179274545,
   3: 0.05539774118928701,
   4: 0.03444624791113541,
   5: 0.02850975404072205
    }
    
    assert set(result.keys()) == set(expected.keys())
    
    for node in expected:
        assert pytest.approx(result[node], rel=1e-2) == expected[node], f"Mismatch at node {node}"
