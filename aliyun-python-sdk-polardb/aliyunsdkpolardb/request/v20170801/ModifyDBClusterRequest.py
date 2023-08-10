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
from aliyunsdkpolardb.endpoint import endpoint_data

class ModifyDBClusterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'polardb', '2017-08-01', 'ModifyDBCluster','polardb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_StandbyHAMode(self): # String
		return self.get_query_params().get('StandbyHAMode')

	def set_StandbyHAMode(self, StandbyHAMode):  # String
		self.add_query_param('StandbyHAMode', StandbyHAMode)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_DBClusterId(self): # String
		return self.get_query_params().get('DBClusterId')

	def set_DBClusterId(self, DBClusterId):  # String
		self.add_query_param('DBClusterId', DBClusterId)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_FaultSimulateMode(self): # String
		return self.get_query_params().get('FaultSimulateMode')

	def set_FaultSimulateMode(self, FaultSimulateMode):  # String
		self.add_query_param('FaultSimulateMode', FaultSimulateMode)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_StorageUpperBound(self): # Long
		return self.get_query_params().get('StorageUpperBound')

	def set_StorageUpperBound(self, StorageUpperBound):  # Long
		self.add_query_param('StorageUpperBound', StorageUpperBound)
	def get_StorageAutoScale(self): # String
		return self.get_query_params().get('StorageAutoScale')

	def set_StorageAutoScale(self, StorageAutoScale):  # String
		self.add_query_param('StorageAutoScale', StorageAutoScale)
	def get_DataSyncMode(self): # String
		return self.get_query_params().get('DataSyncMode')

	def set_DataSyncMode(self, DataSyncMode):  # String
		self.add_query_param('DataSyncMode', DataSyncMode)
