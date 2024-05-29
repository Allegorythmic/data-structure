# Overview of data structure covered

## 1. Array
A collection of elements identified by index or key. The elements are stored in contiguous memory locations.

## 2. Linked List
### 2.1 Singly Linked List
A series of nodes where each node points to the next node in the series.
### 2.2 Doubly Linked List
A series of nodes where each node points to both the next and the previous nodes in the series.

## 3. Stack
A collection of elements that follows the Last In, First Out (LIFO) principle. Elements are added and removed from the top.

## 4. Deque (Double-Ended Queue)
A double-ended queue that allows insertion and deletion of elements from both the front and the rear.

## 5. Queue
### 5.1. Simple Queue
A collection of elements that follows the First In, First Out (FIFO) principle. Elements are added at the rear and removed from the front.
### 5.2. Circular Queue
Similar to a simple queue but connects the end of the queue back to the front, forming a circle.
### 5.3. Priority Queue
Each element is associated with a priority, and elements are served based on their priority.

## 6. Hash Table
A data structure that maps keys to values for efficient lookup. It uses a hash function to compute an index into an array of buckets or slots.

## 7. Tree
### 7.1 Binary Tree
A tree data structure in which each node has at most two children referred to as the left child and the right child.
### 7.2. Binary Search Tree (BST)
A binary tree with the additional condition that for each node, the left subtree contains only nodes with values less than the node's value, and the right subtree only nodes with values greater than the node's value.
### 7.3. AVL Tree
A self-balancing binary search tree where the difference in heights between the left and right subtrees is at most one for all nodes.
### 7.4. Red-Black Tree
A self-balancing binary search tree with an extra bit of storage per node: its color, which can be either red or black. This ensures the tree remains approximately balanced.
### 7.5. B-Tree
A self-balancing tree data structure that maintains sorted data and allows searches, sequential access, insertions, and deletions in logarithmic time. It is commonly used in databases and file systems.
### 7.6. Segment Tree
A tree data structure used for storing information about intervals or segments. It allows querying which segments a point falls into or querying some information about a segment efficiently.
### 7.7. Fenwick Tree (Binary Indexed Tree)
A data structure that provides efficient methods for calculation and manipulation of the prefix sums of a table of values.
### 7.8. Suffix Tree
A compressed trie of all suffixes of a given text. It is used in efficient string matching algorithms.
### 7.9. KD-Tree (K-Dimensional Tree)
A space-partitioning data structure for organizing points in a k-dimensional space. It is useful for range searches and nearest neighbor searches.
### 7.10. R-Tree
A tree data structure used for spatial access methods, i.e., for indexing multi-dimensional information such as geographical coordinates, rectangles, and polygons.
### 7.11. Quad Tree
A tree data structure in which each internal node has exactly four children. It is commonly used to partition a two-dimensional space by recursively subdividing it into four quadrants or regions.
### 7.12. Octree
Similar to a quad tree, but it partitions three-dimensional space by recursively subdividing it into eight octants.

## 8. Heap
### 8.1. Min Heap
A complete binary tree where the value of each node is less than or equal to the values of its children, with the smallest value at the root.
### 8.2. Max Heap
A complete binary tree where the value of each node is greater than or equal to the values of its children, with the largest value at the root.

## 9. Graph
### 9.1. Adjacency Matrix
A 2D array where each cell at row i and column j indicates whether there is an edge between vertex i and vertex j.
### 9.2. Adjacency List
An array of lists. The index represents a vertex, and each element in the list at that index represents the vertices adjacent to it.

## 10. Trie
A tree-like data structure used to store a dynamic set of strings, where the keys are usually strings. It is used for searching words in a dictionary efficiently.

## 11. Set
A collection of unique elements. It is often used to test membership, remove duplicates, and compute mathematical operations like union, intersection, and difference.

## 12. Disjoint Set (Union-Find)
A data structure that keeps track of a set of elements partitioned into a number of disjoint (non-overlapping) subsets. It supports two operations: finding the set a particular element is in, and uniting two sets.

## 13. Skip List
A data structure that allows fast search within an ordered sequence of elements. It is built in layers, with each layer being a sorted list of elements, and elements in higher layers also appearing in lower layers.

## 14. Bloom Filter
A space-efficient probabilistic data structure used to test whether an element is a member of a set. False positives are possible, but false negatives are not.

## 15. Treap
A combination of a binary search tree and a heap. Each node has a key and a priority, and the tree maintains both the binary search tree property and the heap property.

## 16. Count-Min Sketch
A probabilistic data structure that serves as a frequency table of events in data streams. It provides approximate counts of elements with bounded errors.
