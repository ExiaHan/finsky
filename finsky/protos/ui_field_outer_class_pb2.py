# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ui_field_outer_class.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ui_field_outer_class.proto',
  package='UiFieldOuterClass',
  syntax='proto2',
  serialized_pb=_b('\n\x1aui_field_outer_class.proto\x12\x11UiFieldOuterClass\"1\n\x0cUiFieldValue\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bstringValue\x18\x02 \x01(\t\"\xe0\x02\n\x07UiField\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nisOptional\x18\x03 \x01(\x08\x12\r\n\x05label\x18\x04 \x01(\t\x12\x37\n\ttextField\x18\x06 \x01(\x0b\x32$.UiFieldOuterClass.UiField.TextField\x12\x12\n\nisDisabled\x18\x0b \x01(\x08\x1a\xd6\x01\n\tTextField\x12\x11\n\tmaxLength\x18\x02 \x01(\x05\x12\x16\n\x0ekeyboardLayout\x18\x04 \x01(\x05\x12\x43\n\nvalidation\x18\x05 \x03(\x0b\x32/.UiFieldOuterClass.UiField.TextField.Validation\x12\x14\n\x0cinitialValue\x18\x06 \x01(\t\x12\x10\n\x08isMasked\x18\x08 \x01(\x08\x1a\x31\n\nValidation\x12\r\n\x05regex\x18\x01 \x01(\t\x12\x14\n\x0c\x65rrorMessage\x18\x02 \x01(\tBW\nBcom.google.commerce.payments.orchestration.proto.ui.common.genericB\x11UiFieldOuterClass')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_UIFIELDVALUE = _descriptor.Descriptor(
  name='UiFieldValue',
  full_name='UiFieldOuterClass.UiFieldValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='UiFieldOuterClass.UiFieldValue.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stringValue', full_name='UiFieldOuterClass.UiFieldValue.stringValue', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=98,
)


_UIFIELD_TEXTFIELD_VALIDATION = _descriptor.Descriptor(
  name='Validation',
  full_name='UiFieldOuterClass.UiField.TextField.Validation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='regex', full_name='UiFieldOuterClass.UiField.TextField.Validation.regex', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='errorMessage', full_name='UiFieldOuterClass.UiField.TextField.Validation.errorMessage', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=404,
  serialized_end=453,
)

_UIFIELD_TEXTFIELD = _descriptor.Descriptor(
  name='TextField',
  full_name='UiFieldOuterClass.UiField.TextField',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='maxLength', full_name='UiFieldOuterClass.UiField.TextField.maxLength', index=0,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keyboardLayout', full_name='UiFieldOuterClass.UiField.TextField.keyboardLayout', index=1,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='validation', full_name='UiFieldOuterClass.UiField.TextField.validation', index=2,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='initialValue', full_name='UiFieldOuterClass.UiField.TextField.initialValue', index=3,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isMasked', full_name='UiFieldOuterClass.UiField.TextField.isMasked', index=4,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_UIFIELD_TEXTFIELD_VALIDATION, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=239,
  serialized_end=453,
)

_UIFIELD = _descriptor.Descriptor(
  name='UiField',
  full_name='UiFieldOuterClass.UiField',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='UiFieldOuterClass.UiField.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isOptional', full_name='UiFieldOuterClass.UiField.isOptional', index=1,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label', full_name='UiFieldOuterClass.UiField.label', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='textField', full_name='UiFieldOuterClass.UiField.textField', index=3,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isDisabled', full_name='UiFieldOuterClass.UiField.isDisabled', index=4,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_UIFIELD_TEXTFIELD, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=453,
)

_UIFIELD_TEXTFIELD_VALIDATION.containing_type = _UIFIELD_TEXTFIELD
_UIFIELD_TEXTFIELD.fields_by_name['validation'].message_type = _UIFIELD_TEXTFIELD_VALIDATION
_UIFIELD_TEXTFIELD.containing_type = _UIFIELD
_UIFIELD.fields_by_name['textField'].message_type = _UIFIELD_TEXTFIELD
DESCRIPTOR.message_types_by_name['UiFieldValue'] = _UIFIELDVALUE
DESCRIPTOR.message_types_by_name['UiField'] = _UIFIELD

UiFieldValue = _reflection.GeneratedProtocolMessageType('UiFieldValue', (_message.Message,), dict(
  DESCRIPTOR = _UIFIELDVALUE,
  __module__ = 'ui_field_outer_class_pb2'
  # @@protoc_insertion_point(class_scope:UiFieldOuterClass.UiFieldValue)
  ))
_sym_db.RegisterMessage(UiFieldValue)

UiField = _reflection.GeneratedProtocolMessageType('UiField', (_message.Message,), dict(

  TextField = _reflection.GeneratedProtocolMessageType('TextField', (_message.Message,), dict(

    Validation = _reflection.GeneratedProtocolMessageType('Validation', (_message.Message,), dict(
      DESCRIPTOR = _UIFIELD_TEXTFIELD_VALIDATION,
      __module__ = 'ui_field_outer_class_pb2'
      # @@protoc_insertion_point(class_scope:UiFieldOuterClass.UiField.TextField.Validation)
      ))
    ,
    DESCRIPTOR = _UIFIELD_TEXTFIELD,
    __module__ = 'ui_field_outer_class_pb2'
    # @@protoc_insertion_point(class_scope:UiFieldOuterClass.UiField.TextField)
    ))
  ,
  DESCRIPTOR = _UIFIELD,
  __module__ = 'ui_field_outer_class_pb2'
  # @@protoc_insertion_point(class_scope:UiFieldOuterClass.UiField)
  ))
_sym_db.RegisterMessage(UiField)
_sym_db.RegisterMessage(UiField.TextField)
_sym_db.RegisterMessage(UiField.TextField.Validation)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\nBcom.google.commerce.payments.orchestration.proto.ui.common.genericB\021UiFieldOuterClass'))
# @@protoc_insertion_point(module_scope)
