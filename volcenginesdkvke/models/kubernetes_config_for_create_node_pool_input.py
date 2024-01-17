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


class KubernetesConfigForCreateNodePoolInput(object):
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
        'cordon': 'bool',
        'labels': 'list[LabelForCreateNodePoolInput]',
        'name_prefix': 'str',
        'taints': 'list[TaintForCreateNodePoolInput]'
    }

    attribute_map = {
        'cordon': 'Cordon',
        'labels': 'Labels',
        'name_prefix': 'NamePrefix',
        'taints': 'Taints'
    }

    def __init__(self, cordon=None, labels=None, name_prefix=None, taints=None, _configuration=None):  # noqa: E501
        """KubernetesConfigForCreateNodePoolInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cordon = None
        self._labels = None
        self._name_prefix = None
        self._taints = None
        self.discriminator = None

        if cordon is not None:
            self.cordon = cordon
        if labels is not None:
            self.labels = labels
        if name_prefix is not None:
            self.name_prefix = name_prefix
        if taints is not None:
            self.taints = taints

    @property
    def cordon(self):
        """Gets the cordon of this KubernetesConfigForCreateNodePoolInput.  # noqa: E501


        :return: The cordon of this KubernetesConfigForCreateNodePoolInput.  # noqa: E501
        :rtype: bool
        """
        return self._cordon

    @cordon.setter
    def cordon(self, cordon):
        """Sets the cordon of this KubernetesConfigForCreateNodePoolInput.


        :param cordon: The cordon of this KubernetesConfigForCreateNodePoolInput.  # noqa: E501
        :type: bool
        """

        self._cordon = cordon

    @property
    def labels(self):
        """Gets the labels of this KubernetesConfigForCreateNodePoolInput.  # noqa: E501


        :return: The labels of this KubernetesConfigForCreateNodePoolInput.  # noqa: E501
        :rtype: list[LabelForCreateNodePoolInput]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this KubernetesConfigForCreateNodePoolInput.


        :param labels: The labels of this KubernetesConfigForCreateNodePoolInput.  # noqa: E501
        :type: list[LabelForCreateNodePoolInput]
        """

        self._labels = labels

    @property
    def name_prefix(self):
        """Gets the name_prefix of this KubernetesConfigForCreateNodePoolInput.  # noqa: E501


        :return: The name_prefix of this KubernetesConfigForCreateNodePoolInput.  # noqa: E501
        :rtype: str
        """
        return self._name_prefix

    @name_prefix.setter
    def name_prefix(self, name_prefix):
        """Sets the name_prefix of this KubernetesConfigForCreateNodePoolInput.


        :param name_prefix: The name_prefix of this KubernetesConfigForCreateNodePoolInput.  # noqa: E501
        :type: str
        """

        self._name_prefix = name_prefix

    @property
    def taints(self):
        """Gets the taints of this KubernetesConfigForCreateNodePoolInput.  # noqa: E501


        :return: The taints of this KubernetesConfigForCreateNodePoolInput.  # noqa: E501
        :rtype: list[TaintForCreateNodePoolInput]
        """
        return self._taints

    @taints.setter
    def taints(self, taints):
        """Sets the taints of this KubernetesConfigForCreateNodePoolInput.


        :param taints: The taints of this KubernetesConfigForCreateNodePoolInput.  # noqa: E501
        :type: list[TaintForCreateNodePoolInput]
        """

        self._taints = taints

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
        if issubclass(KubernetesConfigForCreateNodePoolInput, dict):
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
        if not isinstance(other, KubernetesConfigForCreateNodePoolInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KubernetesConfigForCreateNodePoolInput):
            return True

        return self.to_dict() != other.to_dict()
