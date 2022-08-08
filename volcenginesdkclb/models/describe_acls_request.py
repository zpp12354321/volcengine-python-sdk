# coding: utf-8

"""
    clb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeAclsRequest(object):
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
        'acl_ids': 'list[str]',
        'acl_name': 'str',
        'page_number': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'acl_ids': 'AclIds',
        'acl_name': 'AclName',
        'page_number': 'PageNumber',
        'page_size': 'PageSize'
    }

    def __init__(self, acl_ids=None, acl_name=None, page_number=None, page_size=None, _configuration=None):  # noqa: E501
        """DescribeAclsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._acl_ids = None
        self._acl_name = None
        self._page_number = None
        self._page_size = None
        self.discriminator = None

        if acl_ids is not None:
            self.acl_ids = acl_ids
        if acl_name is not None:
            self.acl_name = acl_name
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size

    @property
    def acl_ids(self):
        """Gets the acl_ids of this DescribeAclsRequest.  # noqa: E501


        :return: The acl_ids of this DescribeAclsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._acl_ids

    @acl_ids.setter
    def acl_ids(self, acl_ids):
        """Sets the acl_ids of this DescribeAclsRequest.


        :param acl_ids: The acl_ids of this DescribeAclsRequest.  # noqa: E501
        :type: list[str]
        """

        self._acl_ids = acl_ids

    @property
    def acl_name(self):
        """Gets the acl_name of this DescribeAclsRequest.  # noqa: E501


        :return: The acl_name of this DescribeAclsRequest.  # noqa: E501
        :rtype: str
        """
        return self._acl_name

    @acl_name.setter
    def acl_name(self, acl_name):
        """Sets the acl_name of this DescribeAclsRequest.


        :param acl_name: The acl_name of this DescribeAclsRequest.  # noqa: E501
        :type: str
        """

        self._acl_name = acl_name

    @property
    def page_number(self):
        """Gets the page_number of this DescribeAclsRequest.  # noqa: E501


        :return: The page_number of this DescribeAclsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeAclsRequest.


        :param page_number: The page_number of this DescribeAclsRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeAclsRequest.  # noqa: E501


        :return: The page_size of this DescribeAclsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeAclsRequest.


        :param page_size: The page_size of this DescribeAclsRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

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
        if issubclass(DescribeAclsRequest, dict):
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
        if not isinstance(other, DescribeAclsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeAclsRequest):
            return True

        return self.to_dict() != other.to_dict()
