735. Asteroid Collision


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        mstk = []
        
        for i, planet in enumerate(asteroids):
            if not mstk or (mstk[-1] > 0 and planet > 0) or mstk[-1] < 0:
                mstk.append(planet)
                continue

            while mstk and mstk[-1] > 0 and planet < 0:
                # if new planet is smaller
                if mstk[-1] > - planet:
                    planet = 0
                    break
                # if new planet is equal to right most one
                elif mstk[-1] == - planet:
                    mstk.pop()
                    planet = 0
                    break
                # if new planet is larger 
                elif mstk[-1] < - planet:
                    mstk.pop()

            if planet:
                mstk.append(planet)
                     

        return mstk
