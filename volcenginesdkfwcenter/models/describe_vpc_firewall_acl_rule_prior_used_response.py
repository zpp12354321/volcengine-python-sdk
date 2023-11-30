# coding: utf-8

"""
    fwcenter

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeVpcFirewallAclRulePriorUsedResponse(object):
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
        'account_id': 'str',
        'end': 'int',
        'start': 'int',
        'vpc_firewall_id': 'str'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'end': 'End',
        'start': 'Start',
        'vpc_firewall_id': 'VpcFirewallId'
    }

    def __init__(self, account_id=None, end=None, start=None, vpc_firewall_id=None, _configuration=None):  # noqa: E501
        """DescribeVpcFirewallAclRulePriorUsedResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_id = None
        self._end = None
        self._start = None
        self._vpc_firewall_id = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if end is not None:
            self.end = end
        if start is not None:
            self.start = start
        if vpc_firewall_id is not None:
            self.vpc_firewall_id = vpc_firewall_id

    @property
    def account_id(self):
        """Gets the account_id of this DescribeVpcFirewallAclRulePriorUsedResponse.  # noqa: E501


        :return: The account_id of this DescribeVpcFirewallAclRulePriorUsedResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this DescribeVpcFirewallAclRulePriorUsedResponse.


        :param account_id: The account_id of this DescribeVpcFirewallAclRulePriorUsedResponse.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def end(self):
        """Gets the end of this DescribeVpcFirewallAclRulePriorUsedResponse.  # noqa: E501


        :return: The end of this DescribeVpcFirewallAclRulePriorUsedResponse.  # noqa: E501
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this DescribeVpcFirewallAclRulePriorUsedResponse.


        :param end: The end of this DescribeVpcFirewallAclRulePriorUsedResponse.  # noqa: E501
        :type: int
        """

        self._end = end

    @property
    def start(self):
        """Gets the start of this DescribeVpcFirewallAclRulePriorUsedResponse.  # noqa: E501


        :return: The start of this DescribeVpcFirewallAclRulePriorUsedResponse.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this DescribeVpcFirewallAclRulePriorUsedResponse.


        :param start: The start of this DescribeVpcFirewallAclRulePriorUsedResponse.  # noqa: E501
        :type: int
        """

        self._start = start

    @property
    def vpc_firewall_id(self):
        """Gets the vpc_firewall_id of this DescribeVpcFirewallAclRulePriorUsedResponse.  # noqa: E501


        :return: The vpc_firewall_id of this DescribeVpcFirewallAclRulePriorUsedResponse.  # noqa: E501
        :rtype: str
        """
        return self._vpc_firewall_id

    @vpc_firewall_id.setter
    def vpc_firewall_id(self, vpc_firewall_id):
        """Sets the vpc_firewall_id of this DescribeVpcFirewallAclRulePriorUsedResponse.


        :param vpc_firewall_id: The vpc_firewall_id of this DescribeVpcFirewallAclRulePriorUsedResponse.  # noqa: E501
        :type: str
        """

        self._vpc_firewall_id = vpc_firewall_id

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
        if issubclass(DescribeVpcFirewallAclRulePriorUsedResponse, dict):
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
        if not isinstance(other, DescribeVpcFirewallAclRulePriorUsedResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeVpcFirewallAclRulePriorUsedResponse):
            return True

        return self.to_dict() != other.to_dict()
