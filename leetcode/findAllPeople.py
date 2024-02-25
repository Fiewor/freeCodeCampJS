# https://leetcode.com/problems/find-all-people-with-secret/?envType=daily-question&envId=2024-02-24

def findAllPeople(n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
    secrets = set([0, firstPerson])
    time_map = {}

    for src, dest, time in meetings:
        if time not in time_map:
            time_map[time] = defaultdict(list)
        
        time_map[time][src].append(dest)
        time_map[time][dest].append(src)
    
    def dfs(src, adj):
        if src in visited:
            return
        visited.add(src)
        secrets.add(src)
        for neighbor in adj[src]:
            dfs(neighbor, adj)
    
    for time in sorted(time_map.keys()):
        visited = set()
        for src in time_map[time]:
            if src in secrets:
                dfs(src, time_map[time])

    return list(secrets)
