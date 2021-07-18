# Getting longest substring without repeating
I solved this problem by viewing it as a transversal problem. Basically, I have an index and a pointer. The index is for transversing round the given string; while the pointer tells when to restart if a duplicate character is found.


I broke down the solution to this problem into the following steps:
1. Obtaining all distinct substrings and their respective lengths; as seen in function get_distinct_substrings
2. Getting the longest occuring string from the extracted substrings in 1; as seen in function get_longest_substring

I also wrote tests to ensure everything was fine.

## To Do
- [ ] Make code cleaner. Reduce the repetitions
