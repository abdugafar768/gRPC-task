import exemple_pb2_grpc
import exemple_pb2
import grpc
import sher


channel = grpc.insecure_channel('127.0.0.1:50051')
stub = exemple_pb2_grpc.TestServiceStub(channel)

while True:

    j = 0 
    for i in range(len(sher.messages)):
        print(i, " <-----> ",sher.name[j])
        j += 1
    try:
        request = exemple_pb2.PresonRequest(num=int('Enter a number: '))

        response_stream = stub.TestMethod(request)
        for response in response_stream:
            print('--->', response.result)

    except grpc.RpcError as e:
        print(e.details())
    except ValueError as e:
        print('cant convert symbol to number')
