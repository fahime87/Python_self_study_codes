# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: college.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='college.proto',
  package='tutorial_1',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rcollege.proto\x12\ntutorial_1\"\xe2\x05\n\x07Student\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\x13\n\x0bNational_id\x18\x02 \x02(\x05\x12/\n\x06phones\x18\x03 \x03(\x0b\x32\x1f.tutorial_1.Student.PhoneNumber\x12)\n\x08\x42irthDay\x18\x04 \x01(\x0b\x32\x17.tutorial_1.Student.Day\x12\'\n\x06Gender\x18\x05 \x01(\x0e\x32\x17.tutorial_1.Student.Sex\x12-\n\x07\x41\x64\x64ress\x18\x06 \x03(\x0b\x32\x1c.tutorial_1.Student.Location\x12)\n\x07\x43ourses\x18\x07 \x03(\x0b\x32\x18.tutorial_1.CollegCourse\x1aP\n\x0bPhoneNumber\x12\x0e\n\x06number\x18\x01 \x01(\t\x12\x31\n\x04type\x18\x02 \x01(\x0e\x32\x1d.tutorial_1.Student.PhoneType:\x04HOME\x1aO\n\x03\x44\x61y\x12\x0b\n\x03\x64\x61y\x18\x01 \x01(\x05\x12-\n\x05mount\x18\x02 \x01(\x0e\x32\x1e.tutorial_1.Student.Mount_list\x12\x0c\n\x04year\x18\x03 \x01(\x05\x1aG\n\x08Location\x12\x15\n\x07\x63ountry\x18\x01 \x01(\t:\x04iran\x12\x14\n\x04\x63ity\x18\x02 \x01(\t:\x06tehran\x12\x0e\n\x06street\x18\x03 \x01(\t\"+\n\tPhoneType\x12\n\n\x06MOBILE\x10\x00\x12\x08\n\x04HOME\x10\x01\x12\x08\n\x04WORK\x10\x02\"\x9e\x01\n\nMount_list\x12\x0b\n\x07January\x10\x01\x12\x0c\n\x08\x46\x65\x62ruary\x10\x02\x12\t\n\x05March\x10\x03\x12\t\n\x05\x41pril\x10\x04\x12\x07\n\x03May\x10\x05\x12\x08\n\x04June\x10\x06\x12\x08\n\x04July\x10\x07\x12\n\n\x06\x41ugust\x10\x08\x12\r\n\tSeptember\x10\t\x12\x0b\n\x07October\x10\n\x12\x0c\n\x08November\x10\x0b\x12\x0c\n\x08\x44\x65\x63\x65mber\x10\x0c\"\x1b\n\x03Sex\x12\x08\n\x04male\x10\x01\x12\n\n\x06\x66\x65mail\x10\x02\"\x8b\x01\n\x0c\x43ollegCourse\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0c\n\x04Name\x18\x02 \x01(\t\x12\x36\n\x04Unit\x18\x03 \x01(\x0e\x32#.tutorial_1.CollegCourse.CourseUnit:\x03one\")\n\nCourseUnit\x12\x07\n\x03one\x10\x01\x12\x07\n\x03two\x10\x02\x12\t\n\x05three\x10\x03\"a\n\x07\x63ollege\x12,\n\ncourseList\x18\r \x03(\x0b\x32\x18.tutorial_1.CollegCourse\x12(\n\x0bstudentList\x18\x0c \x03(\x0b\x32\x13.tutorial_1.Student'
)



_STUDENT_PHONETYPE = _descriptor.EnumDescriptor(
  name='PhoneType',
  full_name='tutorial_1.Student.PhoneType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MOBILE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HOME', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WORK', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=535,
  serialized_end=578,
)
_sym_db.RegisterEnumDescriptor(_STUDENT_PHONETYPE)

_STUDENT_MOUNT_LIST = _descriptor.EnumDescriptor(
  name='Mount_list',
  full_name='tutorial_1.Student.Mount_list',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='January', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='February', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='March', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='April', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='May', index=4, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='June', index=5, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='July', index=6, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='August', index=7, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='September', index=8, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='October', index=9, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='November', index=10, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='December', index=11, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=581,
  serialized_end=739,
)
_sym_db.RegisterEnumDescriptor(_STUDENT_MOUNT_LIST)

_STUDENT_SEX = _descriptor.EnumDescriptor(
  name='Sex',
  full_name='tutorial_1.Student.Sex',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='male', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='femail', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=741,
  serialized_end=768,
)
_sym_db.RegisterEnumDescriptor(_STUDENT_SEX)

_COLLEGCOURSE_COURSEUNIT = _descriptor.EnumDescriptor(
  name='CourseUnit',
  full_name='tutorial_1.CollegCourse.CourseUnit',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='one', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='two', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='three', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=869,
  serialized_end=910,
)
_sym_db.RegisterEnumDescriptor(_COLLEGCOURSE_COURSEUNIT)


_STUDENT_PHONENUMBER = _descriptor.Descriptor(
  name='PhoneNumber',
  full_name='tutorial_1.Student.PhoneNumber',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='tutorial_1.Student.PhoneNumber.number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='tutorial_1.Student.PhoneNumber.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
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
  serialized_start=299,
  serialized_end=379,
)

_STUDENT_DAY = _descriptor.Descriptor(
  name='Day',
  full_name='tutorial_1.Student.Day',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='day', full_name='tutorial_1.Student.Day.day', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mount', full_name='tutorial_1.Student.Day.mount', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='year', full_name='tutorial_1.Student.Day.year', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=381,
  serialized_end=460,
)

