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
from aliyunsdkdts.endpoint import endpoint_data

class DescribeSubscriptionMetaRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dts', '2020-01-01', 'DescribeSubscriptionMeta','dts')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Topics(self): # String
		return self.get_query_params().get('Topics')

	def set_Topics(self, Topics):  # String
		self.add_query_param('Topics', Topics)
	def get_Sid(self): # String
		return self.get_query_params().get('Sid')

	def set_Sid(self, Sid):  # String
		self.add_query_param('Sid', Sid)
	def get_SubMigrationJobIds(self): # String
		return self.get_query_params().get('SubMigrationJobIds')

	def set_SubMigrationJobIds(self, SubMigrationJobIds):  # String
		self.add_query_param('SubMigrationJobIds', SubMigrationJobIds)
	def get_DtsInstanceId(self): # String
		return self.get_query_params().get('DtsInstanceId')

	def set_DtsInstanceId(self, DtsInstanceId):  # String
		self.add_query_param('DtsInstanceId', DtsInstanceId)
