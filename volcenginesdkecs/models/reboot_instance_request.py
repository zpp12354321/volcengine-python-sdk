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


class RebootInstanceRequest(object):
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
        'force_stop': 'bool',
        'instance_id': 'str'
    }

    attribute_map = {
        'client_token': 'ClientToken',
        'force_stop': 'ForceStop',
        'instance_id': 'InstanceId'
    }

    def __init__(self, client_token=None, force_stop=None, instance_id=None, _configuration=None):  # noqa: E501
        """RebootInstanceRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_token = None
        self._force_stop = None
        self._instance_id = None
        self.discriminator = None

        if client_token is not None:
            self.client_token = client_token
        if force_stop is not None:
            self.force_stop = force_stop
        if instance_id is not None:
            self.instance_id = instance_id

    @property
    def client_token(self):
        """Gets the client_token of this RebootInstanceRequest.  # noqa: E501


        :return: The client_token of this RebootInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this RebootInstanceRequest.


        :param client_token: The client_token of this RebootInstanceRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def force_stop(self):
        """Gets the force_stop of this RebootInstanceRequest.  # noqa: E501


        :return: The force_stop of this RebootInstanceRequest.  # noqa: E501
        :rtype: bool
        """
        return self._force_stop

    @force_stop.setter
    def force_stop(self, force_stop):
        """Sets the force_stop of this RebootInstanceRequest.


        :param force_stop: The force_stop of this RebootInstanceRequest.  # noqa: E501
        :type: bool
        """

        self._force_stop = force_stop

    @property
    def instance_id(self):
        """Gets the instance_id of this RebootInstanceRequest.  # noqa: E501


        :return: The instance_id of this RebootInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this RebootInstanceRequest.


        :param instance_id: The instance_id of this RebootInstanceRequest.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

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
        if issubclass(RebootInstanceRequest, dict):
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
        if not isinstance(other, RebootInstanceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RebootInstanceRequest):
            return True

        return self.to_dict() != other.to_dict()
