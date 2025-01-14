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

class DescribeDisksRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'DescribeDisks','ens')
		self.set_method('POST')

	def get_Type(self): # String
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_query_param('Type', Type)
	def get_OrderByParams(self): # String
		return self.get_query_params().get('OrderByParams')

	def set_OrderByParams(self, OrderByParams):  # String
		self.add_query_param('OrderByParams', OrderByParams)
	def get_DiskName(self): # String
		return self.get_query_params().get('DiskName')

	def set_DiskName(self, DiskName):  # String
		self.add_query_param('DiskName', DiskName)
	def get_DiskChargeType(self): # String
		return self.get_query_params().get('DiskChargeType')

	def set_DiskChargeType(self, DiskChargeType):  # String
		self.add_query_param('DiskChargeType', DiskChargeType)
	def get_EnsRegionId(self): # String
		return self.get_query_params().get('EnsRegionId')

	def set_EnsRegionId(self, EnsRegionId):  # String
		self.add_query_param('EnsRegionId', EnsRegionId)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
	def get_PageNumber(self): # String
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # String
		self.add_query_param('PageNumber', PageNumber)
	def get_PageSize(self): # String
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # String
		self.add_query_param('PageSize', PageSize)
	def get_DiskIds(self): # String
		return self.get_query_params().get('DiskIds')

	def set_DiskIds(self, DiskIds):  # String
		self.add_query_param('DiskIds', DiskIds)
	def get_DiskId(self): # String
		return self.get_query_params().get('DiskId')

	def set_DiskId(self, DiskId):  # String
		self.add_query_param('DiskId', DiskId)
	def get_EnsRegionIds(self): # String
		return self.get_query_params().get('EnsRegionIds')

	def set_EnsRegionIds(self, EnsRegionIds):  # String
		self.add_query_param('EnsRegionIds', EnsRegionIds)
	def get_DiskType(self): # String
		return self.get_query_params().get('DiskType')

	def set_DiskType(self, DiskType):  # String
		self.add_query_param('DiskType', DiskType)
	def get_Category(self): # String
		return self.get_query_params().get('Category')

	def set_Category(self, Category):  # String
		self.add_query_param('Category', Category)
