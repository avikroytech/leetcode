class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        players = {}

        for match in matches:
            if match[0] not in players.keys():
                players[match[0]] = 0
            if match[1] not in players.keys():
                players[match[1]] = 1
            else:
                players[match[1]] += 1

        zeroLosses = []
        oneLoss = []

        for player, score in players.items():
            if score == 1:
                oneLoss.append(player)
            elif score == 0:
                zeroLosses.append(player)

        zeroLosses.sort()
        oneLoss.sort()

        return zeroLosses, oneLoss
