# https://leetcode.com/problems/group-anagrams/

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    map = {}
    ind = 0
    arr = [] 

    for str in strs:
        str_sorted = ''.join(sorted(str))
        
        if str_sorted in map:
            arr[map[str_sorted]].append(str)
        else:
            map[str_sorted] = ind
            arr.append([])
            arr[ind].append(str)
            ind += 1

    return arr

# even better
def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    map = {}

    for str in strs:
        str_sorted = ''.join(sorted(str))
        
        if str_sorted in map:
            map[str_sorted].append(str)
        else:
            map[str_sorted] = [str]

    return map.values()