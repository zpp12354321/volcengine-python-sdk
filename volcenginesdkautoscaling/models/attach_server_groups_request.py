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


class AttachServerGroupsRequest(object):
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
        'client_token': 'str',
        'scaling_group_id': 'str',
        'server_group_attributes': 'list[ServerGroupAttributeForAttachServerGroupsInput]'
    }

    attribute_map = {
        'client_token': 'ClientToken',
        'scaling_group_id': 'ScalingGroupId',
        'server_group_attributes': 'ServerGroupAttributes'
    }

    def __init__(self, client_token=None, scaling_group_id=None, server_group_attributes=None, _configuration=None):  # noqa: E501
        """AttachServerGroupsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_token = None
        self._scaling_group_id = None
        self._server_group_attributes = None
        self.discriminator = None

        if client_token is not None:
            self.client_token = client_token
        if scaling_group_id is not None:
            self.scaling_group_id = scaling_group_id
        if server_group_attributes is not None:
            self.server_group_attributes = server_group_attributes

    @property
    def client_token(self):
        """Gets the client_token of this AttachServerGroupsRequest.  # noqa: E501


        :return: The client_token of this AttachServerGroupsRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this AttachServerGroupsRequest.


        :param client_token: The client_token of this AttachServerGroupsRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def scaling_group_id(self):
        """Gets the scaling_group_id of this AttachServerGroupsRequest.  # noqa: E501


        :return: The scaling_group_id of this AttachServerGroupsRequest.  # noqa: E501
        :rtype: str
        """
        return self._scaling_group_id

    @scaling_group_id.setter
    def scaling_group_id(self, scaling_group_id):
        """Sets the scaling_group_id of this AttachServerGroupsRequest.


        :param scaling_group_id: The scaling_group_id of this AttachServerGroupsRequest.  # noqa: E501
        :type: str
        """

        self._scaling_group_id = scaling_group_id

    @property
    def server_group_attributes(self):
        """Gets the server_group_attributes of this AttachServerGroupsRequest.  # noqa: E501


        :return: The server_group_attributes of this AttachServerGroupsRequest.  # noqa: E501
        :rtype: list[ServerGroupAttributeForAttachServerGroupsInput]
        """
        return self._server_group_attributes

    @server_group_attributes.setter
    def server_group_attributes(self, server_group_attributes):
        """Sets the server_group_attributes of this AttachServerGroupsRequest.


        :param server_group_attributes: The server_group_attributes of this AttachServerGroupsRequest.  # noqa: E501
        :type: list[ServerGroupAttributeForAttachServerGroupsInput]
        """

        self._server_group_attributes = server_group_attributes

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
        if issubclass(AttachServerGroupsRequest, dict):
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
        if not isinstance(other, AttachServerGroupsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AttachServerGroupsRequest):
            return True

        return self.to_dict() != other.to_dict()
