# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/map/proto/map_junction.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from modules.map.proto import map_id_pb2 as modules_dot_map_dot_proto_dot_map__id__pb2
from modules.map.proto import map_geometry_pb2 as modules_dot_map_dot_proto_dot_map__geometry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/map/proto/map_junction.proto',
  package='apollo.hdmap',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n$modules/map/proto/map_junction.proto\x12\x0c\x61pollo.hdmap\x1a\x1emodules/map/proto/map_id.proto\x1a$modules/map/proto/map_geometry.proto\"v\n\x08Junction\x12\x1c\n\x02id\x18\x01 \x01(\x0b\x32\x10.apollo.hdmap.Id\x12&\n\x07polygon\x18\x02 \x01(\x0b\x32\x15.apollo.hdmap.Polygon\x12$\n\noverlap_id\x18\x03 \x03(\x0b\x32\x10.apollo.hdmap.Id'
  ,
  dependencies=[modules_dot_map_dot_proto_dot_map__id__pb2.DESCRIPTOR,modules_dot_map_dot_proto_dot_map__geometry__pb2.DESCRIPTOR,])




_JUNCTION = _descriptor.Descriptor(
  name='Junction',
  full_name='apollo.hdmap.Junction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='apollo.hdmap.Junction.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='polygon', full_name='apollo.hdmap.Junction.polygon', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='overlap_id', full_name='apollo.hdmap.Junction.overlap_id', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=242,
)

_JUNCTION.fields_by_name['id'].message_type = modules_dot_map_dot_proto_dot_map__id__pb2._ID
_JUNCTION.fields_by_name['polygon'].message_type = modules_dot_map_dot_proto_dot_map__geometry__pb2._POLYGON
_JUNCTION.fields_by_name['overlap_id'].message_type = modules_dot_map_dot_proto_dot_map__id__pb2._ID
DESCRIPTOR.message_types_by_name['Junction'] = _JUNCTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Junction = _reflection.GeneratedProtocolMessageType('Junction', (_message.Message,), {
  'DESCRIPTOR' : _JUNCTION,
  '__module__' : 'modules.map.proto.map_junction_pb2'
  # @@protoc_insertion_point(class_scope:apollo.hdmap.Junction)
  })
_sym_db.RegisterMessage(Junction)


# @@protoc_insertion_point(module_scope)
