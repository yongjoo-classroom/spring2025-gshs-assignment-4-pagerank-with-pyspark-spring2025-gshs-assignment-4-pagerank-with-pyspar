# PageRank with PySpark

## Objective
PageRank is an algorithm to rank web pages based on their importance. 
In this assignment, you will implement PageRank in PySpark.

## Additional Resources
You can learn more about PySpark and transformations here:
- [PySpark Documentation](https://spark.apache.org/docs/latest/rdd-programming-guide.html)
- [RDD Transformations](https://spark.apache.org/docs/latest/rdd-programming-guide.html#transformations)

## Formula
For a given node **i**, the PageRank score is computed as:

<img width="1148" alt="Screenshot 2025-02-05 at 4 27 41 PM" src="https://github.com/user-attachments/assets/a9b64f9a-67df-4be8-95d4-f1beb95fc214" />

Taking d = 0.85, 

<img width="1147" alt="Screenshot 2025-02-05 at 4 27 56 PM" src="https://github.com/user-attachments/assets/1c812963-fb97-4a82-8036-f389eed0e489" />


where:
- **PR(i)** is the PageRank of node **i**.
- **M(i)** is the set of nodes linking to **i**.
- **L(j)** is the number of outbound links of **j**.
- **0.85** is the damping factor.

Initial rank value of each node will be 1. 

## Instructions
1. Implement the function `compute_pagerank` in `pagerank.py`.
2. The function should take:
   - A dictionary where keys are nodes and values are lists of outgoing links from that node.
   - The number of iterations to refine the PageRank scores.
3. The function should return a dictionary mapping each node to its final PageRank score.

### Input Format
```
{
    0: [1, 2],
    1: [2, 6],
    2: [1, 0, 7],
    3: [1, 0],
    4: [1, 2],
    5: [0, 1, 2],
    6: [0, 7],
    7: [0, 1, 3],
}
```
