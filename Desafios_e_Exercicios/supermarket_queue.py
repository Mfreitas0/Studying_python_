"""
There is a queue for the self-checkout tills at the supermarket. Your task is write a
function to calculate the total time required for all the customers to check out!

input
customers: an array of positive integers representing the queue. Each integer represents a 
customer, and its value is the amount of time they require to check out.

n: a positive integer, the number of checkout tills. 
"""

def queue_time(customers, n):
    ls = [0] * n
    for i in customers:
        ls = sorted(ls)
        ls[0] += i
    return max(ls)

print(queue_time([2], 5)) #2
print(queue_time([5], 1)) #5
print(queue_time([1,2,3,4,5], 1) )#15
print(queue_time([1,2,3,4,5], 100) )#5
print(queue_time([2,2,3,3,4,4], 2))#9