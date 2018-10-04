# class Solution:
#     def subdomainVisits(self, cpdomains):
#         """
#         :type cpdomains: List[str]
#         :rtype: List[str]
#         """
#         NumberList = []
#         WebList = []
#         WebSet = []
#         NumberSet = []
#         for domain in cpdomains:
#             num, web = domain.split(' ')
#             NumberList.append(num)
#             WebSet.append(web)
#             WebList.append(web)
#             subdomain =  web.split('.')
#             NumberSet.append(num)
#             for i in range(len(subdomain)-1):
#                 tmp = (subdomain[i]+'.')
#                 web = web.replace(tmp, '')
#                 WebSet.append(web)
#                 NumberSet.append(num)
#         WebSet1 = list(set(WebSet))
#         res_list = []
#         for i in WebSet1:
#             if WebSet.count(i)==1:
#                 j = WebSet.index(i)
#                 res_list.append(NumberSet[j]+' '+i)
#             else:
#                 indices = [k for k, x in enumerate(WebSet) if x ==i]
#                 tmp=0
#                 for j in indices:
#                     tmp+=int(NumberSet[j])
#                 res_list.append( str(tmp)+ ' ' + i)
#
#         return res_list


# another solution
# 1. using dictionary
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """

        res_domain = {}
        res_list = []
        for cpd in cpdomains:
            times, domain = cpd.split(' ')
            sub_domains = domain.split('.')
            for i in range(len(sub_domains)):
                sub_domain = '.'.join(sub_domains[i:])
                if sub_domain not in res_domain:
                    res_domain[sub_domain]=0
                res_domain[sub_domain]+=int(times)

        for key, value in res_domain.items():
            res_list.append(str(value) + ' ' + key)
        return res_list



cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
sol = Solution()
res = sol.subdomainVisits(cpdomains)
print(res)

