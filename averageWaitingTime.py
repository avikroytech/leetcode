class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        waiting_times = []
        current_time = customers[0][0]

        for customer in customers:
            waiting_time = customer[1]
            if current_time > customer[0]:
                waiting_time += current_time - customer[0]
            else:
                current_time += customer[0] - current_time
            
            waiting_times.append(waiting_time)
            current_time += customer[1]
        
        return sum(waiting_times) / len(waiting_times)
