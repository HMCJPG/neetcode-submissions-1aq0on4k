class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        
        int n = temperatures.size();

        std::vector<int> results(n, 0);
        std::stack<int> st;

        for (int i = 0; i < n; ++i) {

            while (!st.empty() && temperatures[i] > temperatures[st.top()]) {
                int lastDay = st.top();
                st.pop();

                results[lastDay] = i - lastDay;

            }
            st.push(i);

        }

        return results;











    }
};
