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

class DescribeDdosThresholdRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'antiddos-public', '2017-05-18', 'DescribeDdosThreshold')
		self.set_method('POST')

	def get_DdosType(self): # String
		return self.get_query_params().get('DdosType')

	def set_DdosType(self, DdosType):  # String
		self.add_query_param('DdosType', DdosType)
	def get_DdosRegionId(self): # String
		return self.get_query_params().get('DdosRegionId')

	def set_DdosRegionId(self, DdosRegionId):  # String
		self.add_query_param('DdosRegionId', DdosRegionId)
	def get_InstanceType(self): # String
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self, InstanceType):  # String
		self.add_query_param('InstanceType', InstanceType)
	def get_InstanceIdss(self): # RepeatList
		return self.get_query_params().get('InstanceIds')

	def set_InstanceIdss(self, InstanceIds):  # RepeatList
		for depth1 in range(len(InstanceIds)):
			self.add_query_param('InstanceIds.' + str(depth1 + 1), InstanceIds[depth1])
