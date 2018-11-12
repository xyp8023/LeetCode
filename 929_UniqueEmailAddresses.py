class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        emails_dict = dict()
        for email in emails:
            [localName, domainName] = email.split('@')
            if '+' in localName:
                plusLocalName = localName.split('+')
                localName = plusLocalName[0]
            if '.' in localName:
                localName = localName.replace('.', '')
            r_email = localName + '@' + domainName

            if r_email not in emails_dict:
                emails_dict[r_email]=1
            else:
                emails_dict[r_email]+=1
        return len(emails_dict.keys())



# class Solution:
#     def numUniqueEmails(self, emails):
#         """
#         :type emails: List[str]
#         :rtype: int
#         """
#         emails=self.dotPlusProcess(emails)
#         emails_dict = dict()
#         for email in emails:
#             if email not in emails_dict:
#                 emails_dict[email]=1
#             else:
#                 emails_dict[email]+=1
#         return len(emails_dict.keys())
#     def dotPlusProcess(self, emails):
#         """
#         :type emails: List[str]
#         :rtype: List[str]
#         """
#         r_emails = list()
#         for email in emails:
#             [localName,domainName] = email.split('@')
#             if '+' in localName:
#                 [plusBefore, plusAfter] = localName.split('+')
#                 localName = plusBefore
#             if '.' in localName:
#                 localName=localName.replace('.','')
#             r_emails.append(localName+'@'+domainName)
#         return r_emails





emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
sol = Solution()
res = sol.numUniqueEmails(emails)
print(res)