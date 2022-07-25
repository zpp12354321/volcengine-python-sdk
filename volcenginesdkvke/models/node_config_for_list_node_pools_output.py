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


class NodeConfigForListNodePoolsOutput(object):
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
        'additional_container_storage_enabled': 'bool',
        'data_volumes': 'list[DataVolumeForListNodePoolsOutput]',
        'initialize_script': 'str',
        'instance_type_ids': 'list[str]',
        'security': 'SecurityForListNodePoolsOutput',
        'subnet_ids': 'list[str]',
        'system_volume': 'SystemVolumeForListNodePoolsOutput'
    }

    attribute_map = {
        'additional_container_storage_enabled': 'AdditionalContainerStorageEnabled',
        'data_volumes': 'DataVolumes',
        'initialize_script': 'InitializeScript',
        'instance_type_ids': 'InstanceTypeIds',
        'security': 'Security',
        'subnet_ids': 'SubnetIds',
        'system_volume': 'SystemVolume'
    }

    def __init__(self, additional_container_storage_enabled=None, data_volumes=None, initialize_script=None, instance_type_ids=None, security=None, subnet_ids=None, system_volume=None, _configuration=None):  # noqa: E501
        """NodeConfigForListNodePoolsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._additional_container_storage_enabled = None
        self._data_volumes = None
        self._initialize_script = None
        self._instance_type_ids = None
        self._security = None
        self._subnet_ids = None
        self._system_volume = None
        self.discriminator = None

        if additional_container_storage_enabled is not None:
            self.additional_container_storage_enabled = additional_container_storage_enabled
        if data_volumes is not None:
            self.data_volumes = data_volumes
        if initialize_script is not None:
            self.initialize_script = initialize_script
        if instance_type_ids is not None:
            self.instance_type_ids = instance_type_ids
        if security is not None:
            self.security = security
        if subnet_ids is not None:
            self.subnet_ids = subnet_ids
        if system_volume is not None:
            self.system_volume = system_volume

    @property
    def additional_container_storage_enabled(self):
        """Gets the additional_container_storage_enabled of this NodeConfigForListNodePoolsOutput.  # noqa: E501


        :return: The additional_container_storage_enabled of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :rtype: bool
        """
        return self._additional_container_storage_enabled

    @additional_container_storage_enabled.setter
    def additional_container_storage_enabled(self, additional_container_storage_enabled):
        """Sets the additional_container_storage_enabled of this NodeConfigForListNodePoolsOutput.


        :param additional_container_storage_enabled: The additional_container_storage_enabled of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :type: bool
        """

        self._additional_container_storage_enabled = additional_container_storage_enabled

    @property
    def data_volumes(self):
        """Gets the data_volumes of this NodeConfigForListNodePoolsOutput.  # noqa: E501


        :return: The data_volumes of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :rtype: list[DataVolumeForListNodePoolsOutput]
        """
        return self._data_volumes

    @data_volumes.setter
    def data_volumes(self, data_volumes):
        """Sets the data_volumes of this NodeConfigForListNodePoolsOutput.


        :param data_volumes: The data_volumes of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :type: list[DataVolumeForListNodePoolsOutput]
        """

        self._data_volumes = data_volumes

    @property
    def initialize_script(self):
        """Gets the initialize_script of this NodeConfigForListNodePoolsOutput.  # noqa: E501


        :return: The initialize_script of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :rtype: str
        """
        return self._initialize_script

    @initialize_script.setter
    def initialize_script(self, initialize_script):
        """Sets the initialize_script of this NodeConfigForListNodePoolsOutput.


        :param initialize_script: The initialize_script of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :type: str
        """

        self._initialize_script = initialize_script

    @property
    def instance_type_ids(self):
        """Gets the instance_type_ids of this NodeConfigForListNodePoolsOutput.  # noqa: E501


        :return: The instance_type_ids of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._instance_type_ids

    @instance_type_ids.setter
    def instance_type_ids(self, instance_type_ids):
        """Sets the instance_type_ids of this NodeConfigForListNodePoolsOutput.


        :param instance_type_ids: The instance_type_ids of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :type: list[str]
        """

        self._instance_type_ids = instance_type_ids

    @property
    def security(self):
        """Gets the security of this NodeConfigForListNodePoolsOutput.  # noqa: E501


        :return: The security of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :rtype: SecurityForListNodePoolsOutput
        """
        return self._security

    @security.setter
    def security(self, security):
        """Sets the security of this NodeConfigForListNodePoolsOutput.


        :param security: The security of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :type: SecurityForListNodePoolsOutput
        """

        self._security = security

    @property
    def subnet_ids(self):
        """Gets the subnet_ids of this NodeConfigForListNodePoolsOutput.  # noqa: E501


        :return: The subnet_ids of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._subnet_ids

    @subnet_ids.setter
    def subnet_ids(self, subnet_ids):
        """Sets the subnet_ids of this NodeConfigForListNodePoolsOutput.


        :param subnet_ids: The subnet_ids of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :type: list[str]
        """

        self._subnet_ids = subnet_ids

    @property
    def system_volume(self):
        """Gets the system_volume of this NodeConfigForListNodePoolsOutput.  # noqa: E501


        :return: The system_volume of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :rtype: SystemVolumeForListNodePoolsOutput
        """
        return self._system_volume

    @system_volume.setter
    def system_volume(self, system_volume):
        """Sets the system_volume of this NodeConfigForListNodePoolsOutput.


        :param system_volume: The system_volume of this NodeConfigForListNodePoolsOutput.  # noqa: E501
        :type: SystemVolumeForListNodePoolsOutput
        """

        self._system_volume = system_volume

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
        if issubclass(NodeConfigForListNodePoolsOutput, dict):
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
        if not isinstance(other, NodeConfigForListNodePoolsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NodeConfigForListNodePoolsOutput):
            return True

        return self.to_dict() != other.to_dict()