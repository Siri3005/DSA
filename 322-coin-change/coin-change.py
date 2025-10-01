class Solution(object):
    def coinChange(self, coins, amount):
        amt=[amount+1]*(amount+1)
        amt[0]=0
        for i in range(1,amount+1):
            for j in range(len(coins)):
                if (coins[j]<=i):
                    amt[i]=min(amt[i],1+amt[i-coins[j]])
        if amt[amount]<amount+1:
            return amt[amount]
        else:
            return -1
            
        