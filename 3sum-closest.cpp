// http://oj.leetcode.com/discuss/2217/o-n-3-solution-can-pass-the-judge 
// Python TLE
class Solution {
public:

    int threeSumClosest(vector<int> &num, int target) {

        int i,j,k,s,s1;

        s = num[0] + num[1] + num[2];
        s1 = abs(s - target);
        for(i=0;i<num.size()-2;i++)
            for(j=i+1;j<num.size()-1;j++)
                for(k=j+1;k<num.size();k++)
                {
                    if(s1> abs(num[i] + num[j] + num[k] - target) )
                    {
                        s = num[i] + num[j] + num[k];
                        s1 = abs(s - target);

                        // Without this condition, I get TLE
                        if(s1==0)
                            return s;
                    }
                }
        return s;
    }
};

