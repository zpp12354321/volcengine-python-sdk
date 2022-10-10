# coding: utf-8

"""
    vke

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class NodeConfigForCreateDefaultNodePoolInput(object):
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
        'initialize_script': 'str',
        'security': 'SecurityForCreateDefaultNodePoolInput'
    }

    attribute_map = {
        'initialize_script': 'InitializeScript',
        'security': 'Security'
    }

    def __init__(self, initialize_script=None, security=None, _configuration=None):  # noqa: E501
        """NodeConfigForCreateDefaultNodePoolInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._initialize_script = None
        self._security = None
        self.discriminator = None

        if initialize_script is not None:
            self.initialize_script = initialize_script
        if security is not None:
            self.security = security

    @property
    def initialize_script(self):
        """Gets the initialize_script of this NodeConfigForCreateDefaultNodePoolInput.  # noqa: E501


        :return: The initialize_script of this NodeConfigForCreateDefaultNodePoolInput.  # noqa: E501
        :rtype: str
        """
        return self._initialize_script

    @initialize_script.setter
    def initialize_script(self, initialize_script):
        """Sets the initialize_script of this NodeConfigForCreateDefaultNodePoolInput.


        :param initialize_script: The initialize_script of this NodeConfigForCreateDefaultNodePoolInput.  # noqa: E501
        :type: str
        """

        self._initialize_script = initialize_script

    @property
    def security(self):
        """Gets the security of this NodeConfigForCreateDefaultNodePoolInput.  # noqa: E501


        :return: The security of this NodeConfigForCreateDefaultNodePoolInput.  # noqa: E501
        :rtype: SecurityForCreateDefaultNodePoolInput
        """
        return self._security

    @security.setter
    def security(self, security):
        """Sets the security of this NodeConfigForCreateDefaultNodePoolInput.


        :param security: The security of this NodeConfigForCreateDefaultNodePoolInput.  # noqa: E501
        :type: SecurityForCreateDefaultNodePoolInput
        """

        self._security = security

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
        if issubclass(NodeConfigForCreateDefaultNodePoolInput, dict):
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
        if not isinstance(other, NodeConfigForCreateDefaultNodePoolInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NodeConfigForCreateDefaultNodePoolInput):
            return True

        return self.to_dict() != other.to_dict()