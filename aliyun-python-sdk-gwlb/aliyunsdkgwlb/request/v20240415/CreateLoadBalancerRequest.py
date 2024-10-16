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

class CreateLoadBalancerRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Gwlb', '2024-04-15', 'CreateLoadBalancer')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_ClientToken(self): # String
		return self.get_body_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_body_params('ClientToken', ClientToken)
	def get_AddressIpVersion(self): # String
		return self.get_body_params().get('AddressIpVersion')

	def set_AddressIpVersion(self, AddressIpVersion):  # String
		self.add_body_params('AddressIpVersion', AddressIpVersion)
	def get_ResourceGroupId(self): # String
		return self.get_body_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_body_params('ResourceGroupId', ResourceGroupId)
	def get_LoadBalancerName(self): # String
		return self.get_body_params().get('LoadBalancerName')

	def set_LoadBalancerName(self, LoadBalancerName):  # String
		self.add_body_params('LoadBalancerName', LoadBalancerName)
	def get_Tag(self): # Array
		return self.get_body_params().get('Tag')

	def set_Tag(self, Tag):  # Array
		for index1, value1 in enumerate(Tag):
			if value1.get('Key') is not None:
				self.add_body_params('Tag.' + str(index1 + 1) + '.Key', value1.get('Key'))
			if value1.get('Value') is not None:
				self.add_body_params('Tag.' + str(index1 + 1) + '.Value', value1.get('Value'))
	def get_DryRun(self): # Boolean
		return self.get_body_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_body_params('DryRun', DryRun)
	def get_ZoneMappings(self): # Array
		return self.get_body_params().get('ZoneMappings')

	def set_ZoneMappings(self, ZoneMappings):  # Array
		for index1, value1 in enumerate(ZoneMappings):
			if value1.get('VSwitchId') is not None:
				self.add_body_params('ZoneMappings.' + str(index1 + 1) + '.VSwitchId', value1.get('VSwitchId'))
			if value1.get('ZoneId') is not None:
				self.add_body_params('ZoneMappings.' + str(index1 + 1) + '.ZoneId', value1.get('ZoneId'))
	def get_VpcId(self): # String
		return self.get_body_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_body_params('VpcId', VpcId)
