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

class UpdateUserTagMetaRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'quickbi-public', '2022-01-01', 'UpdateUserTagMeta','2.2.0')
		self.set_method('POST')

	def get_TagName(self): # String
		return self.get_query_params().get('TagName')

	def set_TagName(self, TagName):  # String
		self.add_query_param('TagName', TagName)
	def get_TagId(self): # String
		return self.get_query_params().get('TagId')

	def set_TagId(self, TagId):  # String
		self.add_query_param('TagId', TagId)
	def get_TagDescription(self): # String
		return self.get_query_params().get('TagDescription')

	def set_TagDescription(self, TagDescription):  # String
		self.add_query_param('TagDescription', TagDescription)
