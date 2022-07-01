# coding: utf-8

"""
    vpc

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CreateVpcRequest(object):
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
        'cidr_block': 'str',
        'description': 'str',
        'dns_servers': 'list[str]',
        'vpc_name': 'str'
    }

    attribute_map = {
        'cidr_block': 'CidrBlock',
        'description': 'Description',
        'dns_servers': 'DnsServers',
        'vpc_name': 'VpcName'
    }

    def __init__(self, cidr_block=None, description=None, dns_servers=None, vpc_name=None, _configuration=None):  # noqa: E501
        """CreateVpcRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cidr_block = None
        self._description = None
        self._dns_servers = None
        self._vpc_name = None
        self.discriminator = None

        self.cidr_block = cidr_block
        if description is not None:
            self.description = description
        if dns_servers is not None:
            self.dns_servers = dns_servers
        if vpc_name is not None:
            self.vpc_name = vpc_name

    @property
    def cidr_block(self):
        """Gets the cidr_block of this CreateVpcRequest.  # noqa: E501


        :return: The cidr_block of this CreateVpcRequest.  # noqa: E501
        :rtype: str
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """Sets the cidr_block of this CreateVpcRequest.


        :param cidr_block: The cidr_block of this CreateVpcRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and cidr_block is None:
            raise ValueError("Invalid value for `cidr_block`, must not be `None`")  # noqa: E501

        self._cidr_block = cidr_block

    @property
    def description(self):
        """Gets the description of this CreateVpcRequest.  # noqa: E501


        :return: The description of this CreateVpcRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateVpcRequest.


        :param description: The description of this CreateVpcRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                description is not None and len(description) > 255):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def dns_servers(self):
        """Gets the dns_servers of this CreateVpcRequest.  # noqa: E501


        :return: The dns_servers of this CreateVpcRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._dns_servers

    @dns_servers.setter
    def dns_servers(self, dns_servers):
        """Sets the dns_servers of this CreateVpcRequest.


        :param dns_servers: The dns_servers of this CreateVpcRequest.  # noqa: E501
        :type: list[str]
        """

        self._dns_servers = dns_servers

    @property
    def vpc_name(self):
        """Gets the vpc_name of this CreateVpcRequest.  # noqa: E501


        :return: The vpc_name of this CreateVpcRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        """Sets the vpc_name of this CreateVpcRequest.


        :param vpc_name: The vpc_name of this CreateVpcRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                vpc_name is not None and len(vpc_name) > 128):
            raise ValueError("Invalid value for `vpc_name`, length must be less than or equal to `128`")  # noqa: E501
        if (self._configuration.client_side_validation and
                vpc_name is not None and len(vpc_name) < 1):
            raise ValueError("Invalid value for `vpc_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._vpc_name = vpc_name

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
        if issubclass(CreateVpcRequest, dict):
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
        if not isinstance(other, CreateVpcRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateVpcRequest):
            return True

        return self.to_dict() != other.to_dict()
