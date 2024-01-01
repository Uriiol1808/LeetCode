"""
841. Keys and Rooms
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except 
for room 0. Your goal is to visit all the rooms. However, you cannot enter 
a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. 
Each key has a number on it, denoting which room it unlocks, 
and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain 
if you visited room i, return true if you can visit all the rooms, 
or false otherwise.
"""

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited_rooms = set()

        def dfs(room):
            if room in visited_rooms:
                return
            visited_rooms.add(room)
            for key in rooms[room]:
                dfs(key)
        
        dfs(0)
        return len(visited_rooms) == len(rooms)
        
s = Solution()

# Case 1
result1 = s.canVisitAllRooms(rooms=[[1],[2],[3],[]])
expected1 = True
print(f"Result: {result1}, Expected: {expected1}")
assert result1 == expected1

# Case 2
result2 = s.canVisitAllRooms(rooms=[[1,3],[3,0,1],[2],[0]])
expected2 = False
print(f"Result: {result2}, Expected: {expected2}")
assert result2 == expected2

# Case 3
result3 = s.canVisitAllRooms(rooms=[[2],[],[1]])
expected3 = True
print(f"Result: {result3}, Expected: {expected3}")
assert result3 == expected3