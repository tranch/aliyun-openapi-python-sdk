# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest

class UpdateSavedQueryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ResourceCenter', '2022-12-01', 'UpdateSavedQuery')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_Expression(self): # String
		return self.get_query_params().get('Expression')

	def set_Expression(self, Expression):  # String
		self.add_query_param('Expression', Expression)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_QueryId(self): # String
		return self.get_query_params().get('QueryId')

	def set_QueryId(self, QueryId):  # String
		self.add_query_param('QueryId', QueryId)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
