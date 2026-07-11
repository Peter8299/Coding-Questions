class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        for i in s:
            if i in "({[":
                stk.append(i)
            else:
                if not stk:return False
                t=stk.pop()
                if i==")" and t!="(":return False
                if i=="}" and t!="{":return False
                if i=="]" and t!="[":return False
        return len(stk)==0