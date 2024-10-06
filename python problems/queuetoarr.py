class Queue:
    def __init__(self,max_size):
        self.queue=[None]*max_size
        self.front=0
        self.rear=0
        self.size=0
        self.max_size=max_size
    def push(self,x):
        if self.size==self.max_size:
           return "queue is full"
        self.queue[self.rear]=x
        self.rear=(self.rear+1)% self.max_size
        self.size+=1
    def pop(self):
        if self.size==0:
            return -1
        popped_value=self.queue[self.front]
        self.queue[self.front]==None
        self.front=(self.front+1)%self.max_size
        self.size-=1
        return popped_value
def process_queries(queries,max_size):
        q=Queue(max_size)
        result=[]
        for query in queries:
            if query[0]==1:
                q.push(query[1])
            elif query[0]==2:
                result.append(q.pop())
        return result  
Q = 5
queries = [(1, 2), (1, 3), (2,), (1, 4), (2,)]
max_size = 5 
result = process_queries(queries, max_size)

# Print the result of the pop operations
print(*result)          