class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def checkIpv4(arr):
            for seg in arr:
                if len(seg) > 1 and seg[0] == '0':
                    return "Neither"
                if not seg.isnumeric():
                    return "Neither"
                if not ( 0 <= int(seg) <= 255):
                    return 'Neither'
            return 'IPv4'
        def checkIpv6(arr):
            letters = {'a','b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F'}
            for seg in arr:
                if 1 > len(seg) or len(seg) > 4:
                    return 'Neither'
                for i in seg:
                    if not i.isnumeric() and i not in letters:
                        return 'Neither'
            return 'IPv6'
        if len(queryIP.split('.')) == 4:
            return checkIpv4(queryIP.split('.'))
        elif len(queryIP.split(':')) == 8:
            return checkIpv6(queryIP.split(':'))
        else:
            return 'Neither'
        
        