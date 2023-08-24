# coding: utf-8

"""
    iam

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class MoveProjectResourceRequest(object):
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
        'resource_trn': 'list[str]',
        'target_project_name': 'str'
    }

    attribute_map = {
        'resource_trn': 'ResourceTrn',
        'target_project_name': 'TargetProjectName'
    }

    def __init__(self, resource_trn=None, target_project_name=None, _configuration=None):  # noqa: E501
        """MoveProjectResourceRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._resource_trn = None
        self._target_project_name = None
        self.discriminator = None

        if resource_trn is not None:
            self.resource_trn = resource_trn
        self.target_project_name = target_project_name

    @property
    def resource_trn(self):
        """Gets the resource_trn of this MoveProjectResourceRequest.  # noqa: E501


        :return: The resource_trn of this MoveProjectResourceRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._resource_trn

    @resource_trn.setter
    def resource_trn(self, resource_trn):
        """Sets the resource_trn of this MoveProjectResourceRequest.


        :param resource_trn: The resource_trn of this MoveProjectResourceRequest.  # noqa: E501
        :type: list[str]
        """

        self._resource_trn = resource_trn

    @property
    def target_project_name(self):
        """Gets the target_project_name of this MoveProjectResourceRequest.  # noqa: E501


        :return: The target_project_name of this MoveProjectResourceRequest.  # noqa: E501
        :rtype: str
        """
        return self._target_project_name

    @target_project_name.setter
    def target_project_name(self, target_project_name):
        """Sets the target_project_name of this MoveProjectResourceRequest.


        :param target_project_name: The target_project_name of this MoveProjectResourceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and target_project_name is None:
            raise ValueError("Invalid value for `target_project_name`, must not be `None`")  # noqa: E501

        self._target_project_name = target_project_name

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
        if issubclass(MoveProjectResourceRequest, dict):
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
        if not isinstance(other, MoveProjectResourceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MoveProjectResourceRequest):
            return True

        return self.to_dict() != other.to_dict()
