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


class CreateDirectConnectGatewayRouteRequest(object):
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
        'destination_cidr_block': 'str',
        'direct_connect_gateway_id': 'str',
        'next_hop_id': 'str'
    }

    attribute_map = {
        'destination_cidr_block': 'DestinationCidrBlock',
        'direct_connect_gateway_id': 'DirectConnectGatewayId',
        'next_hop_id': 'NextHopId'
    }

    def __init__(self, destination_cidr_block=None, direct_connect_gateway_id=None, next_hop_id=None, _configuration=None):  # noqa: E501
        """CreateDirectConnectGatewayRouteRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._destination_cidr_block = None
        self._direct_connect_gateway_id = None
        self._next_hop_id = None
        self.discriminator = None

        self.destination_cidr_block = destination_cidr_block
        self.direct_connect_gateway_id = direct_connect_gateway_id
        self.next_hop_id = next_hop_id

    @property
    def destination_cidr_block(self):
        """Gets the destination_cidr_block of this CreateDirectConnectGatewayRouteRequest.  # noqa: E501


        :return: The destination_cidr_block of this CreateDirectConnectGatewayRouteRequest.  # noqa: E501
        :rtype: str
        """
        return self._destination_cidr_block

    @destination_cidr_block.setter
    def destination_cidr_block(self, destination_cidr_block):
        """Sets the destination_cidr_block of this CreateDirectConnectGatewayRouteRequest.


        :param destination_cidr_block: The destination_cidr_block of this CreateDirectConnectGatewayRouteRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and destination_cidr_block is None:
            raise ValueError("Invalid value for `destination_cidr_block`, must not be `None`")  # noqa: E501

        self._destination_cidr_block = destination_cidr_block

    @property
    def direct_connect_gateway_id(self):
        """Gets the direct_connect_gateway_id of this CreateDirectConnectGatewayRouteRequest.  # noqa: E501


        :return: The direct_connect_gateway_id of this CreateDirectConnectGatewayRouteRequest.  # noqa: E501
        :rtype: str
        """
        return self._direct_connect_gateway_id

    @direct_connect_gateway_id.setter
    def direct_connect_gateway_id(self, direct_connect_gateway_id):
        """Sets the direct_connect_gateway_id of this CreateDirectConnectGatewayRouteRequest.


        :param direct_connect_gateway_id: The direct_connect_gateway_id of this CreateDirectConnectGatewayRouteRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and direct_connect_gateway_id is None:
            raise ValueError("Invalid value for `direct_connect_gateway_id`, must not be `None`")  # noqa: E501

        self._direct_connect_gateway_id = direct_connect_gateway_id

    @property
    def next_hop_id(self):
        """Gets the next_hop_id of this CreateDirectConnectGatewayRouteRequest.  # noqa: E501


        :return: The next_hop_id of this CreateDirectConnectGatewayRouteRequest.  # noqa: E501
        :rtype: str
        """
        return self._next_hop_id

    @next_hop_id.setter
    def next_hop_id(self, next_hop_id):
        """Sets the next_hop_id of this CreateDirectConnectGatewayRouteRequest.


        :param next_hop_id: The next_hop_id of this CreateDirectConnectGatewayRouteRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and next_hop_id is None:
            raise ValueError("Invalid value for `next_hop_id`, must not be `None`")  # noqa: E501

        self._next_hop_id = next_hop_id

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
        if issubclass(CreateDirectConnectGatewayRouteRequest, dict):
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
        if not isinstance(other, CreateDirectConnectGatewayRouteRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateDirectConnectGatewayRouteRequest):
            return True

        return self.to_dict() != other.to_dict()
