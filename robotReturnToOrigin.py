class Solution:
    def judgeCircle(self, moves: str) -> bool:
        current = [0,0]

        for move in moves:
            match move:
                case "U":
                    current[1] += 1
                case "D":
                    current[1] -= 1
                case "L":
                    current[0] -= 1
                case"R":
                    current[0] += 1
        
        return current == [0,0]