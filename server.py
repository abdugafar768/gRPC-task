import grpc
import concurrent.futures
import exemple_pb2_grpc
import exemple_pb2
import sher
import time


class TestServicer(exemple_pb2_grpc.TestServiceServicer):


    def TestMethod(self, request, context):

        for j in sher.messages[request.num]:
            for i in j:
                yield exemple_pb2.PersonResponce(result=i)
                time.sleep(1) 



def serve():
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    exemple_pb2_grpc.add_TestServiceServicer_to_server(TestServicer(), server)
    server.add_insecure_port("127.0.0.1:50051")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()