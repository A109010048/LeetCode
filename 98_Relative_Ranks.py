class Solution(object):
    def findRelativeRanks(self, score):
        sorted_score = sorted(score)
        sorted_score = sorted_score[::-1]
  
        for i in range(len(score)):
            score[i] = sorted_score.index(score[i]) + 1
            if score[i] == 1:
                score[i] = "Gold Medal"
            elif score[i] == 2:
                score[i] = "Silver Medal"
            elif score[i] == 3:
                score[i] = "Bronze Medal"
            else:
                score[i] = str(score[i])

        return score