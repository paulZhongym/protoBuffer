# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: book.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nbook.proto\x12\x02\x61\x33\"\x99\x01\n\x04\x42ook\x12\x0c\n\x04isbn\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x1d\n\x05genre\x18\x04 \x01(\x0e\x32\x0e.a3.Book.Genre\x12\x0c\n\x04year\x18\x05 \x01(\x05\"7\n\x05Genre\x12\x0b\n\x07\x46ICTION\x10\x00\x12\x0b\n\x07ROMANCE\x10\x01\x12\x08\n\x04WORK\x10\x02\x12\n\n\x06SCHOOL\x10\x03\"\x8b\x01\n\rInventoryItem\x12\n\n\x02pk\x18\x01 \x01(\t\x12\x18\n\x04\x62ook\x18\x02 \x01(\x0b\x32\x08.a3.BookH\x00\x12(\n\x06status\x18\x03 \x01(\x0e\x32\x18.a3.InventoryItem.Status\"\"\n\x06Status\x12\r\n\tAVAILABLE\x10\x00\x12\t\n\x05TAKEN\x10\x01\x42\x06\n\x04item\"+\n\x11\x43reateBookRequest\x12\x16\n\x04\x62ook\x18\x01 \x01(\x0b\x32\x08.a3.Book\"%\n\x12\x43reateBookResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1e\n\x0eGetBookRequest\x12\x0c\n\x04isbn\x18\x01 \x01(\t\")\n\x0fGetBookResponse\x12\x16\n\x04\x62ook\x18\x01 \x01(\x0b\x32\x08.a3.Book2\x83\x01\n\x10InventoryService\x12;\n\nCreateBook\x12\x15.a3.CreateBookRequest\x1a\x16.a3.CreateBookResponse\x12\x32\n\x07GetBook\x12\x12.a3.GetBookRequest\x1a\x13.a3.GetBookResponse')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'book_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BOOK._serialized_start=19
  _BOOK._serialized_end=172
  _BOOK_GENRE._serialized_start=117
  _BOOK_GENRE._serialized_end=172
  _INVENTORYITEM._serialized_start=175
  _INVENTORYITEM._serialized_end=314
  _INVENTORYITEM_STATUS._serialized_start=272
  _INVENTORYITEM_STATUS._serialized_end=306
  _CREATEBOOKREQUEST._serialized_start=316
  _CREATEBOOKREQUEST._serialized_end=359
  _CREATEBOOKRESPONSE._serialized_start=361
  _CREATEBOOKRESPONSE._serialized_end=398
  _GETBOOKREQUEST._serialized_start=400
  _GETBOOKREQUEST._serialized_end=430
  _GETBOOKRESPONSE._serialized_start=432
  _GETBOOKRESPONSE._serialized_end=473
  _INVENTORYSERVICE._serialized_start=476
  _INVENTORYSERVICE._serialized_end=607
# @@protoc_insertion_point(module_scope)
