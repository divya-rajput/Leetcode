#Complexity analysis 
#Time complexity- O(n) Space complexity- O(k), whaere k is length of teams.
def tournamentWinner(competitions, results):
    teams = dict()
    for i in range(len(results)):
          if results[i] == 0:
               if competitions[i][1] not in teams:
                    teams[competitions[i][1]] = 3
               else:
                    teams[competitions[i][1]] += 3
          else:
               if competitions[i][0] not in teams:
                    teams[competitions[i][0]] = 3
               else:
                    teams[competitions[i][0]] += 3
    maximum, max_key = 0, None
    for k in teams:
        if teams[k] > maximum:
            maximum = teams[k]
            max_key = k
    return max_key
               









