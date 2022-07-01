# coding: utf-8

"""
    auto_scaling

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeScalingGroupsRequest(object):
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
        'page_number': 'int',
        'page_size': 'int',
        'scaling_group_ids': 'list[str]',
        'scaling_group_names': 'list[str]'
    }

    attribute_map = {
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'scaling_group_ids': 'ScalingGroupIds',
        'scaling_group_names': 'ScalingGroupNames'
    }

    def __init__(self, page_number=None, page_size=None, scaling_group_ids=None, scaling_group_names=None, _configuration=None):  # noqa: E501
        """DescribeScalingGroupsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._page_number = None
        self._page_size = None
        self._scaling_group_ids = None
        self._scaling_group_names = None
        self.discriminator = None

        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if scaling_group_ids is not None:
            self.scaling_group_ids = scaling_group_ids
        if scaling_group_names is not None:
            self.scaling_group_names = scaling_group_names

    @property
    def page_number(self):
        """Gets the page_number of this DescribeScalingGroupsRequest.  # noqa: E501


        :return: The page_number of this DescribeScalingGroupsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeScalingGroupsRequest.


        :param page_number: The page_number of this DescribeScalingGroupsRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeScalingGroupsRequest.  # noqa: E501


        :return: The page_size of this DescribeScalingGroupsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeScalingGroupsRequest.


        :param page_size: The page_size of this DescribeScalingGroupsRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def scaling_group_ids(self):
        """Gets the scaling_group_ids of this DescribeScalingGroupsRequest.  # noqa: E501


        :return: The scaling_group_ids of this DescribeScalingGroupsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._scaling_group_ids

    @scaling_group_ids.setter
    def scaling_group_ids(self, scaling_group_ids):
        """Sets the scaling_group_ids of this DescribeScalingGroupsRequest.


        :param scaling_group_ids: The scaling_group_ids of this DescribeScalingGroupsRequest.  # noqa: E501
        :type: list[str]
        """

        self._scaling_group_ids = scaling_group_ids

    @property
    def scaling_group_names(self):
        """Gets the scaling_group_names of this DescribeScalingGroupsRequest.  # noqa: E501


        :return: The scaling_group_names of this DescribeScalingGroupsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._scaling_group_names

    @scaling_group_names.setter
    def scaling_group_names(self, scaling_group_names):
        """Sets the scaling_group_names of this DescribeScalingGroupsRequest.


        :param scaling_group_names: The scaling_group_names of this DescribeScalingGroupsRequest.  # noqa: E501
        :type: list[str]
        """

        self._scaling_group_names = scaling_group_names

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
        if issubclass(DescribeScalingGroupsRequest, dict):
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
        if not isinstance(other, DescribeScalingGroupsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeScalingGroupsRequest):
            return True

        return self.to_dict() != other.to_dict()
