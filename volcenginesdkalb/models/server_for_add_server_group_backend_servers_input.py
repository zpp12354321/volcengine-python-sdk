# coding: utf-8

"""
    alb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ServerForAddServerGroupBackendServersInput(object):
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
        'instance_id': 'str',
        'ip': 'str',
        'port': 'int',
        'remote_enabled': 'str',
        'type': 'str',
        'weight': 'int'
    }

    attribute_map = {
        'description': 'Description',
        'instance_id': 'InstanceId',
        'ip': 'Ip',
        'port': 'Port',
        'remote_enabled': 'RemoteEnabled',
        'type': 'Type',
        'weight': 'Weight'
    }

    def __init__(self, description=None, instance_id=None, ip=None, port=None, remote_enabled=None, type=None, weight=None, _configuration=None):  # noqa: E501
        """ServerForAddServerGroupBackendServersInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._instance_id = None
        self._ip = None
        self._port = None
        self._remote_enabled = None
        self._type = None
        self._weight = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.instance_id = instance_id
        self.ip = ip
        self.port = port
        if remote_enabled is not None:
            self.remote_enabled = remote_enabled
        self.type = type
        if weight is not None:
            self.weight = weight

    @property
    def description(self):
        """Gets the description of this ServerForAddServerGroupBackendServersInput.  # noqa: E501


        :return: The description of this ServerForAddServerGroupBackendServersInput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ServerForAddServerGroupBackendServersInput.


        :param description: The description of this ServerForAddServerGroupBackendServersInput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def instance_id(self):
        """Gets the instance_id of this ServerForAddServerGroupBackendServersInput.  # noqa: E501


        :return: The instance_id of this ServerForAddServerGroupBackendServersInput.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ServerForAddServerGroupBackendServersInput.


        :param instance_id: The instance_id of this ServerForAddServerGroupBackendServersInput.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_id is None:
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def ip(self):
        """Gets the ip of this ServerForAddServerGroupBackendServersInput.  # noqa: E501


        :return: The ip of this ServerForAddServerGroupBackendServersInput.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this ServerForAddServerGroupBackendServersInput.


        :param ip: The ip of this ServerForAddServerGroupBackendServersInput.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and ip is None:
            raise ValueError("Invalid value for `ip`, must not be `None`")  # noqa: E501

        self._ip = ip

    @property
    def port(self):
        """Gets the port of this ServerForAddServerGroupBackendServersInput.  # noqa: E501


        :return: The port of this ServerForAddServerGroupBackendServersInput.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ServerForAddServerGroupBackendServersInput.


        :param port: The port of this ServerForAddServerGroupBackendServersInput.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def remote_enabled(self):
        """Gets the remote_enabled of this ServerForAddServerGroupBackendServersInput.  # noqa: E501


        :return: The remote_enabled of this ServerForAddServerGroupBackendServersInput.  # noqa: E501
        :rtype: str
        """
        return self._remote_enabled

    @remote_enabled.setter
    def remote_enabled(self, remote_enabled):
        """Sets the remote_enabled of this ServerForAddServerGroupBackendServersInput.


        :param remote_enabled: The remote_enabled of this ServerForAddServerGroupBackendServersInput.  # noqa: E501
        :type: str
        """

        self._remote_enabled = remote_enabled

    @property
    def type(self):
        """Gets the type of this ServerForAddServerGroupBackendServersInput.  # noqa: E501


        :return: The type of this ServerForAddServerGroupBackendServersInput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ServerForAddServerGroupBackendServersInput.


        :param type: The type of this ServerForAddServerGroupBackendServersInput.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def weight(self):
        """Gets the weight of this ServerForAddServerGroupBackendServersInput.  # noqa: E501


        :return: The weight of this ServerForAddServerGroupBackendServersInput.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this ServerForAddServerGroupBackendServersInput.


        :param weight: The weight of this ServerForAddServerGroupBackendServersInput.  # noqa: E501
        :type: int
        """

        self._weight = weight

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
        if issubclass(ServerForAddServerGroupBackendServersInput, dict):
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
        if not isinstance(other, ServerForAddServerGroupBackendServersInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ServerForAddServerGroupBackendServersInput):
            return True

        return self.to_dict() != other.to_dict()