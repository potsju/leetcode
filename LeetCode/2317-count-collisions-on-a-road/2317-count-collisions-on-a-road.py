class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """
        collisions = 0
        moving = list(directions)
        while moving and moving[0] == "L":
            moving.pop(0)
        while moving and moving[-1] == "R":
            moving.pop()
        for c in moving:
            if c != "S":
                collisions+=1
        return collisions