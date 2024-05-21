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

    // Case 1
    std::vector<int> arr = {1,2,2,1,1,3};
    bool result = s.uniqueOccurrences(arr);
    bool expected = true;
    std::cout << "Result: " << result << ", Expected: " << expected << std::endl;

    std::vector<int> arr2 = {1,2};
    bool result2 = s.uniqueOccurrences(arr2);
    bool expected2 = false;
    std::cout << "Result: " << result2 << ", Expected: " << expected2 << std::endl;

    std::vector<int> arr3 = {-3,0,1,-3,1,1,1,-3,10,0};
    bool result3 = s.uniqueOccurrences(arr3);
    bool expected3 = true;
    std::cout << "Result: " << result3 << ", Expected: " << expected3 << std::endl;
}