# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: animalai/communicator_objects/unity_input.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from animalai.communicator_objects import unity_rl_input_pb2 as animalai_dot_communicator__objects_dot_unity__rl__input__pb2
from animalai.communicator_objects import unity_rl_initialization_input_pb2 as animalai_dot_communicator__objects_dot_unity__rl__initialization__input__pb2
from animalai.communicator_objects import unity_rl_reset_input_pb2 as animalai_dot_communicator__objects_dot_unity__rl__reset__input__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='animalai/communicator_objects/unity_input.proto',
  package='communicator_objects',
  syntax='proto3',
  serialized_options=_b('\252\002\034MLAgents.CommunicatorObjects'),
  serialized_pb=_b('\n/animalai/communicator_objects/unity_input.proto\x12\x14\x63ommunicator_objects\x1a\x32\x61nimalai/communicator_objects/unity_rl_input.proto\x1a\x41\x61nimalai/communicator_objects/unity_rl_initialization_input.proto\x1a\x38\x61nimalai/communicator_objects/unity_rl_reset_input.proto\"\xd6\x01\n\nUnityInput\x12\x34\n\x08rl_input\x18\x01 \x01(\x0b\x32\".communicator_objects.UnityRLInput\x12Q\n\x17rl_initialization_input\x18\x02 \x01(\x0b\x32\x30.communicator_objects.UnityRLInitializationInput\x12?\n\x0erl_reset_input\x18\x03 \x01(\x0b\x32\'.communicator_objects.UnityRLResetInputB\x1f\xaa\x02\x1cMLAgents.CommunicatorObjectsb\x06proto3')
  ,
  dependencies=[animalai_dot_communicator__objects_dot_unity__rl__input__pb2.DESCRIPTOR,animalai_dot_communicator__objects_dot_unity__rl__initialization__input__pb2.DESCRIPTOR,animalai_dot_communicator__objects_dot_unity__rl__reset__input__pb2.DESCRIPTOR,])




_UNITYINPUT = _descriptor.Descriptor(
  name='UnityInput',
  full_name='communicator_objects.UnityInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rl_input', full_name='communicator_objects.UnityInput.rl_input', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rl_initialization_input', full_name='communicator_objects.UnityInput.rl_initialization_input', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rl_reset_input', full_name='communicator_objects.UnityInput.rl_reset_input', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=251,
  serialized_end=465,
)

_UNITYINPUT.fields_by_name['rl_input'].message_type = animalai_dot_communicator__objects_dot_unity__rl__input__pb2._UNITYRLINPUT
_UNITYINPUT.fields_by_name['rl_initialization_input'].message_type = animalai_dot_communicator__objects_dot_unity__rl__initialization__input__pb2._UNITYRLINITIALIZATIONINPUT
_UNITYINPUT.fields_by_name['rl_reset_input'].message_type = animalai_dot_communicator__objects_dot_unity__rl__reset__input__pb2._UNITYRLRESETINPUT
DESCRIPTOR.message_types_by_name['UnityInput'] = _UNITYINPUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UnityInput = _reflection.GeneratedProtocolMessageType('UnityInput', (_message.Message,), {
  'DESCRIPTOR' : _UNITYINPUT,
  '__module__' : 'animalai.communicator_objects.unity_input_pb2'
  # @@protoc_insertion_point(class_scope:communicator_objects.UnityInput)
  })
_sym_db.RegisterMessage(UnityInput)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
