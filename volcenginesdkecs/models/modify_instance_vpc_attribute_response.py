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


class ModifyInstanceVpcAttributeResponse(object):
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
        'network_interface_id': 'str'
    }

    attribute_map = {
        'network_interface_id': 'NetworkInterfaceId'
    }

    def __init__(self, network_interface_id=None, _configuration=None):  # noqa: E501
        """ModifyInstanceVpcAttributeResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._network_interface_id = None
        self.discriminator = None

        if network_interface_id is not None:
            self.network_interface_id = network_interface_id

    @property
    def network_interface_id(self):
        """Gets the network_interface_id of this ModifyInstanceVpcAttributeResponse.  # noqa: E501


        :return: The network_interface_id of this ModifyInstanceVpcAttributeResponse.  # noqa: E501
        :rtype: str
        """
        return self._network_interface_id

    @network_interface_id.setter
    def network_interface_id(self, network_interface_id):
        """Sets the network_interface_id of this ModifyInstanceVpcAttributeResponse.


        :param network_interface_id: The network_interface_id of this ModifyInstanceVpcAttributeResponse.  # noqa: E501
        :type: str
        """

        self._network_interface_id = network_interface_id

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
        if issubclass(ModifyInstanceVpcAttributeResponse, dict):
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
        if not isinstance(other, ModifyInstanceVpcAttributeResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyInstanceVpcAttributeResponse):
            return True

        return self.to_dict() != other.to_dict()
