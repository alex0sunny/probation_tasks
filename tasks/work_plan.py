# 1147 · Work Plan  Medium

# Xiaomei is the manager in charge of the team and needs to make the work plans for the team to 
# help the team generate the most value. Every week, the team will have alternative tasks, 
# one is a simple task, and the other is a complex task. In week i, the value of the team’s 
# completion of simple tasks is low[i], and the value of completion of complex tasks 
# is high[i]. Due to the technical difficulty of the complex task itself, if the 
# team chooses to perform the complex task in week i, they need to concentrate on preparation 
# without doing any task in week i-1. If the team choose to perform a simple task in week i, 
# there is no need to make any preparations in advance. Now that Xiaomei's team has received 
# a list of expected tasks for the next n weeks, please help Xiaomei determine 
# the weekly work schedule that help the team generate the most value.

# Example 1:

# Input:low=[4,2,3,7],hard=[3,5,6,9]
# output:17
# Explanation:
# Pick simple task in the first week, value = 4
# Prepare for the second week and pick complex task in the third week, value = 4 + 6 = 10
# Pick a simple task in the fourth week, value = 10 + 7 = 17

# Example 2:

# Input:low=[1,3,5,9],high=[3,5,7,9]
# Output:19

def workPlan(low, high):
  dp = [low[0]] + [0] * (len(low) - 1)
  for i in range(1, len(low)):
    dp[i] = max(dp[i-1] + low[i], dp[i-2] + high[i])
  return dp[-1]
