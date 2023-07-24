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


class TopicsInfoForDescribeTopicsOutput(object):
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
        'create_time': 'str',
        'description': 'str',
        'partition_number': 'int',
        'replica_number': 'int',
        'status': 'str',
        'topic_name': 'str'
    }

    attribute_map = {
        'create_time': 'CreateTime',
        'description': 'Description',
        'partition_number': 'PartitionNumber',
        'replica_number': 'ReplicaNumber',
        'status': 'Status',
        'topic_name': 'TopicName'
    }

    def __init__(self, create_time=None, description=None, partition_number=None, replica_number=None, status=None, topic_name=None, _configuration=None):  # noqa: E501
        """TopicsInfoForDescribeTopicsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._create_time = None
        self._description = None
        self._partition_number = None
        self._replica_number = None
        self._status = None
        self._topic_name = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if description is not None:
            self.description = description
        if partition_number is not None:
            self.partition_number = partition_number
        if replica_number is not None:
            self.replica_number = replica_number
        if status is not None:
            self.status = status
        if topic_name is not None:
            self.topic_name = topic_name

    @property
    def create_time(self):
        """Gets the create_time of this TopicsInfoForDescribeTopicsOutput.  # noqa: E501


        :return: The create_time of this TopicsInfoForDescribeTopicsOutput.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this TopicsInfoForDescribeTopicsOutput.


        :param create_time: The create_time of this TopicsInfoForDescribeTopicsOutput.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def description(self):
        """Gets the description of this TopicsInfoForDescribeTopicsOutput.  # noqa: E501


        :return: The description of this TopicsInfoForDescribeTopicsOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TopicsInfoForDescribeTopicsOutput.


        :param description: The description of this TopicsInfoForDescribeTopicsOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def partition_number(self):
        """Gets the partition_number of this TopicsInfoForDescribeTopicsOutput.  # noqa: E501


        :return: The partition_number of this TopicsInfoForDescribeTopicsOutput.  # noqa: E501
        :rtype: int
        """
        return self._partition_number

    @partition_number.setter
    def partition_number(self, partition_number):
        """Sets the partition_number of this TopicsInfoForDescribeTopicsOutput.


        :param partition_number: The partition_number of this TopicsInfoForDescribeTopicsOutput.  # noqa: E501
        :type: int
        """

        self._partition_number = partition_number

    @property
    def replica_number(self):
        """Gets the replica_number of this TopicsInfoForDescribeTopicsOutput.  # noqa: E501


        :return: The replica_number of this TopicsInfoForDescribeTopicsOutput.  # noqa: E501
        :rtype: int
        """
        return self._replica_number

    @replica_number.setter
    def replica_number(self, replica_number):
        """Sets the replica_number of this TopicsInfoForDescribeTopicsOutput.


        :param replica_number: The replica_number of this TopicsInfoForDescribeTopicsOutput.  # noqa: E501
        :type: int
        """

        self._replica_number = replica_number

    @property
    def status(self):
        """Gets the status of this TopicsInfoForDescribeTopicsOutput.  # noqa: E501


        :return: The status of this TopicsInfoForDescribeTopicsOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TopicsInfoForDescribeTopicsOutput.


        :param status: The status of this TopicsInfoForDescribeTopicsOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def topic_name(self):
        """Gets the topic_name of this TopicsInfoForDescribeTopicsOutput.  # noqa: E501


        :return: The topic_name of this TopicsInfoForDescribeTopicsOutput.  # noqa: E501
        :rtype: str
        """
        return self._topic_name

    @topic_name.setter
    def topic_name(self, topic_name):
        """Sets the topic_name of this TopicsInfoForDescribeTopicsOutput.


        :param topic_name: The topic_name of this TopicsInfoForDescribeTopicsOutput.  # noqa: E501
        :type: str
        """

        self._topic_name = topic_name

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
        if issubclass(TopicsInfoForDescribeTopicsOutput, dict):
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
        if not isinstance(other, TopicsInfoForDescribeTopicsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TopicsInfoForDescribeTopicsOutput):
            return True

        return self.to_dict() != other.to_dict()
