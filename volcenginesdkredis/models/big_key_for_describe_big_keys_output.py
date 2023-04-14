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


class BigKeyForDescribeBigKeysOutput(object):
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
        'db_name': 'str',
        'key_info': 'str',
        'key_type': 'str',
        'value_len': 'str',
        'value_size': 'str'
    }

    attribute_map = {
        'db_name': 'DBName',
        'key_info': 'KeyInfo',
        'key_type': 'KeyType',
        'value_len': 'ValueLen',
        'value_size': 'ValueSize'
    }

    def __init__(self, db_name=None, key_info=None, key_type=None, value_len=None, value_size=None, _configuration=None):  # noqa: E501
        """BigKeyForDescribeBigKeysOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._db_name = None
        self._key_info = None
        self._key_type = None
        self._value_len = None
        self._value_size = None
        self.discriminator = None

        if db_name is not None:
            self.db_name = db_name
        if key_info is not None:
            self.key_info = key_info
        if key_type is not None:
            self.key_type = key_type
        if value_len is not None:
            self.value_len = value_len
        if value_size is not None:
            self.value_size = value_size

    @property
    def db_name(self):
        """Gets the db_name of this BigKeyForDescribeBigKeysOutput.  # noqa: E501


        :return: The db_name of this BigKeyForDescribeBigKeysOutput.  # noqa: E501
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this BigKeyForDescribeBigKeysOutput.


        :param db_name: The db_name of this BigKeyForDescribeBigKeysOutput.  # noqa: E501
        :type: str
        """

        self._db_name = db_name

    @property
    def key_info(self):
        """Gets the key_info of this BigKeyForDescribeBigKeysOutput.  # noqa: E501


        :return: The key_info of this BigKeyForDescribeBigKeysOutput.  # noqa: E501
        :rtype: str
        """
        return self._key_info

    @key_info.setter
    def key_info(self, key_info):
        """Sets the key_info of this BigKeyForDescribeBigKeysOutput.


        :param key_info: The key_info of this BigKeyForDescribeBigKeysOutput.  # noqa: E501
        :type: str
        """

        self._key_info = key_info

    @property
    def key_type(self):
        """Gets the key_type of this BigKeyForDescribeBigKeysOutput.  # noqa: E501


        :return: The key_type of this BigKeyForDescribeBigKeysOutput.  # noqa: E501
        :rtype: str
        """
        return self._key_type

    @key_type.setter
    def key_type(self, key_type):
        """Sets the key_type of this BigKeyForDescribeBigKeysOutput.


        :param key_type: The key_type of this BigKeyForDescribeBigKeysOutput.  # noqa: E501
        :type: str
        """

        self._key_type = key_type

    @property
    def value_len(self):
        """Gets the value_len of this BigKeyForDescribeBigKeysOutput.  # noqa: E501


        :return: The value_len of this BigKeyForDescribeBigKeysOutput.  # noqa: E501
        :rtype: str
        """
        return self._value_len

    @value_len.setter
    def value_len(self, value_len):
        """Sets the value_len of this BigKeyForDescribeBigKeysOutput.


        :param value_len: The value_len of this BigKeyForDescribeBigKeysOutput.  # noqa: E501
        :type: str
        """

        self._value_len = value_len

    @property
    def value_size(self):
        """Gets the value_size of this BigKeyForDescribeBigKeysOutput.  # noqa: E501


        :return: The value_size of this BigKeyForDescribeBigKeysOutput.  # noqa: E501
        :rtype: str
        """
        return self._value_size

    @value_size.setter
    def value_size(self, value_size):
        """Sets the value_size of this BigKeyForDescribeBigKeysOutput.


        :param value_size: The value_size of this BigKeyForDescribeBigKeysOutput.  # noqa: E501
        :type: str
        """

        self._value_size = value_size

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
        if issubclass(BigKeyForDescribeBigKeysOutput, dict):
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
        if not isinstance(other, BigKeyForDescribeBigKeysOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BigKeyForDescribeBigKeysOutput):
            return True

        return self.to_dict() != other.to_dict()
