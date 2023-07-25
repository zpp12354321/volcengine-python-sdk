# coding: utf-8

"""
    kafka

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ModifyInstanceSpecRequest(object):
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
        'compute_spec': 'str',
        'instance_id': 'str',
        'need_rebalance': 'bool',
        'partition_number': 'int',
        'rebalance_time': 'str',
        'storage_space': 'int'
    }

    attribute_map = {
        'compute_spec': 'ComputeSpec',
        'instance_id': 'InstanceId',
        'need_rebalance': 'NeedRebalance',
        'partition_number': 'PartitionNumber',
        'rebalance_time': 'RebalanceTime',
        'storage_space': 'StorageSpace'
    }

    def __init__(self, compute_spec=None, instance_id=None, need_rebalance=None, partition_number=None, rebalance_time=None, storage_space=None, _configuration=None):  # noqa: E501
        """ModifyInstanceSpecRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._compute_spec = None
        self._instance_id = None
        self._need_rebalance = None
        self._partition_number = None
        self._rebalance_time = None
        self._storage_space = None
        self.discriminator = None

        if compute_spec is not None:
            self.compute_spec = compute_spec
        if instance_id is not None:
            self.instance_id = instance_id
        if need_rebalance is not None:
            self.need_rebalance = need_rebalance
        if partition_number is not None:
            self.partition_number = partition_number
        if rebalance_time is not None:
            self.rebalance_time = rebalance_time
        if storage_space is not None:
            self.storage_space = storage_space

    @property
    def compute_spec(self):
        """Gets the compute_spec of this ModifyInstanceSpecRequest.  # noqa: E501


        :return: The compute_spec of this ModifyInstanceSpecRequest.  # noqa: E501
        :rtype: str
        """
        return self._compute_spec

    @compute_spec.setter
    def compute_spec(self, compute_spec):
        """Sets the compute_spec of this ModifyInstanceSpecRequest.


        :param compute_spec: The compute_spec of this ModifyInstanceSpecRequest.  # noqa: E501
        :type: str
        """

        self._compute_spec = compute_spec

    @property
    def instance_id(self):
        """Gets the instance_id of this ModifyInstanceSpecRequest.  # noqa: E501


        :return: The instance_id of this ModifyInstanceSpecRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ModifyInstanceSpecRequest.


        :param instance_id: The instance_id of this ModifyInstanceSpecRequest.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def need_rebalance(self):
        """Gets the need_rebalance of this ModifyInstanceSpecRequest.  # noqa: E501


        :return: The need_rebalance of this ModifyInstanceSpecRequest.  # noqa: E501
        :rtype: bool
        """
        return self._need_rebalance

    @need_rebalance.setter
    def need_rebalance(self, need_rebalance):
        """Sets the need_rebalance of this ModifyInstanceSpecRequest.


        :param need_rebalance: The need_rebalance of this ModifyInstanceSpecRequest.  # noqa: E501
        :type: bool
        """

        self._need_rebalance = need_rebalance

    @property
    def partition_number(self):
        """Gets the partition_number of this ModifyInstanceSpecRequest.  # noqa: E501


        :return: The partition_number of this ModifyInstanceSpecRequest.  # noqa: E501
        :rtype: int
        """
        return self._partition_number

    @partition_number.setter
    def partition_number(self, partition_number):
        """Sets the partition_number of this ModifyInstanceSpecRequest.


        :param partition_number: The partition_number of this ModifyInstanceSpecRequest.  # noqa: E501
        :type: int
        """

        self._partition_number = partition_number

    @property
    def rebalance_time(self):
        """Gets the rebalance_time of this ModifyInstanceSpecRequest.  # noqa: E501


        :return: The rebalance_time of this ModifyInstanceSpecRequest.  # noqa: E501
        :rtype: str
        """
        return self._rebalance_time

    @rebalance_time.setter
    def rebalance_time(self, rebalance_time):
        """Sets the rebalance_time of this ModifyInstanceSpecRequest.


        :param rebalance_time: The rebalance_time of this ModifyInstanceSpecRequest.  # noqa: E501
        :type: str
        """

        self._rebalance_time = rebalance_time

    @property
    def storage_space(self):
        """Gets the storage_space of this ModifyInstanceSpecRequest.  # noqa: E501


        :return: The storage_space of this ModifyInstanceSpecRequest.  # noqa: E501
        :rtype: int
        """
        return self._storage_space

    @storage_space.setter
    def storage_space(self, storage_space):
        """Sets the storage_space of this ModifyInstanceSpecRequest.


        :param storage_space: The storage_space of this ModifyInstanceSpecRequest.  # noqa: E501
        :type: int
        """

        self._storage_space = storage_space

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
        if issubclass(ModifyInstanceSpecRequest, dict):
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
        if not isinstance(other, ModifyInstanceSpecRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyInstanceSpecRequest):
            return True

        return self.to_dict() != other.to_dict()
