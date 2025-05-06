

## 📝 Tasks Overview

### 1. Multi-threaded Merge Sort
- **Description**: Implements merge sort using Python's `threading` module. Threads split the sorting workload recursively, with depth control to limit thread count.
- **Key Features**:
  - Compares execution time with single-threaded merge sort.
  - Limits threads using a `MAX_DEPTH` threshold (default: 3).

### 2. Multi-threaded Quicksort
- **Description**: Parallelizes quicksort by sorting sub-arrays concurrently with threads.
- **Key Features**:
  - Controls thread count via `MAX_DEPTH` (default: 2).
  - Compares performance against single-threaded quicksort.

### 3. Concurrent File Downloader
- **Description**: Downloads multiple files concurrently using threads.
- **Key Features**:
  - Accepts URLs via command line or a text file.
  - Compares concurrent vs. sequential download times.
  - Saves files as `concurrent_file_{i}.txt` and `sequential_file_{i}.txt`.

---
