841. Keys and Rooms


# BFS
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        from collections import deque
        n = len(rooms)
        roomState = [0] * n
        roomState[0] = 1 

        keys = deque()
        keys.extend(rooms[0])

        while keys:
            curkey = keys.pop()
            if roomState[curkey] == 1:
                continue

            roomState[curkey] = 1
            keys.extend(rooms[curkey])

        return sum(roomState) == n
