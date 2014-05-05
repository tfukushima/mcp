# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: containerizer.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import mesos_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='containerizer.proto',
  package='mesos.containerizer',
  serialized_pb='\n\x13\x63ontainerizer.proto\x12\x13mesos.containerizer\x1a\x0bmesos.proto\"\xec\x01\n\x06Launch\x12(\n\x0c\x63ontainer_id\x18\x01 \x02(\x0b\x32\x12.mesos.ContainerID\x12\"\n\ttask_info\x18\x02 \x01(\x0b\x32\x0f.mesos.TaskInfo\x12*\n\rexecutor_info\x18\x03 \x01(\x0b\x32\x13.mesos.ExecutorInfo\x12\x11\n\tdirectory\x18\x04 \x01(\t\x12\x0c\n\x04user\x18\x05 \x01(\t\x12 \n\x08slave_id\x18\x06 \x01(\x0b\x32\x0e.mesos.SlaveID\x12\x11\n\tslave_pid\x18\x07 \x01(\t\x12\x12\n\ncheckpoint\x18\x08 \x01(\x08\"V\n\x06Update\x12(\n\x0c\x63ontainer_id\x18\x01 \x02(\x0b\x32\x12.mesos.ContainerID\x12\"\n\tresources\x18\x02 \x03(\x0b\x32\x0f.mesos.Resource\"0\n\x04Wait\x12(\n\x0c\x63ontainer_id\x18\x01 \x02(\x0b\x32\x12.mesos.ContainerID\"3\n\x07\x44\x65stroy\x12(\n\x0c\x63ontainer_id\x18\x01 \x02(\x0b\x32\x12.mesos.ContainerID\"1\n\x05Usage\x12(\n\x0c\x63ontainer_id\x18\x01 \x02(\x0b\x32\x12.mesos.ContainerID\">\n\x0bTermination\x12\x0e\n\x06killed\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x02(\t\x12\x0e\n\x06status\x18\x03 \x01(\x05\x42(\n\x1eorg.apache.mesos.containerizerB\x06Protos')




_LAUNCH = _descriptor.Descriptor(
  name='Launch',
  full_name='mesos.containerizer.Launch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='container_id', full_name='mesos.containerizer.Launch.container_id', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='task_info', full_name='mesos.containerizer.Launch.task_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='executor_info', full_name='mesos.containerizer.Launch.executor_info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='directory', full_name='mesos.containerizer.Launch.directory', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user', full_name='mesos.containerizer.Launch.user', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='slave_id', full_name='mesos.containerizer.Launch.slave_id', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='slave_pid', full_name='mesos.containerizer.Launch.slave_pid', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='checkpoint', full_name='mesos.containerizer.Launch.checkpoint', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=58,
  serialized_end=294,
)


_UPDATE = _descriptor.Descriptor(
  name='Update',
  full_name='mesos.containerizer.Update',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='container_id', full_name='mesos.containerizer.Update.container_id', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resources', full_name='mesos.containerizer.Update.resources', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=296,
  serialized_end=382,
)


_WAIT = _descriptor.Descriptor(
  name='Wait',
  full_name='mesos.containerizer.Wait',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='container_id', full_name='mesos.containerizer.Wait.container_id', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=384,
  serialized_end=432,
)


_DESTROY = _descriptor.Descriptor(
  name='Destroy',
  full_name='mesos.containerizer.Destroy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='container_id', full_name='mesos.containerizer.Destroy.container_id', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=434,
  serialized_end=485,
)


_USAGE = _descriptor.Descriptor(
  name='Usage',
  full_name='mesos.containerizer.Usage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='container_id', full_name='mesos.containerizer.Usage.container_id', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=487,
  serialized_end=536,
)


_TERMINATION = _descriptor.Descriptor(
  name='Termination',
  full_name='mesos.containerizer.Termination',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='killed', full_name='mesos.containerizer.Termination.killed', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='mesos.containerizer.Termination.message', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='mesos.containerizer.Termination.status', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=538,
  serialized_end=600,
)

_LAUNCH.fields_by_name['container_id'].message_type = mesos_pb2._CONTAINERID
_LAUNCH.fields_by_name['task_info'].message_type = mesos_pb2._TASKINFO
_LAUNCH.fields_by_name['executor_info'].message_type = mesos_pb2._EXECUTORINFO
_LAUNCH.fields_by_name['slave_id'].message_type = mesos_pb2._SLAVEID
_UPDATE.fields_by_name['container_id'].message_type = mesos_pb2._CONTAINERID
_UPDATE.fields_by_name['resources'].message_type = mesos_pb2._RESOURCE
_WAIT.fields_by_name['container_id'].message_type = mesos_pb2._CONTAINERID
_DESTROY.fields_by_name['container_id'].message_type = mesos_pb2._CONTAINERID
_USAGE.fields_by_name['container_id'].message_type = mesos_pb2._CONTAINERID
DESCRIPTOR.message_types_by_name['Launch'] = _LAUNCH
DESCRIPTOR.message_types_by_name['Update'] = _UPDATE
DESCRIPTOR.message_types_by_name['Wait'] = _WAIT
DESCRIPTOR.message_types_by_name['Destroy'] = _DESTROY
DESCRIPTOR.message_types_by_name['Usage'] = _USAGE
DESCRIPTOR.message_types_by_name['Termination'] = _TERMINATION

class Launch(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LAUNCH

  # @@protoc_insertion_point(class_scope:mesos.containerizer.Launch)

class Update(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _UPDATE

  # @@protoc_insertion_point(class_scope:mesos.containerizer.Update)

class Wait(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _WAIT

  # @@protoc_insertion_point(class_scope:mesos.containerizer.Wait)

class Destroy(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DESTROY

  # @@protoc_insertion_point(class_scope:mesos.containerizer.Destroy)

class Usage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _USAGE

  # @@protoc_insertion_point(class_scope:mesos.containerizer.Usage)

class Termination(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TERMINATION

  # @@protoc_insertion_point(class_scope:mesos.containerizer.Termination)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\036org.apache.mesos.containerizerB\006Protos')
# @@protoc_insertion_point(module_scope)
