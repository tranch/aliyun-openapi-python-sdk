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
from aliyunsdkess.endpoint import endpoint_data

class EnableScalingGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ess', '2014-08-28', 'EnableScalingGroup','ess')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ScalingGroupId(self):
		return self.get_query_params().get('ScalingGroupId')

	def set_ScalingGroupId(self,ScalingGroupId):
		self.add_query_param('ScalingGroupId',ScalingGroupId)

	def get_ActiveScalingConfigurationId(self):
		return self.get_query_params().get('ActiveScalingConfigurationId')

	def set_ActiveScalingConfigurationId(self,ActiveScalingConfigurationId):
		self.add_query_param('ActiveScalingConfigurationId',ActiveScalingConfigurationId)

	def get_LaunchTemplateId(self):
		return self.get_query_params().get('LaunchTemplateId')

	def set_LaunchTemplateId(self,LaunchTemplateId):
		self.add_query_param('LaunchTemplateId',LaunchTemplateId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_LaunchTemplateOverrides(self):
		return self.get_query_params().get('LaunchTemplateOverride')

	def set_LaunchTemplateOverrides(self, LaunchTemplateOverrides):
		for depth1 in range(len(LaunchTemplateOverrides)):
			if LaunchTemplateOverrides[depth1].get('WeightedCapacity') is not None:
				self.add_query_param('LaunchTemplateOverride.' + str(depth1 + 1) + '.WeightedCapacity', LaunchTemplateOverrides[depth1].get('WeightedCapacity'))
			if LaunchTemplateOverrides[depth1].get('InstanceType') is not None:
				self.add_query_param('LaunchTemplateOverride.' + str(depth1 + 1) + '.InstanceType', LaunchTemplateOverrides[depth1].get('InstanceType'))

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_LaunchTemplateVersion(self):
		return self.get_query_params().get('LaunchTemplateVersion')

	def set_LaunchTemplateVersion(self,LaunchTemplateVersion):
		self.add_query_param('LaunchTemplateVersion',LaunchTemplateVersion)

	def get_InstanceIds(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceIds(self, InstanceIds):
		for depth1 in range(len(InstanceIds)):
			if InstanceIds[depth1] is not None:
				self.add_query_param('InstanceId.' + str(depth1 + 1) , InstanceIds[depth1])

	def get_LoadBalancerWeights(self):
		return self.get_query_params().get('LoadBalancerWeight')

	def set_LoadBalancerWeights(self, LoadBalancerWeights):
		for depth1 in range(len(LoadBalancerWeights)):
			if LoadBalancerWeights[depth1] is not None:
				self.add_query_param('LoadBalancerWeight.' + str(depth1 + 1) , LoadBalancerWeights[depth1])