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

class DescribeImageCachesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Eci', '2018-08-08', 'DescribeImageCaches','eci')

	def get_ImageCacheId(self):
		return self.get_query_params().get('ImageCacheId')

	def set_ImageCacheId(self,ImageCacheId):
		self.add_query_param('ImageCacheId',ImageCacheId)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_SnapshotId(self):
		return self.get_query_params().get('SnapshotId')

	def set_SnapshotId(self,SnapshotId):
		self.add_query_param('SnapshotId',SnapshotId)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):
		self.add_query_param('ResourceGroupId', ResourceGroupId)

	def get_ImageCacheName(self):
		return self.get_query_params().get('ImageCacheName')

	def set_ImageCacheName(self,ImageCacheName):
		self.add_query_param('ImageCacheName',ImageCacheName)

	def get_Image(self):
		return self.get_query_params().get('Image')

	def set_Image(self,Image):
		self.add_query_param('Image',Image)

	def get_Tags(self):
		return self.get_query_params().get('Tags')

	def set_Tags(self, Tags):
		for i in range(len(Tags)):
			if Tags[i].get('Key') is not None:
				self.add_query_param('Tag.' + str(i + 1) + '.Key', Tags[i].get('Key'))
			if Tags[i].get('Value') is not None:
				self.add_query_param('Tag.' + str(i + 1) + '.Value', Tags[i].get('Value'))

	def get_MatchImage(self):
		return self.get_query_params().get('MatchImage')

	def set_MatchImage(self, MatchImage):
		for i in range(len(MatchImage)):
			if MatchImage[i] is not None:
				self.add_query_param('MatchImage.' + str(i + 1), MatchImage[i])

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_Limit(self):
		return self.get_query_params().get('Limit')

	def set_Limit(self, Limit):
		self.add_query_param('Limit', Limit)

	def get_NextToken(self):
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):
		self.add_query_param('NextToken', NextToken)

	def get_ImageFullMatch(self):
		return self.get_query_params().get('ImageFullMatch')

	def set_ImageFullMatch(self, ImageFullMatch):
		self.add_query_param('ImageFullMatch', ImageFullMatch)

	def get_ImageMatchCountRequest(self):
		return self.get_query_params().get('ImageMatchCountRequest')

	def set_ImageMatchCountRequest(self, ImageMatchCountRequest):
		self.add_query_param('ImageMatchCountRequest', ImageMatchCountRequest)





