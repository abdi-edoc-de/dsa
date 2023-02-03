class Solution:
    def simplifyPath(self, path: str) -> str:
        clean = []
        for p in path:
            if p == '/' and clean and clean[-1] == '/':
                continue
            clean.append(p)
        path = ''.join(clean)
        paths, result = [p for p in path.split('/') if p != ''], []
        for p in paths:
            if p == '..':
                if result:
                    result.pop()
            elif p == '.':
                continue
            else:
                result.append(p)
        return '/' + '/'.join(result)
        
            