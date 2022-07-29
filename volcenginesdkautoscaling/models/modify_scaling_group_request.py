# coding: utf-8

"""
    auto_scaling

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ModifyScalingGroupRequest(object):
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
        'active_scaling_configuration_id': 'str',
        'default_cooldown': 'int',
        'desire_instance_number': 'int',
        'instance_terminate_policy': 'str',
        'max_instance_number': 'int',
        'min_instance_number': 'int',
        'scaling_group_id': 'str',
        'scaling_group_name': 'str',
        'subnet_ids': 'list[str]'
    }

    attribute_map = {
        'active_scaling_configuration_id': 'ActiveScalingConfigurationId',
        'default_cooldown': 'DefaultCooldown',
        'desire_instance_number': 'DesireInstanceNumber',
        'instance_terminate_policy': 'InstanceTerminatePolicy',
        'max_instance_number': 'MaxInstanceNumber',
        'min_instance_number': 'MinInstanceNumber',
        'scaling_group_id': 'ScalingGroupId',
        'scaling_group_name': 'ScalingGroupName',
        'subnet_ids': 'SubnetIds'
    }

    def __init__(self, active_scaling_configuration_id=None, default_cooldown=None, desire_instance_number=None, instance_terminate_policy=None, max_instance_number=None, min_instance_number=None, scaling_group_id=None, scaling_group_name=None, subnet_ids=None, _configuration=None):  # noqa: E501
        """ModifyScalingGroupRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._active_scaling_configuration_id = None
        self._default_cooldown = None
        self._desire_instance_number = None
        self._instance_terminate_policy = None
        self._max_instance_number = None
        self._min_instance_number = None
        self._scaling_group_id = None
        self._scaling_group_name = None
        self._subnet_ids = None
        self.discriminator = None

        if active_scaling_configuration_id is not None:
            self.active_scaling_configuration_id = active_scaling_configuration_id
        if default_cooldown is not None:
            self.default_cooldown = default_cooldown
        if desire_instance_number is not None:
            self.desire_instance_number = desire_instance_number
        if instance_terminate_policy is not None:
            self.instance_terminate_policy = instance_terminate_policy
        if max_instance_number is not None:
            self.max_instance_number = max_instance_number
        if min_instance_number is not None:
            self.min_instance_number = min_instance_number
        if scaling_group_id is not None:
            self.scaling_group_id = scaling_group_id
        if scaling_group_name is not None:
            self.scaling_group_name = scaling_group_name
        if subnet_ids is not None:
            self.subnet_ids = subnet_ids

    @property
    def active_scaling_configuration_id(self):
        """Gets the active_scaling_configuration_id of this ModifyScalingGroupRequest.  # noqa: E501


        :return: The active_scaling_configuration_id of this ModifyScalingGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._active_scaling_configuration_id

    @active_scaling_configuration_id.setter
    def active_scaling_configuration_id(self, active_scaling_configuration_id):
        """Sets the active_scaling_configuration_id of this ModifyScalingGroupRequest.


        :param active_scaling_configuration_id: The active_scaling_configuration_id of this ModifyScalingGroupRequest.  # noqa: E501
        :type: str
        """

        self._active_scaling_configuration_id = active_scaling_configuration_id

    @property
    def default_cooldown(self):
        """Gets the default_cooldown of this ModifyScalingGroupRequest.  # noqa: E501


        :return: The default_cooldown of this ModifyScalingGroupRequest.  # noqa: E501
        :rtype: int
        """
        return self._default_cooldown

    @default_cooldown.setter
    def default_cooldown(self, default_cooldown):
        """Sets the default_cooldown of this ModifyScalingGroupRequest.


        :param default_cooldown: The default_cooldown of this ModifyScalingGroupRequest.  # noqa: E501
        :type: int
        """

        self._default_cooldown = default_cooldown

    @property
    def desire_instance_number(self):
        """Gets the desire_instance_number of this ModifyScalingGroupRequest.  # noqa: E501


        :return: The desire_instance_number of this ModifyScalingGroupRequest.  # noqa: E501
        :rtype: int
        """
        return self._desire_instance_number

    @desire_instance_number.setter
    def desire_instance_number(self, desire_instance_number):
        """Sets the desire_instance_number of this ModifyScalingGroupRequest.


        :param desire_instance_number: The desire_instance_number of this ModifyScalingGroupRequest.  # noqa: E501
        :type: int
        """

        self._desire_instance_number = desire_instance_number

    @property
    def instance_terminate_policy(self):
        """Gets the instance_terminate_policy of this ModifyScalingGroupRequest.  # noqa: E501


        :return: The instance_terminate_policy of this ModifyScalingGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_terminate_policy

    @instance_terminate_policy.setter
    def instance_terminate_policy(self, instance_terminate_policy):
        """Sets the instance_terminate_policy of this ModifyScalingGroupRequest.


        :param instance_terminate_policy: The instance_terminate_policy of this ModifyScalingGroupRequest.  # noqa: E501
        :type: str
        """

        self._instance_terminate_policy = instance_terminate_policy

    @property
    def max_instance_number(self):
        """Gets the max_instance_number of this ModifyScalingGroupRequest.  # noqa: E501


        :return: The max_instance_number of this ModifyScalingGroupRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_instance_number

    @max_instance_number.setter
    def max_instance_number(self, max_instance_number):
        """Sets the max_instance_number of this ModifyScalingGroupRequest.


        :param max_instance_number: The max_instance_number of this ModifyScalingGroupRequest.  # noqa: E501
        :type: int
        """

        self._max_instance_number = max_instance_number

    @property
    def min_instance_number(self):
        """Gets the min_instance_number of this ModifyScalingGroupRequest.  # noqa: E501


        :return: The min_instance_number of this ModifyScalingGroupRequest.  # noqa: E501
        :rtype: int
        """
        return self._min_instance_number

    @min_instance_number.setter
    def min_instance_number(self, min_instance_number):
        """Sets the min_instance_number of this ModifyScalingGroupRequest.


        :param min_instance_number: The min_instance_number of this ModifyScalingGroupRequest.  # noqa: E501
        :type: int
        """

        self._min_instance_number = min_instance_number

    @property
    def scaling_group_id(self):
        """Gets the scaling_group_id of this ModifyScalingGroupRequest.  # noqa: E501


        :return: The scaling_group_id of this ModifyScalingGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._scaling_group_id

    @scaling_group_id.setter
    def scaling_group_id(self, scaling_group_id):
        """Sets the scaling_group_id of this ModifyScalingGroupRequest.


        :param scaling_group_id: The scaling_group_id of this ModifyScalingGroupRequest.  # noqa: E501
        :type: str
        """

        self._scaling_group_id = scaling_group_id

    @property
    def scaling_group_name(self):
        """Gets the scaling_group_name of this ModifyScalingGroupRequest.  # noqa: E501


        :return: The scaling_group_name of this ModifyScalingGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._scaling_group_name

    @scaling_group_name.setter
    def scaling_group_name(self, scaling_group_name):
        """Sets the scaling_group_name of this ModifyScalingGroupRequest.


        :param scaling_group_name: The scaling_group_name of this ModifyScalingGroupRequest.  # noqa: E501
        :type: str
        """

        self._scaling_group_name = scaling_group_name

    @property
    def subnet_ids(self):
        """Gets the subnet_ids of this ModifyScalingGroupRequest.  # noqa: E501


        :return: The subnet_ids of this ModifyScalingGroupRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._subnet_ids

    @subnet_ids.setter
    def subnet_ids(self, subnet_ids):
        """Sets the subnet_ids of this ModifyScalingGroupRequest.


        :param subnet_ids: The subnet_ids of this ModifyScalingGroupRequest.  # noqa: E501
        :type: list[str]
        """

        self._subnet_ids = subnet_ids

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
        if issubclass(ModifyScalingGroupRequest, dict):
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
        if not isinstance(other, ModifyScalingGroupRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyScalingGroupRequest):
            return True

        return self.to_dict() != other.to_dict()
