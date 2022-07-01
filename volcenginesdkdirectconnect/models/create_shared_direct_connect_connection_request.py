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


class CreateSharedDirectConnectConnectionRequest(object):
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
        'bandwidth': 'int',
        'description': 'str',
        'direct_connect_connection_id': 'str',
        'shared_direct_connect_connection_name': 'str',
        'user_account_id': 'str',
        'vlan_id': 'int'
    }

    attribute_map = {
        'bandwidth': 'Bandwidth',
        'description': 'Description',
        'direct_connect_connection_id': 'DirectConnectConnectionId',
        'shared_direct_connect_connection_name': 'SharedDirectConnectConnectionName',
        'user_account_id': 'UserAccountId',
        'vlan_id': 'VlanId'
    }

    def __init__(self, bandwidth=None, description=None, direct_connect_connection_id=None, shared_direct_connect_connection_name=None, user_account_id=None, vlan_id=None, _configuration=None):  # noqa: E501
        """CreateSharedDirectConnectConnectionRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bandwidth = None
        self._description = None
        self._direct_connect_connection_id = None
        self._shared_direct_connect_connection_name = None
        self._user_account_id = None
        self._vlan_id = None
        self.discriminator = None

        self.bandwidth = bandwidth
        if description is not None:
            self.description = description
        self.direct_connect_connection_id = direct_connect_connection_id
        if shared_direct_connect_connection_name is not None:
            self.shared_direct_connect_connection_name = shared_direct_connect_connection_name
        self.user_account_id = user_account_id
        self.vlan_id = vlan_id

    @property
    def bandwidth(self):
        """Gets the bandwidth of this CreateSharedDirectConnectConnectionRequest.  # noqa: E501


        :return: The bandwidth of this CreateSharedDirectConnectConnectionRequest.  # noqa: E501
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this CreateSharedDirectConnectConnectionRequest.


        :param bandwidth: The bandwidth of this CreateSharedDirectConnectConnectionRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and bandwidth is None:
            raise ValueError("Invalid value for `bandwidth`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                bandwidth is not None and bandwidth > 1000):  # noqa: E501
            raise ValueError("Invalid value for `bandwidth`, must be a value less than or equal to `1000`")  # noqa: E501
        if (self._configuration.client_side_validation and
                bandwidth is not None and bandwidth < 50):  # noqa: E501
            raise ValueError("Invalid value for `bandwidth`, must be a value greater than or equal to `50`")  # noqa: E501

        self._bandwidth = bandwidth

    @property
    def description(self):
        """Gets the description of this CreateSharedDirectConnectConnectionRequest.  # noqa: E501


        :return: The description of this CreateSharedDirectConnectConnectionRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateSharedDirectConnectConnectionRequest.


        :param description: The description of this CreateSharedDirectConnectConnectionRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def direct_connect_connection_id(self):
        """Gets the direct_connect_connection_id of this CreateSharedDirectConnectConnectionRequest.  # noqa: E501


        :return: The direct_connect_connection_id of this CreateSharedDirectConnectConnectionRequest.  # noqa: E501
        :rtype: str
        """
        return self._direct_connect_connection_id

    @direct_connect_connection_id.setter
    def direct_connect_connection_id(self, direct_connect_connection_id):
        """Sets the direct_connect_connection_id of this CreateSharedDirectConnectConnectionRequest.


        :param direct_connect_connection_id: The direct_connect_connection_id of this CreateSharedDirectConnectConnectionRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and direct_connect_connection_id is None:
            raise ValueError("Invalid value for `direct_connect_connection_id`, must not be `None`")  # noqa: E501

        self._direct_connect_connection_id = direct_connect_connection_id

    @property
    def shared_direct_connect_connection_name(self):
        """Gets the shared_direct_connect_connection_name of this CreateSharedDirectConnectConnectionRequest.  # noqa: E501


        :return: The shared_direct_connect_connection_name of this CreateSharedDirectConnectConnectionRequest.  # noqa: E501
        :rtype: str
        """
        return self._shared_direct_connect_connection_name

    @shared_direct_connect_connection_name.setter
    def shared_direct_connect_connection_name(self, shared_direct_connect_connection_name):
        """Sets the shared_direct_connect_connection_name of this CreateSharedDirectConnectConnectionRequest.


        :param shared_direct_connect_connection_name: The shared_direct_connect_connection_name of this CreateSharedDirectConnectConnectionRequest.  # noqa: E501
        :type: str
        """

        self._shared_direct_connect_connection_name = shared_direct_connect_connection_name

    @property
    def user_account_id(self):
        """Gets the user_account_id of this CreateSharedDirectConnectConnectionRequest.  # noqa: E501


        :return: The user_account_id of this CreateSharedDirectConnectConnectionRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_account_id

    @user_account_id.setter
    def user_account_id(self, user_account_id):
        """Sets the user_account_id of this CreateSharedDirectConnectConnectionRequest.


        :param user_account_id: The user_account_id of this CreateSharedDirectConnectConnectionRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and user_account_id is None:
            raise ValueError("Invalid value for `user_account_id`, must not be `None`")  # noqa: E501

        self._user_account_id = user_account_id

    @property
    def vlan_id(self):
        """Gets the vlan_id of this CreateSharedDirectConnectConnectionRequest.  # noqa: E501


        :return: The vlan_id of this CreateSharedDirectConnectConnectionRequest.  # noqa: E501
        :rtype: int
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """Sets the vlan_id of this CreateSharedDirectConnectConnectionRequest.


        :param vlan_id: The vlan_id of this CreateSharedDirectConnectConnectionRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and vlan_id is None:
            raise ValueError("Invalid value for `vlan_id`, must not be `None`")  # noqa: E501

        self._vlan_id = vlan_id

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
        if issubclass(CreateSharedDirectConnectConnectionRequest, dict):
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
        if not isinstance(other, CreateSharedDirectConnectConnectionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateSharedDirectConnectConnectionRequest):
            return True

        return self.to_dict() != other.to_dict()
