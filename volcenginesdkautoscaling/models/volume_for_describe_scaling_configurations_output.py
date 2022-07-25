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


class VolumeForDescribeScalingConfigurationsOutput(object):
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
        'delete_with_instance': 'bool',
        'size': 'int',
        'volume_type': 'str'
    }

    attribute_map = {
        'delete_with_instance': 'DeleteWithInstance',
        'size': 'Size',
        'volume_type': 'VolumeType'
    }

    def __init__(self, delete_with_instance=None, size=None, volume_type=None, _configuration=None):  # noqa: E501
        """VolumeForDescribeScalingConfigurationsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._delete_with_instance = None
        self._size = None
        self._volume_type = None
        self.discriminator = None

        if delete_with_instance is not None:
            self.delete_with_instance = delete_with_instance
        if size is not None:
            self.size = size
        if volume_type is not None:
            self.volume_type = volume_type

    @property
    def delete_with_instance(self):
        """Gets the delete_with_instance of this VolumeForDescribeScalingConfigurationsOutput.  # noqa: E501


        :return: The delete_with_instance of this VolumeForDescribeScalingConfigurationsOutput.  # noqa: E501
        :rtype: bool
        """
        return self._delete_with_instance

    @delete_with_instance.setter
    def delete_with_instance(self, delete_with_instance):
        """Sets the delete_with_instance of this VolumeForDescribeScalingConfigurationsOutput.


        :param delete_with_instance: The delete_with_instance of this VolumeForDescribeScalingConfigurationsOutput.  # noqa: E501
        :type: bool
        """

        self._delete_with_instance = delete_with_instance

    @property
    def size(self):
        """Gets the size of this VolumeForDescribeScalingConfigurationsOutput.  # noqa: E501


        :return: The size of this VolumeForDescribeScalingConfigurationsOutput.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this VolumeForDescribeScalingConfigurationsOutput.


        :param size: The size of this VolumeForDescribeScalingConfigurationsOutput.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def volume_type(self):
        """Gets the volume_type of this VolumeForDescribeScalingConfigurationsOutput.  # noqa: E501


        :return: The volume_type of this VolumeForDescribeScalingConfigurationsOutput.  # noqa: E501
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this VolumeForDescribeScalingConfigurationsOutput.


        :param volume_type: The volume_type of this VolumeForDescribeScalingConfigurationsOutput.  # noqa: E501
        :type: str
        """

        self._volume_type = volume_type

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
        if issubclass(VolumeForDescribeScalingConfigurationsOutput, dict):
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
        if not isinstance(other, VolumeForDescribeScalingConfigurationsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VolumeForDescribeScalingConfigurationsOutput):
            return True

        return self.to_dict() != other.to_dict()