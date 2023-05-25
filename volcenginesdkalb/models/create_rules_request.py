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


class CreateRulesRequest(object):
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
        'listener_id': 'str',
        'rules': 'list[RuleForCreateRulesInput]'
    }

    attribute_map = {
        'listener_id': 'ListenerId',
        'rules': 'Rules'
    }

    def __init__(self, listener_id=None, rules=None, _configuration=None):  # noqa: E501
        """CreateRulesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._listener_id = None
        self._rules = None
        self.discriminator = None

        self.listener_id = listener_id
        if rules is not None:
            self.rules = rules

    @property
    def listener_id(self):
        """Gets the listener_id of this CreateRulesRequest.  # noqa: E501


        :return: The listener_id of this CreateRulesRequest.  # noqa: E501
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """Sets the listener_id of this CreateRulesRequest.


        :param listener_id: The listener_id of this CreateRulesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and listener_id is None:
            raise ValueError("Invalid value for `listener_id`, must not be `None`")  # noqa: E501

        self._listener_id = listener_id

    @property
    def rules(self):
        """Gets the rules of this CreateRulesRequest.  # noqa: E501


        :return: The rules of this CreateRulesRequest.  # noqa: E501
        :rtype: list[RuleForCreateRulesInput]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this CreateRulesRequest.


        :param rules: The rules of this CreateRulesRequest.  # noqa: E501
        :type: list[RuleForCreateRulesInput]
        """

        self._rules = rules

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
        if issubclass(CreateRulesRequest, dict):
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
        if not isinstance(other, CreateRulesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateRulesRequest):
            return True

        return self.to_dict() != other.to_dict()