# coding: utf-8

"""
    spark

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DataListForlistApplicationHistoryOutput(object):
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
        'app_create_time': 'str',
        'app_finish_time': 'str',
        'app_start_time': 'str',
        'resource_meterage': 'ResourceMeterageForlistApplicationHistoryOutput',
        'retry_count': 'int',
        'state': 'str'
    }

    attribute_map = {
        'app_create_time': 'AppCreateTime',
        'app_finish_time': 'AppFinishTime',
        'app_start_time': 'AppStartTime',
        'resource_meterage': 'ResourceMeterage',
        'retry_count': 'RetryCount',
        'state': 'State'
    }

    def __init__(self, app_create_time=None, app_finish_time=None, app_start_time=None, resource_meterage=None, retry_count=None, state=None, _configuration=None):  # noqa: E501
        """DataListForlistApplicationHistoryOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._app_create_time = None
        self._app_finish_time = None
        self._app_start_time = None
        self._resource_meterage = None
        self._retry_count = None
        self._state = None
        self.discriminator = None

        if app_create_time is not None:
            self.app_create_time = app_create_time
        if app_finish_time is not None:
            self.app_finish_time = app_finish_time
        if app_start_time is not None:
            self.app_start_time = app_start_time
        if resource_meterage is not None:
            self.resource_meterage = resource_meterage
        if retry_count is not None:
            self.retry_count = retry_count
        if state is not None:
            self.state = state

    @property
    def app_create_time(self):
        """Gets the app_create_time of this DataListForlistApplicationHistoryOutput.  # noqa: E501


        :return: The app_create_time of this DataListForlistApplicationHistoryOutput.  # noqa: E501
        :rtype: str
        """
        return self._app_create_time

    @app_create_time.setter
    def app_create_time(self, app_create_time):
        """Sets the app_create_time of this DataListForlistApplicationHistoryOutput.


        :param app_create_time: The app_create_time of this DataListForlistApplicationHistoryOutput.  # noqa: E501
        :type: str
        """

        self._app_create_time = app_create_time

    @property
    def app_finish_time(self):
        """Gets the app_finish_time of this DataListForlistApplicationHistoryOutput.  # noqa: E501


        :return: The app_finish_time of this DataListForlistApplicationHistoryOutput.  # noqa: E501
        :rtype: str
        """
        return self._app_finish_time

    @app_finish_time.setter
    def app_finish_time(self, app_finish_time):
        """Sets the app_finish_time of this DataListForlistApplicationHistoryOutput.


        :param app_finish_time: The app_finish_time of this DataListForlistApplicationHistoryOutput.  # noqa: E501
        :type: str
        """

        self._app_finish_time = app_finish_time

    @property
    def app_start_time(self):
        """Gets the app_start_time of this DataListForlistApplicationHistoryOutput.  # noqa: E501


        :return: The app_start_time of this DataListForlistApplicationHistoryOutput.  # noqa: E501
        :rtype: str
        """
        return self._app_start_time

    @app_start_time.setter
    def app_start_time(self, app_start_time):
        """Sets the app_start_time of this DataListForlistApplicationHistoryOutput.


        :param app_start_time: The app_start_time of this DataListForlistApplicationHistoryOutput.  # noqa: E501
        :type: str
        """

        self._app_start_time = app_start_time

    @property
    def resource_meterage(self):
        """Gets the resource_meterage of this DataListForlistApplicationHistoryOutput.  # noqa: E501


        :return: The resource_meterage of this DataListForlistApplicationHistoryOutput.  # noqa: E501
        :rtype: ResourceMeterageForlistApplicationHistoryOutput
        """
        return self._resource_meterage

    @resource_meterage.setter
    def resource_meterage(self, resource_meterage):
        """Sets the resource_meterage of this DataListForlistApplicationHistoryOutput.


        :param resource_meterage: The resource_meterage of this DataListForlistApplicationHistoryOutput.  # noqa: E501
        :type: ResourceMeterageForlistApplicationHistoryOutput
        """

        self._resource_meterage = resource_meterage

    @property
    def retry_count(self):
        """Gets the retry_count of this DataListForlistApplicationHistoryOutput.  # noqa: E501


        :return: The retry_count of this DataListForlistApplicationHistoryOutput.  # noqa: E501
        :rtype: int
        """
        return self._retry_count

    @retry_count.setter
    def retry_count(self, retry_count):
        """Sets the retry_count of this DataListForlistApplicationHistoryOutput.


        :param retry_count: The retry_count of this DataListForlistApplicationHistoryOutput.  # noqa: E501
        :type: int
        """

        self._retry_count = retry_count

    @property
    def state(self):
        """Gets the state of this DataListForlistApplicationHistoryOutput.  # noqa: E501


        :return: The state of this DataListForlistApplicationHistoryOutput.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DataListForlistApplicationHistoryOutput.


        :param state: The state of this DataListForlistApplicationHistoryOutput.  # noqa: E501
        :type: str
        """

        self._state = state

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
        if issubclass(DataListForlistApplicationHistoryOutput, dict):
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
        if not isinstance(other, DataListForlistApplicationHistoryOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataListForlistApplicationHistoryOutput):
            return True

        return self.to_dict() != other.to_dict()
