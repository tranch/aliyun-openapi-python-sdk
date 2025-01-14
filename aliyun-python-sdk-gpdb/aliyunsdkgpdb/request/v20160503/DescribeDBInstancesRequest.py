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
from aliyunsdkgpdb.endpoint import endpoint_data

class DescribeDBInstancesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'gpdb', '2016-05-03', 'DescribeDBInstances','gpdb')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_DBInstanceModes(self):
		return self.get_query_params().get('DBInstanceModes')

	def set_DBInstanceModes(self,DBInstanceModes):
		self.add_query_param('DBInstanceModes',DBInstanceModes)

	def get_DBInstanceStatuses(self):
		return self.get_query_params().get('DBInstanceStatuses')

	def set_DBInstanceStatuses(self,DBInstanceStatuses):
		self.add_query_param('DBInstanceStatuses',DBInstanceStatuses)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_DBInstanceDescription(self):
		return self.get_query_params().get('DBInstanceDescription')

	def set_DBInstanceDescription(self,DBInstanceDescription):
		self.add_query_param('DBInstanceDescription',DBInstanceDescription)

	def get_Tags(self):
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tags):
		for depth1 in range(len(Tags)):
			if Tags[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tags[depth1].get('Value'))
			if Tags[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tags[depth1].get('Key'))

	def get_DBInstanceIds(self):
		return self.get_query_params().get('DBInstanceIds')

	def set_DBInstanceIds(self,DBInstanceIds):
		self.add_query_param('DBInstanceIds',DBInstanceIds)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_DBInstanceCategories(self):
		return self.get_query_params().get('DBInstanceCategories')

	def set_DBInstanceCategories(self,DBInstanceCategories):
		self.add_query_param('DBInstanceCategories',DBInstanceCategories)

	def get_InstanceDeployTypes(self):
		return self.get_query_params().get('InstanceDeployTypes')

	def set_InstanceDeployTypes(self,InstanceDeployTypes):
		self.add_query_param('InstanceDeployTypes',InstanceDeployTypes)

	def get_InstanceNetworkType(self):
		return self.get_query_params().get('InstanceNetworkType')

	def set_InstanceNetworkType(self,InstanceNetworkType):
		self.add_query_param('InstanceNetworkType',InstanceNetworkType)