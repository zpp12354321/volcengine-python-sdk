# coding: utf-8

"""
    kafka

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class AccessPolicyForDescribeTopicAccessPoliciesOutput(object):
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
        'access_policy': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'access_policy': 'AccessPolicy',
        'user_name': 'UserName'
    }

    def __init__(self, access_policy=None, user_name=None, _configuration=None):  # noqa: E501
        """AccessPolicyForDescribeTopicAccessPoliciesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access_policy = None
        self._user_name = None
        self.discriminator = None

        if access_policy is not None:
            self.access_policy = access_policy
        if user_name is not None:
            self.user_name = user_name

    @property
    def access_policy(self):
        """Gets the access_policy of this AccessPolicyForDescribeTopicAccessPoliciesOutput.  # noqa: E501


        :return: The access_policy of this AccessPolicyForDescribeTopicAccessPoliciesOutput.  # noqa: E501
        :rtype: str
        """
        return self._access_policy

    @access_policy.setter
    def access_policy(self, access_policy):
        """Sets the access_policy of this AccessPolicyForDescribeTopicAccessPoliciesOutput.


        :param access_policy: The access_policy of this AccessPolicyForDescribeTopicAccessPoliciesOutput.  # noqa: E501
        :type: str
        """

        self._access_policy = access_policy

    @property
    def user_name(self):
        """Gets the user_name of this AccessPolicyForDescribeTopicAccessPoliciesOutput.  # noqa: E501


        :return: The user_name of this AccessPolicyForDescribeTopicAccessPoliciesOutput.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this AccessPolicyForDescribeTopicAccessPoliciesOutput.


        :param user_name: The user_name of this AccessPolicyForDescribeTopicAccessPoliciesOutput.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

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
        if issubclass(AccessPolicyForDescribeTopicAccessPoliciesOutput, dict):
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
        if not isinstance(other, AccessPolicyForDescribeTopicAccessPoliciesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccessPolicyForDescribeTopicAccessPoliciesOutput):
            return True

        return self.to_dict() != other.to_dict()
