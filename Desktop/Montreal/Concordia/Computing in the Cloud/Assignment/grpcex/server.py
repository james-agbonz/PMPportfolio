from concurrent import futures
import grpc
import greet_pb2_grpc
import greet_pb2

# Implement the service defined in the proto file
class Greeter(greet_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        # Business logic for the SayHello RPC
        print(f"Received request from: {request.name}")
        return greet_pb2.HelloReply(message=f"Hello, {request.name}!")

# Set up the server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greet_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("[::]:50051")  # Listen on port 50051
    print("Server is running on port 50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
