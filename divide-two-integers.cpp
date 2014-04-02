class Solution {
public:
    int divide(int dividend, int divisor) {
		int a = abs(dividend);
		int b = abs(divisor);
		int sign, result, c;
		if (dividend >= 0 && divisor > 0) || (dividend < 0 && divisor < 0) {
			sign = 1;
		}
		else {
			sign = -1;
		}
		if (a < b) {
			result = 0;
		}
		else if (a == b) {
			result = 1;
		}
		else if (b == 1) {
			result = a;
		}
		else {
			result = 0;
			c = b;
			while (c <= a) {
				c += b;
				result += 1;
			}
		}
		if (sign == 1) {
			return result;
		}
		else {
			return 0 - result;
		}
	}
};
