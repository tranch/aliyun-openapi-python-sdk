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
from aliyunsdkfacebody.endpoint import endpoint_data

class ListBodyPersonRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'facebody', '2019-12-30', 'ListBodyPerson','facebody')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Limit(self): # Long
		return self.get_query_params().get('Limit')

	def set_Limit(self, Limit):  # Long
		self.add_query_param('Limit', Limit)
	def get_Offset(self): # Long
		return self.get_query_params().get('Offset')

	def set_Offset(self, Offset):  # Long
		self.add_query_param('Offset', Offset)
	def get_DbId(self): # Long
		return self.get_query_params().get('DbId')

	def set_DbId(self, DbId):  # Long
		self.add_query_param('DbId', DbId)
