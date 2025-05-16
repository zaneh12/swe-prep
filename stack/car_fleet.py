from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        LeetCode 853. Car Fleet
        https://leetcode.com/problems/car-fleet/

        There are n cars going to the same destination along a one-lane road.
        The destination is target miles away.

        Each car i starts at position[i] and travels at constant speed[i].
        A car can never pass another car ahead of it, but it can catch up and form a fleet.

        A fleet is a group of cars traveling at the same speed and position.
        Return the number of fleets that will arrive at the destination.

        Approach:
        - Pair each car's position and speed
        - Sort cars by starting position in descending order (farthest from target to nearest)
        - Simulate fleets using a stack:
          - Push each car's arrival time to the stack
          - If a car arrives sooner than or equal to the one ahead, it merges into the same fleet

        Time Complexity: O(n log n) due to sorting
        Space Complexity: O(n) for the stack

        Redid this one on 2025-05-16. Thought in discrete steps at first, but time is continuous here.
        """
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)  # Sort by position descending

        stack = []
        for p, s in pair:
            arrival_time = (target - p) / s
            stack.append(arrival_time)
            # Merge with the previous fleet if this one arrives earlier or at the same time
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
