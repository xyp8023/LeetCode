class Solution:
    def nextClosestTime(self, time: str) -> str:
        digits = [int(y) for x in time.split(':') for y in x]
        h, m = time.split(':')
        while True:
            if int(m) == 59:
                h, m = str(int(h)+1), '00'
            else:
                m = str(int(m)+1)
            # if int(h) > 23:
            if h=='24':
                h='00'
            if len(h)==1:
                h='0'+h
            if len(m)==1:
                m='0'+m
            if all([int(x) in digits for x in h+m]):
                return h + ':' +m

time = '19:34'
time = '1:34'
# time = '01:34'
# time = '00:00'
res = Solution().nextClosestTime(time)
print(res)
# digits = [int(y) for x in time.split(':') for y in x]
# h, m = time.split(':')
# while True:
#     if m =='59':
#         h, m = str(int(h) + 1),'00'
#         else:
#         m = str(int(m) + 1)
#     if h =='24':
#         h ='00'
#         if len(m) == 1:
#             m ='0'+m
#         if len(h) == 1:
#             h ='0'+h
#     if all(int(x) in digits for x in h + m):
#         return h +':'+m