# coding: utf-8

"""
    redis

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeAllowListDetailResponse(object):
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
        'allow_list': 'str',
        'allow_list_desc': 'str',
        'allow_list_id': 'str',
        'allow_list_name': 'str',
        'allow_list_type': 'str',
        'associated_instances': 'list[AssociatedInstanceForDescribeAllowListDetailOutput]'
    }

    attribute_map = {
        'allow_list': 'AllowList',
        'allow_list_desc': 'AllowListDesc',
        'allow_list_id': 'AllowListId',
        'allow_list_name': 'AllowListName',
        'allow_list_type': 'AllowListType',
        'associated_instances': 'AssociatedInstances'
    }

    def __init__(self, allow_list=None, allow_list_desc=None, allow_list_id=None, allow_list_name=None, allow_list_type=None, associated_instances=None, _configuration=None):  # noqa: E501
        """DescribeAllowListDetailResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allow_list = None
        self._allow_list_desc = None
        self._allow_list_id = None
        self._allow_list_name = None
        self._allow_list_type = None
        self._associated_instances = None
        self.discriminator = None

        if allow_list is not None:
            self.allow_list = allow_list
        if allow_list_desc is not None:
            self.allow_list_desc = allow_list_desc
        if allow_list_id is not None:
            self.allow_list_id = allow_list_id
        if allow_list_name is not None:
            self.allow_list_name = allow_list_name
        if allow_list_type is not None:
            self.allow_list_type = allow_list_type
        if associated_instances is not None:
            self.associated_instances = associated_instances

    @property
    def allow_list(self):
        """Gets the allow_list of this DescribeAllowListDetailResponse.  # noqa: E501


        :return: The allow_list of this DescribeAllowListDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._allow_list

    @allow_list.setter
    def allow_list(self, allow_list):
        """Sets the allow_list of this DescribeAllowListDetailResponse.


        :param allow_list: The allow_list of this DescribeAllowListDetailResponse.  # noqa: E501
        :type: str
        """

        self._allow_list = allow_list

    @property
    def allow_list_desc(self):
        """Gets the allow_list_desc of this DescribeAllowListDetailResponse.  # noqa: E501


        :return: The allow_list_desc of this DescribeAllowListDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._allow_list_desc

    @allow_list_desc.setter
    def allow_list_desc(self, allow_list_desc):
        """Sets the allow_list_desc of this DescribeAllowListDetailResponse.


        :param allow_list_desc: The allow_list_desc of this DescribeAllowListDetailResponse.  # noqa: E501
        :type: str
        """

        self._allow_list_desc = allow_list_desc

    @property
    def allow_list_id(self):
        """Gets the allow_list_id of this DescribeAllowListDetailResponse.  # noqa: E501


        :return: The allow_list_id of this DescribeAllowListDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._allow_list_id

    @allow_list_id.setter
    def allow_list_id(self, allow_list_id):
        """Sets the allow_list_id of this DescribeAllowListDetailResponse.


        :param allow_list_id: The allow_list_id of this DescribeAllowListDetailResponse.  # noqa: E501
        :type: str
        """

        self._allow_list_id = allow_list_id

    @property
    def allow_list_name(self):
        """Gets the allow_list_name of this DescribeAllowListDetailResponse.  # noqa: E501


        :return: The allow_list_name of this DescribeAllowListDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._allow_list_name

    @allow_list_name.setter
    def allow_list_name(self, allow_list_name):
        """Sets the allow_list_name of this DescribeAllowListDetailResponse.


        :param allow_list_name: The allow_list_name of this DescribeAllowListDetailResponse.  # noqa: E501
        :type: str
        """

        self._allow_list_name = allow_list_name

    @property
    def allow_list_type(self):
        """Gets the allow_list_type of this DescribeAllowListDetailResponse.  # noqa: E501


        :return: The allow_list_type of this DescribeAllowListDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._allow_list_type

    @allow_list_type.setter
    def allow_list_type(self, allow_list_type):
        """Sets the allow_list_type of this DescribeAllowListDetailResponse.


        :param allow_list_type: The allow_list_type of this DescribeAllowListDetailResponse.  # noqa: E501
        :type: str
        """

        self._allow_list_type = allow_list_type

    @property
    def associated_instances(self):
        """Gets the associated_instances of this DescribeAllowListDetailResponse.  # noqa: E501


        :return: The associated_instances of this DescribeAllowListDetailResponse.  # noqa: E501
        :rtype: list[AssociatedInstanceForDescribeAllowListDetailOutput]
        """
        return self._associated_instances

    @associated_instances.setter
    def associated_instances(self, associated_instances):
        """Sets the associated_instances of this DescribeAllowListDetailResponse.


        :param associated_instances: The associated_instances of this DescribeAllowListDetailResponse.  # noqa: E501
        :type: list[AssociatedInstanceForDescribeAllowListDetailOutput]
        """

        self._associated_instances = associated_instances

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
        if issubclass(DescribeAllowListDetailResponse, dict):
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
        if not isinstance(other, DescribeAllowListDetailResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeAllowListDetailResponse):
            return True

        return self.to_dict() != other.to_dict()
