import grpc
import greet_pb2_grpc
import greet_pb2

def run():
    # Connect to the server
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)
        
        # Call the SayHello method
        name = "James"  # Example input
        response = stub.SayHello(greet_pb2.HelloRequest(name=name))
        print(f"Server responded: {response.message}")

if __name__ == "__main__":
    run()
