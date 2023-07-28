# coding: utf-8

"""
    rds_mysql_v2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ModifyDBInstanceNameRequest(object):
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
        'instance_id': 'str',
        'instance_new_name': 'str'
    }

    attribute_map = {
        'instance_id': 'InstanceId',
        'instance_new_name': 'InstanceNewName'
    }

    def __init__(self, instance_id=None, instance_new_name=None, _configuration=None):  # noqa: E501
        """ModifyDBInstanceNameRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._instance_id = None
        self._instance_new_name = None
        self.discriminator = None

        self.instance_id = instance_id
        self.instance_new_name = instance_new_name

    @property
    def instance_id(self):
        """Gets the instance_id of this ModifyDBInstanceNameRequest.  # noqa: E501


        :return: The instance_id of this ModifyDBInstanceNameRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ModifyDBInstanceNameRequest.


        :param instance_id: The instance_id of this ModifyDBInstanceNameRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_id is None:
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def instance_new_name(self):
        """Gets the instance_new_name of this ModifyDBInstanceNameRequest.  # noqa: E501


        :return: The instance_new_name of this ModifyDBInstanceNameRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_new_name

    @instance_new_name.setter
    def instance_new_name(self, instance_new_name):
        """Sets the instance_new_name of this ModifyDBInstanceNameRequest.


        :param instance_new_name: The instance_new_name of this ModifyDBInstanceNameRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_new_name is None:
            raise ValueError("Invalid value for `instance_new_name`, must not be `None`")  # noqa: E501

        self._instance_new_name = instance_new_name

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
        if issubclass(ModifyDBInstanceNameRequest, dict):
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
        if not isinstance(other, ModifyDBInstanceNameRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyDBInstanceNameRequest):
            return True

        return self.to_dict() != other.to_dict()
