# coding: utf-8

"""
    cr

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ItemForListRepositoriesOutput(object):
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
        'access_level': 'str',
        'create_time': 'str',
        'description': 'str',
        'name': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'access_level': 'AccessLevel',
        'create_time': 'CreateTime',
        'description': 'Description',
        'name': 'Name',
        'update_time': 'UpdateTime'
    }

    def __init__(self, access_level=None, create_time=None, description=None, name=None, update_time=None, _configuration=None):  # noqa: E501
        """ItemForListRepositoriesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access_level = None
        self._create_time = None
        self._description = None
        self._name = None
        self._update_time = None
        self.discriminator = None

        if access_level is not None:
            self.access_level = access_level
        if create_time is not None:
            self.create_time = create_time
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if update_time is not None:
            self.update_time = update_time

    @property
    def access_level(self):
        """Gets the access_level of this ItemForListRepositoriesOutput.  # noqa: E501


        :return: The access_level of this ItemForListRepositoriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._access_level

    @access_level.setter
    def access_level(self, access_level):
        """Sets the access_level of this ItemForListRepositoriesOutput.


        :param access_level: The access_level of this ItemForListRepositoriesOutput.  # noqa: E501
        :type: str
        """

        self._access_level = access_level

    @property
    def create_time(self):
        """Gets the create_time of this ItemForListRepositoriesOutput.  # noqa: E501


        :return: The create_time of this ItemForListRepositoriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ItemForListRepositoriesOutput.


        :param create_time: The create_time of this ItemForListRepositoriesOutput.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def description(self):
        """Gets the description of this ItemForListRepositoriesOutput.  # noqa: E501


        :return: The description of this ItemForListRepositoriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ItemForListRepositoriesOutput.


        :param description: The description of this ItemForListRepositoriesOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this ItemForListRepositoriesOutput.  # noqa: E501


        :return: The name of this ItemForListRepositoriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ItemForListRepositoriesOutput.


        :param name: The name of this ItemForListRepositoriesOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def update_time(self):
        """Gets the update_time of this ItemForListRepositoriesOutput.  # noqa: E501


        :return: The update_time of this ItemForListRepositoriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ItemForListRepositoriesOutput.


        :param update_time: The update_time of this ItemForListRepositoriesOutput.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

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
        if issubclass(ItemForListRepositoriesOutput, dict):
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
        if not isinstance(other, ItemForListRepositoriesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemForListRepositoriesOutput):
            return True

        return self.to_dict() != other.to_dict()
