#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <cassert>

class Solution{
    public:
    bool uniqueOccurrences(std::vector<int>& arr){
        std::unordered_map<int, int> count_map;

        for (int num : arr){
            if (count_map.find(num) != count_map.end()){
                count_map[num] += 1;
            }else{
                count_map[num] = 1;
            }
        }

        std::unordered_set<int> occurrence_set;
        for (const auto& entry: count_map){
            occurrence_set.insert(entry.second);
        }

        return occurrence_set.size() == count_map.size();
    }
};

int main()
{
    Solution s;

    std::vector<int> arr = {1,2,2,1,1,3};
    bool result = s.uniqueOccurrences(arr);
    bool expected = true;
    std::cout << "Result: " << result << ", Expected: " << expected << std::endl;
}