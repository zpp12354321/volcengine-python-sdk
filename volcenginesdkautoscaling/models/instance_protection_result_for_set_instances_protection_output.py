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


class InstanceProtectionResultForSetInstancesProtectionOutput(object):
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
        'code': 'str',
        'instance_id': 'str',
        'message': 'str',
        'result': 'str'
    }

    attribute_map = {
        'code': 'Code',
        'instance_id': 'InstanceId',
        'message': 'Message',
        'result': 'Result'
    }

    def __init__(self, code=None, instance_id=None, message=None, result=None, _configuration=None):  # noqa: E501
        """InstanceProtectionResultForSetInstancesProtectionOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._code = None
        self._instance_id = None
        self._message = None
        self._result = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if instance_id is not None:
            self.instance_id = instance_id
        if message is not None:
            self.message = message
        if result is not None:
            self.result = result

    @property
    def code(self):
        """Gets the code of this InstanceProtectionResultForSetInstancesProtectionOutput.  # noqa: E501


        :return: The code of this InstanceProtectionResultForSetInstancesProtectionOutput.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this InstanceProtectionResultForSetInstancesProtectionOutput.


        :param code: The code of this InstanceProtectionResultForSetInstancesProtectionOutput.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def instance_id(self):
        """Gets the instance_id of this InstanceProtectionResultForSetInstancesProtectionOutput.  # noqa: E501


        :return: The instance_id of this InstanceProtectionResultForSetInstancesProtectionOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this InstanceProtectionResultForSetInstancesProtectionOutput.


        :param instance_id: The instance_id of this InstanceProtectionResultForSetInstancesProtectionOutput.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def message(self):
        """Gets the message of this InstanceProtectionResultForSetInstancesProtectionOutput.  # noqa: E501


        :return: The message of this InstanceProtectionResultForSetInstancesProtectionOutput.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this InstanceProtectionResultForSetInstancesProtectionOutput.


        :param message: The message of this InstanceProtectionResultForSetInstancesProtectionOutput.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def result(self):
        """Gets the result of this InstanceProtectionResultForSetInstancesProtectionOutput.  # noqa: E501


        :return: The result of this InstanceProtectionResultForSetInstancesProtectionOutput.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this InstanceProtectionResultForSetInstancesProtectionOutput.


        :param result: The result of this InstanceProtectionResultForSetInstancesProtectionOutput.  # noqa: E501
        :type: str
        """

        self._result = result

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
        if issubclass(InstanceProtectionResultForSetInstancesProtectionOutput, dict):
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
        if not isinstance(other, InstanceProtectionResultForSetInstancesProtectionOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstanceProtectionResultForSetInstancesProtectionOutput):
            return True

        return self.to_dict() != other.to_dict()
