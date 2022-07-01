# coding: utf-8

"""
    directconnect

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CreateDirectConnectGatewayRequest(object):
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
        'description': 'str',
        'direct_connect_gateway_name': 'str'
    }

    attribute_map = {
        'description': 'Description',
        'direct_connect_gateway_name': 'DirectConnectGatewayName'
    }

    def __init__(self, description=None, direct_connect_gateway_name=None, _configuration=None):  # noqa: E501
        """CreateDirectConnectGatewayRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._direct_connect_gateway_name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.direct_connect_gateway_name = direct_connect_gateway_name

    @property
    def description(self):
        """Gets the description of this CreateDirectConnectGatewayRequest.  # noqa: E501


        :return: The description of this CreateDirectConnectGatewayRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateDirectConnectGatewayRequest.


        :param description: The description of this CreateDirectConnectGatewayRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def direct_connect_gateway_name(self):
        """Gets the direct_connect_gateway_name of this CreateDirectConnectGatewayRequest.  # noqa: E501


        :return: The direct_connect_gateway_name of this CreateDirectConnectGatewayRequest.  # noqa: E501
        :rtype: str
        """
        return self._direct_connect_gateway_name

    @direct_connect_gateway_name.setter
    def direct_connect_gateway_name(self, direct_connect_gateway_name):
        """Sets the direct_connect_gateway_name of this CreateDirectConnectGatewayRequest.


        :param direct_connect_gateway_name: The direct_connect_gateway_name of this CreateDirectConnectGatewayRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and direct_connect_gateway_name is None:
            raise ValueError("Invalid value for `direct_connect_gateway_name`, must not be `None`")  # noqa: E501

        self._direct_connect_gateway_name = direct_connect_gateway_name

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
        if issubclass(CreateDirectConnectGatewayRequest, dict):
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
        if not isinstance(other, CreateDirectConnectGatewayRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateDirectConnectGatewayRequest):
            return True

        return self.to_dict() != other.to_dict()
