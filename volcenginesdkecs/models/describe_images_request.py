# coding: utf-8

"""
    ecs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeImagesRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'image_ids': 'list[str]',
        'image_status': 'str',
        'instance_type_id': 'str',
        'is_support_cloud_init': 'bool',
        'max_results': 'int',
        'next_token': 'str',
        'os_type': 'str',
        'status': 'list[str]',
        'visibility': 'str'
    }

    attribute_map = {
        'image_ids': 'ImageIds',
        'image_status': 'ImageStatus',
        'instance_type_id': 'InstanceTypeId',
        'is_support_cloud_init': 'IsSupportCloudInit',
        'max_results': 'MaxResults',
        'next_token': 'NextToken',
        'os_type': 'OsType',
        'status': 'Status',
        'visibility': 'Visibility'
    }

    def __init__(self, image_ids=None, image_status=None, instance_type_id=None, is_support_cloud_init=None, max_results=None, next_token=None, os_type=None, status=None, visibility=None, _configuration=None):  # noqa: E501
        """DescribeImagesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._image_ids = None
        self._image_status = None
        self._instance_type_id = None
        self._is_support_cloud_init = None
        self._max_results = None
        self._next_token = None
        self._os_type = None
        self._status = None
        self._visibility = None
        self.discriminator = None

        if image_ids is not None:
            self.image_ids = image_ids
        if image_status is not None:
            self.image_status = image_status
        if instance_type_id is not None:
            self.instance_type_id = instance_type_id
        if is_support_cloud_init is not None:
            self.is_support_cloud_init = is_support_cloud_init
        if max_results is not None:
            self.max_results = max_results
        if next_token is not None:
            self.next_token = next_token
        if os_type is not None:
            self.os_type = os_type
        if status is not None:
            self.status = status
        if visibility is not None:
            self.visibility = visibility

    @property
    def image_ids(self):
        """Gets the image_ids of this DescribeImagesRequest.  # noqa: E501


        :return: The image_ids of this DescribeImagesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._image_ids

    @image_ids.setter
    def image_ids(self, image_ids):
        """Sets the image_ids of this DescribeImagesRequest.


        :param image_ids: The image_ids of this DescribeImagesRequest.  # noqa: E501
        :type: list[str]
        """

        self._image_ids = image_ids

    @property
    def image_status(self):
        """Gets the image_status of this DescribeImagesRequest.  # noqa: E501


        :return: The image_status of this DescribeImagesRequest.  # noqa: E501
        :rtype: str
        """
        return self._image_status

    @image_status.setter
    def image_status(self, image_status):
        """Sets the image_status of this DescribeImagesRequest.


        :param image_status: The image_status of this DescribeImagesRequest.  # noqa: E501
        :type: str
        """

        self._image_status = image_status

    @property
    def instance_type_id(self):
        """Gets the instance_type_id of this DescribeImagesRequest.  # noqa: E501


        :return: The instance_type_id of this DescribeImagesRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_type_id

    @instance_type_id.setter
    def instance_type_id(self, instance_type_id):
        """Sets the instance_type_id of this DescribeImagesRequest.


        :param instance_type_id: The instance_type_id of this DescribeImagesRequest.  # noqa: E501
        :type: str
        """

        self._instance_type_id = instance_type_id

    @property
    def is_support_cloud_init(self):
        """Gets the is_support_cloud_init of this DescribeImagesRequest.  # noqa: E501


        :return: The is_support_cloud_init of this DescribeImagesRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_support_cloud_init

    @is_support_cloud_init.setter
    def is_support_cloud_init(self, is_support_cloud_init):
        """Sets the is_support_cloud_init of this DescribeImagesRequest.


        :param is_support_cloud_init: The is_support_cloud_init of this DescribeImagesRequest.  # noqa: E501
        :type: bool
        """

        self._is_support_cloud_init = is_support_cloud_init

    @property
    def max_results(self):
        """Gets the max_results of this DescribeImagesRequest.  # noqa: E501


        :return: The max_results of this DescribeImagesRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_results

    @max_results.setter
    def max_results(self, max_results):
        """Sets the max_results of this DescribeImagesRequest.


        :param max_results: The max_results of this DescribeImagesRequest.  # noqa: E501
        :type: int
        """

        self._max_results = max_results

    @property
    def next_token(self):
        """Gets the next_token of this DescribeImagesRequest.  # noqa: E501


        :return: The next_token of this DescribeImagesRequest.  # noqa: E501
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this DescribeImagesRequest.


        :param next_token: The next_token of this DescribeImagesRequest.  # noqa: E501
        :type: str
        """

        self._next_token = next_token

    @property
    def os_type(self):
        """Gets the os_type of this DescribeImagesRequest.  # noqa: E501


        :return: The os_type of this DescribeImagesRequest.  # noqa: E501
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this DescribeImagesRequest.


        :param os_type: The os_type of this DescribeImagesRequest.  # noqa: E501
        :type: str
        """

        self._os_type = os_type

    @property
    def status(self):
        """Gets the status of this DescribeImagesRequest.  # noqa: E501


        :return: The status of this DescribeImagesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DescribeImagesRequest.


        :param status: The status of this DescribeImagesRequest.  # noqa: E501
        :type: list[str]
        """

        self._status = status

    @property
    def visibility(self):
        """Gets the visibility of this DescribeImagesRequest.  # noqa: E501


        :return: The visibility of this DescribeImagesRequest.  # noqa: E501
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this DescribeImagesRequest.


        :param visibility: The visibility of this DescribeImagesRequest.  # noqa: E501
        :type: str
        """

        self._visibility = visibility

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DescribeImagesRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DescribeImagesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeImagesRequest):
            return True

        return self.to_dict() != other.to_dict()