_STUDENT_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='tutorial_1.Student.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='country', full_name='tutorial_1.Student.Location.country', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"iran".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='city', full_name='tutorial_1.Student.Location.city', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"tehran".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='street', full_name='tutorial_1.Student.Location.street', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=462,
  serialized_end=533,
)

_STUDENT = _descriptor.Descriptor(
  name='Student',
  full_name='tutorial_1.Student',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Name', full_name='tutorial_1.Student.Name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='National_id', full_name='tutorial_1.Student.National_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phones', full_name='tutorial_1.Student.phones', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='BirthDay', full_name='tutorial_1.Student.BirthDay', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Gender', full_name='tutorial_1.Student.Gender', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Address', full_name='tutorial_1.Student.Address', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Courses', full_name='tutorial_1.Student.Courses', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_STUDENT_PHONENUMBER, _STUDENT_DAY, _STUDENT_LOCATION, ],
  enum_types=[
    _STUDENT_PHONETYPE,
    _STUDENT_MOUNT_LIST,
    _STUDENT_SEX,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=768,
)


_COLLEGCOURSE = _descriptor.Descriptor(
  name='CollegCourse',
  full_name='tutorial_1.CollegCourse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tutorial_1.CollegCourse.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Name', full_name='tutorial_1.CollegCourse.Name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Unit', full_name='tutorial_1.CollegCourse.Unit', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COLLEGCOURSE_COURSEUNIT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=771,
  serialized_end=910,
)


_COLLEGE = _descriptor.Descriptor(
  name='college',
  full_name='tutorial_1.college',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='courseList', full_name='tutorial_1.college.courseList', index=0,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='studentList', full_name='tutorial_1.college.studentList', index=1,
      number=12, type=11, cpp_type=10, label=3,
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
  serialized_start=912,
  serialized_end=1009,
)

_STUDENT_PHONENUMBER.fields_by_name['type'].enum_type = _STUDENT_PHONETYPE
_STUDENT_PHONENUMBER.containing_type = _STUDENT
_STUDENT_DAY.fields_by_name['mount'].enum_type = _STUDENT_MOUNT_LIST
_STUDENT_DAY.containing_type = _STUDENT
_STUDENT_LOCATION.containing_type = _STUDENT
_STUDENT.fields_by_name['phones'].message_type = _STUDENT_PHONENUMBER
_STUDENT.fields_by_name['BirthDay'].message_type = _STUDENT_DAY
_STUDENT.fields_by_name['Gender'].enum_type = _STUDENT_SEX
_STUDENT.fields_by_name['Address'].message_type = _STUDENT_LOCATION
_STUDENT.fields_by_name['Courses'].message_type = _COLLEGCOURSE
_STUDENT_PHONETYPE.containing_type = _STUDENT
_STUDENT_MOUNT_LIST.containing_type = _STUDENT
_STUDENT_SEX.containing_type = _STUDENT
_COLLEGCOURSE.fields_by_name['Unit'].enum_type = _COLLEGCOURSE_COURSEUNIT
_COLLEGCOURSE_COURSEUNIT.containing_type = _COLLEGCOURSE
_COLLEGE.fields_by_name['courseList'].message_type = _COLLEGCOURSE
_COLLEGE.fields_by_name['studentList'].message_type = _STUDENT
DESCRIPTOR.message_types_by_name['Student'] = _STUDENT
DESCRIPTOR.message_types_by_name['CollegCourse'] = _COLLEGCOURSE
DESCRIPTOR.message_types_by_name['college'] = _COLLEGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Student = _reflection.GeneratedProtocolMessageType('Student', (_message.Message,), {

  'PhoneNumber' : _reflection.GeneratedProtocolMessageType('PhoneNumber', (_message.Message,), {
    'DESCRIPTOR' : _STUDENT_PHONENUMBER,
    '__module__' : 'college_pb2'
    # @@protoc_insertion_point(class_scope:tutorial_1.Student.PhoneNumber)
    })
  ,

  'Day' : _reflection.GeneratedProtocolMessageType('Day', (_message.Message,), {
    'DESCRIPTOR' : _STUDENT_DAY,
    '__module__' : 'college_pb2'
    # @@protoc_insertion_point(class_scope:tutorial_1.Student.Day)
    })
  ,

  'Location' : _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), {
    'DESCRIPTOR' : _STUDENT_LOCATION,
    '__module__' : 'college_pb2'
    # @@protoc_insertion_point(class_scope:tutorial_1.Student.Location)
    })
  ,
  'DESCRIPTOR' : _STUDENT,
  '__module__' : 'college_pb2'
  # @@protoc_insertion_point(class_scope:tutorial_1.Student)
  })
_sym_db.RegisterMessage(Student)
_sym_db.RegisterMessage(Student.PhoneNumber)
_sym_db.RegisterMessage(Student.Day)
_sym_db.RegisterMessage(Student.Location)

CollegCourse = _reflection.GeneratedProtocolMessageType('CollegCourse', (_message.Message,), {
  'DESCRIPTOR' : _COLLEGCOURSE,
  '__module__' : 'college_pb2'
  # @@protoc_insertion_point(class_scope:tutorial_1.CollegCourse)
  })
_sym_db.RegisterMessage(CollegCourse)

college = _reflection.GeneratedProtocolMessageType('college', (_message.Message,), {
  'DESCRIPTOR' : _COLLEGE,
  '__module__' : 'college_pb2'
  # @@protoc_insertion_point(class_scope:tutorial_1.college)
  })
_sym_db.RegisterMessage(college)


# @@protoc_insertion_point(module_scope)
