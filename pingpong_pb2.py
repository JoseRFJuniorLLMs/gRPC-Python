# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pingpong.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
  name='pingpong.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0epingpong.proto\"\x15\n\x04Ping\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\"\x15\n\x04Pong\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\x32)\n\x0fPingPongService\x12\x16\n\x04ping\x12\x05.Ping\x1a\x05.Pong\"\x00\x62\x06proto3')
)

_PING = _descriptor.Descriptor(
  name='Ping',
  full_name='Ping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='Ping.count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=39,
)


_PONG = _descriptor.Descriptor(
  name='Pong',
  full_name='Pong',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='Pong.count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=62,
)

DESCRIPTOR.message_types_by_name['Ping'] = _PING
DESCRIPTOR.message_types_by_name['Pong'] = _PONG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Ping = _reflection.GeneratedProtocolMessageType('Ping', (_message.Message,), dict(
  DESCRIPTOR = _PING,
  __module__ = 'pingpong_pb2'
  # @@protoc_insertion_point(class_scope:Ping)
  ))
_sym_db.RegisterMessage(Ping)

Pong = _reflection.GeneratedProtocolMessageType('Pong', (_message.Message,), dict(
  DESCRIPTOR = _PONG,
  __module__ = 'pingpong_pb2'
  # @@protoc_insertion_point(class_scope:Pong)
  ))
_sym_db.RegisterMessage(Pong)



_PINGPONGSERVICE = _descriptor.ServiceDescriptor(
  name='PingPongService',
  full_name='PingPongService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=64,
  serialized_end=105,
  methods=[
  _descriptor.MethodDescriptor(
    name='ping',
    full_name='PingPongService.ping',
    index=0,
    containing_service=None,
    input_type=_PING,
    output_type=_PONG,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PINGPONGSERVICE)

DESCRIPTOR.services_by_name['PingPongService'] = _PINGPONGSERVICE

# @@protoc_insertion_point(module_scope)
