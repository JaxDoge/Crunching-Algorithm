815. Bus Routes



# 直接bfs
import collections
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # badcase
        if source == target:
            return 0

        def bfsSearch(_routes, _source, _target):
            # 构建图（部分），即某个 station 可以去的路线，通过这个 hashmap 知道哪些路线联通
            stationToLine = collections.defaultdict(set)
            # bfs 辅助 queue
            helper_queue = collections.deque()
            # 距离 Hashmap，记录从出发路线到该路线的距离
            distance = collections.defaultdict(int)

            # 线路编号直接从 0 开始
            lineNum = len(_routes)

            # 填充 stationToLine
            for line in range(lineNum):
                for station in _routes[line]:
                    # 如果起始站在线路中，该线路加入队列
                    if station == _source:
                        helper_queue.append(line)
                        # 线路对应距离初始化为1
                        distance[line] = 1
                    stationToLine[station].add(line)

            while helper_queue:
                popline = helper_queue.popleft()
                # 对应距离
                step = distance[popline]

                for station in _routes[popline]:
                    # 包含终点
                    if station == _target:
                        return step
                    # 下回合遍历的线路（部分）
                    next_lines = stationToLine[station]
                    # 可能这个站不是换乘站（没有这种情况吧……
                    if not next_lines: continue
                    for nl in next_lines:
                        if not nl in distance:
                            helper_queue.append(nl)
                            distance[nl] = step + 1

            return -1

        res = bfsSearch(routes,source,target)
        return res

