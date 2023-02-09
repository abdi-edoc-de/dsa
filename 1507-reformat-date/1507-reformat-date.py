class Solution:
    def reformatDate(self, date: str) -> str:
        monthes = {
            "Jan" : 1, "Feb" : 2, "Mar" : 3, "Apr" : 4, "May" : 5, "Jun" : 6, "Jul" : 7, "Aug" : 8, "Sep" : 9, "Oct": 10, "Nov" : 11, "Dec": 12
        }
        
        date = date.split()
        ans = ''
        for i in date[0]:
            if i.isdigit():
                ans += i
        if len(ans) == 1:
            ans = '0' + ans
            
        m = "0" + str(monthes[date[1]]) if monthes[date[1]] < 10 else str(monthes[date[1]])
        return str(date[2]) + "-" + m + '-' + ans
