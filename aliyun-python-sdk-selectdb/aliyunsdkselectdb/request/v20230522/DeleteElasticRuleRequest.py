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

class DeleteElasticRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'selectdb', '2023-05-22', 'DeleteElasticRule')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_Product(self): # String
		return self.get_query_params().get('Product')

	def set_Product(self, Product):  # String
		self.add_query_param('Product', Product)
	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_DbInstanceId(self): # String
		return self.get_query_params().get('DbInstanceId')

	def set_DbInstanceId(self, DbInstanceId):  # String
		self.add_query_param('DbInstanceId', DbInstanceId)
	def get_RuleId(self): # Long
		return self.get_query_params().get('RuleId')

	def set_RuleId(self, RuleId):  # Long
		self.add_query_param('RuleId', RuleId)
