// http://oj.leetcode.com/problems/single-number/
class Solution {
public:
	int singleNumber(int A[], int n) {
		int res;
		for (int i; i < n; i++) {
			res ^= A[i];
		}
		return res;
	}
};
