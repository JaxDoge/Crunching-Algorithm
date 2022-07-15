780. Reaching Points




# Note that there is no negative number in the whole progress
# So we could search all the possible routes from t to s
# rather than from s to t
# the modulo calculation is brilliant
# just think about it, if x > y and x > sx, y > sy, if the next operation is x = x - y > y
# and x = sx, there is no way we could decrease y
# Or, if the transformation is possible, sx must smaller than x % y
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx > sx and ty > sy and tx != ty:
            if tx > ty:
                tx %= ty
            elif ty > tx:
                ty %= tx

        # At these point, we could judge the possiblity of transformation

        if tx == sx and ty == sy:
            return True

        elif tx == sx:
            return ty > sy and (ty - sy) % tx == 0

        elif ty == sy:
            return tx > sx and (tx - sx) % ty == 0

        return False


