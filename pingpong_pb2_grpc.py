# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import pingpong_pb2 as pingpong__pb2


class PingPongServiceStub(object):

  def __init__(self, channel):

    self.ping = channel.unary_unary(
        '/PingPongService/ping',
        request_serializer=pingpong__pb2.Ping.SerializeToString,
        response_deserializer=pingpong__pb2.Pong.FromString,
        )


class PingPongServiceServicer(object):

  def ping(self, request, context):

    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PingPongServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ping': grpc.unary_unary_rpc_method_handler(
          servicer.ping,
          request_deserializer=pingpong__pb2.Ping.FromString,
          response_serializer=pingpong__pb2.Pong.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'PingPongService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))