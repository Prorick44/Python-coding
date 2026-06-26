class Job:
  def __init__(self, id, deadline, profit):
    self.id = id 
    self.deadline = deadline 
    self.profit = profit 
  
def job_sequencing(jobs):
  jobs.sort(key=lambda x : x.profit, reverse=True)

  max_deadline = max(job.deadline for job in jobs)
  slots = [-1] * (max_deadline + 1)

  profit = 0 

  for job in jobs:
    for j in range(job.deadline, 0, -1):
      if slots[j] == -1:
        slots[j] = job.id 
        profit += job.profit 
        break 
  
  return profit 

jobs = [
  Job(1,2,100),
  Job(2,1,19),
  Job(3,2,27),
  Job(4,1,25),
  Job(5,3,15)
]

print(job_sequencing(jobs))
