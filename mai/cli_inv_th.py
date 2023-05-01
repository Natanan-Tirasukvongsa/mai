#!/usr/bin/env python3

# The client node code uses sys.argv to get access to command line input arguments for the request.
import sys
from mai.srv import sendINV
import rclpy
from rclpy.node import Node

class SendINVClient(Node):
    def __init__(self):
        # The constructor definition creates a client with the same type 
        # and name as the service node.
        super().__init__('send_th_client')
        self.cli = self.create_client(sendINV, 'humanoid_fw_inv')
        # The while loop in the constructor checks if a service matching the type 
        # and name of the client is available once a second.
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = sendINV.Request()
    
    def send_request(self, x, y, z):
        self.req.x = x
        self.req.y = y
        self.req.z = z
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

# Below the constructor is the request definition, followed by main.
def main(args=None):
    rclpy.init(args=args)

    send_inv_client = SendINVClient()
    response = send_inv_client.send_request(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
    send_inv_client.get_logger().info(
        'input position x: %f  y: %f z: %f success: %d' %
        (float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]),response.success))

    send_inv_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()