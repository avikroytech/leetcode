class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        townJudge = None
        if len(trust) == n:
            townJudge = -1
        elif len(trust) == 0 and n == 1:
            townJudge = 1
        elif len(trust) == 0 and n > 1:
            townJudge = -1

        trustRelationships = {}

        for person in trust:
            if person[0] in trustRelationships.keys():
                trustRelationships[person[0]].append(person[1])
            else:
                trustRelationships[person[0]] = [person[1]]
        
        if len(trustRelationships.keys()) == n:
            return -1
        elif len(trustRelationships.keys()) == 0 and n == 1:
            return 1
        elif len(trustRelationships.keys()) == 0 and n > 1:
            return -1
        elif len(trustRelationships.keys()) != n - 1:
            return -1

        people = {}

        for person, trust in trustRelationships.items():
            for person in trust:
                if person in people.keys():
                    people[person] += 1
                else:
                    people[person] = 1

        count = 0

        for person, num in people.items():
            if num > count:
                townJudge = person
                count = num
            elif num == count:
                townJudge = -1
        
        if count != n-1:
            return -1

        return townJudge
