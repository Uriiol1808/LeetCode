#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

class Solution{
    public:
    std::vector<std::vector<int>> findDifference(std::vector<int>& nums1, std::vector<int>& nums2){
        std::set<int> answer1;
        std::set<int> answer2;

        std::set<int> set_nums1(nums1.begin(), nums1.end());
        std::set<int> set_nums2(nums2.begin(), nums2.end());

        for (int num : set_nums1){
            if (set_nums2.find(num) == set_nums2.end()){
                answer1.insert(num);
            }
        }
        for (int num : set_nums2){
            if (set_nums1.find(num) == set_nums1.end()){
                answer2.insert(num);
            }
        }

        return {std::vector<int>(answer1.begin(), answer1.end()), std::vector<int>(answer2.begin(), answer2.end())};
    }
};

int main()
{
    Solution s;

    // Case 1
    std::vector<int> nums1_case1 = {1, 2, 3};
    std::vector<int> nums2_case1 = {2, 4, 6};
    std::vector<std::vector<int>> result1 = s.findDifference(nums1_case1, nums2_case1);
    std::vector<std::vector<int>> expected1 = {{1, 3}, {4, 6}};
    std::cout << "Result: {{" << result1[0][0] << "," << result1[0][1] << "},{" << result1[1][0] << "," << result1[1][1] << "}}, Expected: {{" << expected1[0][0] << "," << expected1[0][1] << "},{" << expected1[1][0] << "," << expected1[1][1] << "}}\n";

    std::vector<int> nums1_case2 = {1, 2, 3, 3};
    std::vector<int> nums2_case2 = {1, 1, 2, 2};
    std::vector<std::vector<int>> result2 = s.findDifference(nums1_case2, nums2_case2);
    std::vector<std::vector<int>> expected2 = {{3}, {}};
    std::cout << "Result: {{" << result2[0][0] << "},{}}, Expected: {{" << expected2[0][0] << "},{}}\n";

    return 0;
}