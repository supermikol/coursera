# python3

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time_ = []

    def Process(self, request):
        # write your code here
        finish_length = len(self.finish_time_)
        if finish_length < self.size:
            if finish_length == 0:
                finish_time = request.arrival_time + request.process_time
            else:
                finish_time = max(self.finish_time_[-1] + request.process_time, request.arrival_time + request.process_time)
            self.finish_time_.append(finish_time)
            return Response(False, finish_time - request.process_time)
        else:
            if request.arrival_time >= self.finish_time_[-self.size]:
                finish_time = max(self.finish_time_[-1] + request.process_time, request.arrival_time + request.process_time)
                self.finish_time_.append(finish_time)
                return Response(False, finish_time - request.process_time)
            else:
                return Response(True, -1)
        # return Response(False, -1)

def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count) #array of every line in Request format(arrival time/process time)

    buffer = Buffer(size) #not sure what Process method is doing...yet
    responses = ProcessRequests(requests, buffer)#returns array of all the individual requests processed by buffer.process

    PrintResponses(responses)#prints each processed item after calling #starttime method on it (unless response.dropped, in which case print -1)
