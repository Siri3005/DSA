class Solution(object):
    def average(self, salary):
        salary.remove(min(salary))
        salary.remove(max(salary))
        return float(sum(salary))/len(salary)