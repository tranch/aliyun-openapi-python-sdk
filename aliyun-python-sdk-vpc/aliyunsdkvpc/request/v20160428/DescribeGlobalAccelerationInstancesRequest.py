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
from aliyunsdkvpc.endpoint import endpoint_data

class DescribeGlobalAccelerationInstancesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'DescribeGlobalAccelerationInstances','vpc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_IpAddress(self): # String
		return self.get_query_params().get('IpAddress')

	def set_IpAddress(self, IpAddress):  # String
		self.add_query_param('IpAddress', IpAddress)
	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_BandwidthType(self): # String
		return self.get_query_params().get('BandwidthType')

	def set_BandwidthType(self, BandwidthType):  # String
		self.add_query_param('BandwidthType', BandwidthType)
	def get_IncludeReservationData(self): # Boolean
		return self.get_query_params().get('IncludeReservationData')

	def set_IncludeReservationData(self, IncludeReservationData):  # Boolean
		self.add_query_param('IncludeReservationData', IncludeReservationData)
	def get_GlobalAccelerationInstanceId(self): # String
		return self.get_query_params().get('GlobalAccelerationInstanceId')

	def set_GlobalAccelerationInstanceId(self, GlobalAccelerationInstanceId):  # String
		self.add_query_param('GlobalAccelerationInstanceId', GlobalAccelerationInstanceId)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_ServiceLocation(self): # String
		return self.get_query_params().get('ServiceLocation')

	def set_ServiceLocation(self, ServiceLocation):  # String
		self.add_query_param('ServiceLocation', ServiceLocation)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_ServerId(self): # String
		return self.get_query_params().get('ServerId')

	def set_ServerId(self, ServerId):  # String
		self.add_query_param('ServerId', ServerId)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
