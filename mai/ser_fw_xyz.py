#!/usr/bin/env python3

# imports the send_INV service type from the mai package.
from example_interfaces.srv import sendINV

# import statement imports the ROS 2 Python client library, and specifically the Node class
import rclpy
from rclpy.node import Node

class SendFWService(Node):
    def __init__(self):
        # class constructor initializes the node with the name send_xyz_service
        super().__init__('send_xyz_service')
        # Then, it creates a service and defines the type, name, and callback.
        self.srv = self.create_service(sendINV, 'humanoid_fw_inv', self.send_fw_callback)

    # The definition of the service callback receives the request data and returns the sum as a response.
    def send_fw_callback(self, request, response):
        response.success = True
        self.get_logger().info('success process\nx: %f y: %f z: %f' % (request.x,request.y,request.z))

        return response

def main(args=None):
    rclpy.init(args=args)

    send_fw_service = SendFWService()

    rclpy.spin(send_fw_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()