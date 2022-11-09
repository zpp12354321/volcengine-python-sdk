# coding: utf-8

"""
    vpn

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeVpnGatewayAttributesRequest(object):
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
        'vpn_gateway_id': 'str'
    }

    attribute_map = {
        'vpn_gateway_id': 'VpnGatewayId'
    }

    def __init__(self, vpn_gateway_id=None, _configuration=None):  # noqa: E501
        """DescribeVpnGatewayAttributesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._vpn_gateway_id = None
        self.discriminator = None

        self.vpn_gateway_id = vpn_gateway_id

    @property
    def vpn_gateway_id(self):
        """Gets the vpn_gateway_id of this DescribeVpnGatewayAttributesRequest.  # noqa: E501


        :return: The vpn_gateway_id of this DescribeVpnGatewayAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpn_gateway_id

    @vpn_gateway_id.setter
    def vpn_gateway_id(self, vpn_gateway_id):
        """Sets the vpn_gateway_id of this DescribeVpnGatewayAttributesRequest.


        :param vpn_gateway_id: The vpn_gateway_id of this DescribeVpnGatewayAttributesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and vpn_gateway_id is None:
            raise ValueError("Invalid value for `vpn_gateway_id`, must not be `None`")  # noqa: E501

        self._vpn_gateway_id = vpn_gateway_id

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
        if issubclass(DescribeVpnGatewayAttributesRequest, dict):
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
        if not isinstance(other, DescribeVpnGatewayAttributesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeVpnGatewayAttributesRequest):
            return True

        return self.to_dict() != other.to_dict()
