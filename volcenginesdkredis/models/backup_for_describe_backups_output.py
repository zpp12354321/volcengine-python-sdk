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


class BackupForDescribeBackupsOutput(object):
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
        'backup_strategy': 'str',
        'backup_type': 'str',
        'end_time': 'str',
        'instance_detail': 'InstanceDetailForDescribeBackupsOutput',
        'instance_id': 'str',
        'size': 'int',
        'start_time': 'str',
        'status': 'str'
    }

    attribute_map = {
        'backup_strategy': 'BackupStrategy',
        'backup_type': 'BackupType',
        'end_time': 'EndTime',
        'instance_detail': 'InstanceDetail',
        'instance_id': 'InstanceId',
        'size': 'Size',
        'start_time': 'StartTime',
        'status': 'Status'
    }

    def __init__(self, backup_strategy=None, backup_type=None, end_time=None, instance_detail=None, instance_id=None, size=None, start_time=None, status=None, _configuration=None):  # noqa: E501
        """BackupForDescribeBackupsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._backup_strategy = None
        self._backup_type = None
        self._end_time = None
        self._instance_detail = None
        self._instance_id = None
        self._size = None
        self._start_time = None
        self._status = None
        self.discriminator = None

        if backup_strategy is not None:
            self.backup_strategy = backup_strategy
        if backup_type is not None:
            self.backup_type = backup_type
        if end_time is not None:
            self.end_time = end_time
        if instance_detail is not None:
            self.instance_detail = instance_detail
        if instance_id is not None:
            self.instance_id = instance_id
        if size is not None:
            self.size = size
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status

    @property
    def backup_strategy(self):
        """Gets the backup_strategy of this BackupForDescribeBackupsOutput.  # noqa: E501


        :return: The backup_strategy of this BackupForDescribeBackupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        """Sets the backup_strategy of this BackupForDescribeBackupsOutput.


        :param backup_strategy: The backup_strategy of this BackupForDescribeBackupsOutput.  # noqa: E501
        :type: str
        """

        self._backup_strategy = backup_strategy

    @property
    def backup_type(self):
        """Gets the backup_type of this BackupForDescribeBackupsOutput.  # noqa: E501


        :return: The backup_type of this BackupForDescribeBackupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        """Sets the backup_type of this BackupForDescribeBackupsOutput.


        :param backup_type: The backup_type of this BackupForDescribeBackupsOutput.  # noqa: E501
        :type: str
        """

        self._backup_type = backup_type

    @property
    def end_time(self):
        """Gets the end_time of this BackupForDescribeBackupsOutput.  # noqa: E501


        :return: The end_time of this BackupForDescribeBackupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this BackupForDescribeBackupsOutput.


        :param end_time: The end_time of this BackupForDescribeBackupsOutput.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

    @property
    def instance_detail(self):
        """Gets the instance_detail of this BackupForDescribeBackupsOutput.  # noqa: E501


        :return: The instance_detail of this BackupForDescribeBackupsOutput.  # noqa: E501
        :rtype: InstanceDetailForDescribeBackupsOutput
        """
        return self._instance_detail

    @instance_detail.setter
    def instance_detail(self, instance_detail):
        """Sets the instance_detail of this BackupForDescribeBackupsOutput.


        :param instance_detail: The instance_detail of this BackupForDescribeBackupsOutput.  # noqa: E501
        :type: InstanceDetailForDescribeBackupsOutput
        """

        self._instance_detail = instance_detail

    @property
    def instance_id(self):
        """Gets the instance_id of this BackupForDescribeBackupsOutput.  # noqa: E501


        :return: The instance_id of this BackupForDescribeBackupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this BackupForDescribeBackupsOutput.


        :param instance_id: The instance_id of this BackupForDescribeBackupsOutput.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def size(self):
        """Gets the size of this BackupForDescribeBackupsOutput.  # noqa: E501


        :return: The size of this BackupForDescribeBackupsOutput.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BackupForDescribeBackupsOutput.


        :param size: The size of this BackupForDescribeBackupsOutput.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def start_time(self):
        """Gets the start_time of this BackupForDescribeBackupsOutput.  # noqa: E501


        :return: The start_time of this BackupForDescribeBackupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this BackupForDescribeBackupsOutput.


        :param start_time: The start_time of this BackupForDescribeBackupsOutput.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this BackupForDescribeBackupsOutput.  # noqa: E501


        :return: The status of this BackupForDescribeBackupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BackupForDescribeBackupsOutput.


        :param status: The status of this BackupForDescribeBackupsOutput.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(BackupForDescribeBackupsOutput, dict):
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
        if not isinstance(other, BackupForDescribeBackupsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BackupForDescribeBackupsOutput):
            return True

        return self.to_dict() != other.to_dict()
