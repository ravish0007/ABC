class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        indegree_counter = defaultdict(int)
        for v, u in prerequisites:
            graph[u].append(v)
            indegree_counter[v] += 1
        

        q = deque([u for u in range(numCourses) if indegree_counter[u] == 0])

        visited = set()

        while q:
            curr_course = q.popleft()
            visited.add(curr_course)

            for next_course in graph[curr_course]:
                if next_course not in visited:
                    indegree_counter[next_course] -= 1
                    if indegree_counter[next_course] == 0:
                        q.append(next_course)

        return len(visited) == numCourses
