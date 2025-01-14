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
from aliyunsdkobjectdet.endpoint import endpoint_data

class DetectVideoFrameRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'objectdet', '2019-12-30', 'DetectVideoFrame','objectdet')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Features(self):
		return self.get_body_params().get('Features')

	def set_Features(self,Features):
		self.add_body_params('Features', Features)

	def get_Height(self):
		return self.get_body_params().get('Height')

	def set_Height(self,Height):
		self.add_body_params('Height', Height)

	def get_CreateTime(self):
		return self.get_body_params().get('CreateTime')

	def set_CreateTime(self,CreateTime):
		self.add_body_params('CreateTime', CreateTime)

	def get_FeatureConfig(self):
		return self.get_body_params().get('FeatureConfig')

	def set_FeatureConfig(self,FeatureConfig):
		self.add_body_params('FeatureConfig', FeatureConfig)

	def get_OwnerId(self):
		return self.get_body_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_body_params('OwnerId', OwnerId)

	def get_StreamArn(self):
		return self.get_body_params().get('StreamArn')

	def set_StreamArn(self,StreamArn):
		self.add_body_params('StreamArn', StreamArn)

	def get_ImageURL(self):
		return self.get_body_params().get('ImageURL')

	def set_ImageURL(self,ImageURL):
		self.add_body_params('ImageURL', ImageURL)

	def get_Width(self):
		return self.get_body_params().get('Width')

	def set_Width(self,Width):
		self.add_body_params('Width', Width)