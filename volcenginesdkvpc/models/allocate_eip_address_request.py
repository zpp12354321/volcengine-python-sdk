# coding: utf-8

"""
    vpc

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class AllocateEipAddressRequest(object):
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
        'bandwidth': 'int',
        'billing_type': 'int',
        'description': 'str',
        'isp': 'str',
        'name': 'str',
        'period': 'int',
        'period_unit': 'int',
        'security_protection_types': 'list[str]'
    }

    attribute_map = {
        'bandwidth': 'Bandwidth',
        'billing_type': 'BillingType',
        'description': 'Description',
        'isp': 'ISP',
        'name': 'Name',
        'period': 'Period',
        'period_unit': 'PeriodUnit',
        'security_protection_types': 'SecurityProtectionTypes'
    }

    def __init__(self, bandwidth=None, billing_type=None, description=None, isp=None, name=None, period=None, period_unit=None, security_protection_types=None, _configuration=None):  # noqa: E501
        """AllocateEipAddressRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bandwidth = None
        self._billing_type = None
        self._description = None
        self._isp = None
        self._name = None
        self._period = None
        self._period_unit = None
        self._security_protection_types = None
        self.discriminator = None

        if bandwidth is not None:
            self.bandwidth = bandwidth
        if billing_type is not None:
            self.billing_type = billing_type
        if description is not None:
            self.description = description
        if isp is not None:
            self.isp = isp
        if name is not None:
            self.name = name
        if period is not None:
            self.period = period
        if period_unit is not None:
            self.period_unit = period_unit
        if security_protection_types is not None:
            self.security_protection_types = security_protection_types

    @property
    def bandwidth(self):
        """Gets the bandwidth of this AllocateEipAddressRequest.  # noqa: E501


        :return: The bandwidth of this AllocateEipAddressRequest.  # noqa: E501
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this AllocateEipAddressRequest.


        :param bandwidth: The bandwidth of this AllocateEipAddressRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                bandwidth is not None and bandwidth > 500):  # noqa: E501
            raise ValueError("Invalid value for `bandwidth`, must be a value less than or equal to `500`")  # noqa: E501
        if (self._configuration.client_side_validation and
                bandwidth is not None and bandwidth < 1):  # noqa: E501
            raise ValueError("Invalid value for `bandwidth`, must be a value greater than or equal to `1`")  # noqa: E501

        self._bandwidth = bandwidth

    @property
    def billing_type(self):
        """Gets the billing_type of this AllocateEipAddressRequest.  # noqa: E501


        :return: The billing_type of this AllocateEipAddressRequest.  # noqa: E501
        :rtype: int
        """
        return self._billing_type

    @billing_type.setter
    def billing_type(self, billing_type):
        """Sets the billing_type of this AllocateEipAddressRequest.


        :param billing_type: The billing_type of this AllocateEipAddressRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                billing_type is not None and billing_type > 3):  # noqa: E501
            raise ValueError("Invalid value for `billing_type`, must be a value less than or equal to `3`")  # noqa: E501
        if (self._configuration.client_side_validation and
                billing_type is not None and billing_type < 1):  # noqa: E501
            raise ValueError("Invalid value for `billing_type`, must be a value greater than or equal to `1`")  # noqa: E501

        self._billing_type = billing_type

    @property
    def description(self):
        """Gets the description of this AllocateEipAddressRequest.  # noqa: E501


        :return: The description of this AllocateEipAddressRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AllocateEipAddressRequest.


        :param description: The description of this AllocateEipAddressRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                description is not None and len(description) > 255):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def isp(self):
        """Gets the isp of this AllocateEipAddressRequest.  # noqa: E501


        :return: The isp of this AllocateEipAddressRequest.  # noqa: E501
        :rtype: str
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this AllocateEipAddressRequest.


        :param isp: The isp of this AllocateEipAddressRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["BGP", "ChinaMobile", "ChinaUnicom", "ChinaTelecom"]  # noqa: E501
        if (self._configuration.client_side_validation and
                isp not in allowed_values):
            raise ValueError(
                "Invalid value for `isp` ({0}), must be one of {1}"  # noqa: E501
                .format(isp, allowed_values)
            )

        self._isp = isp

    @property
    def name(self):
        """Gets the name of this AllocateEipAddressRequest.  # noqa: E501


        :return: The name of this AllocateEipAddressRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AllocateEipAddressRequest.


        :param name: The name of this AllocateEipAddressRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 128):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `128`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def period(self):
        """Gets the period of this AllocateEipAddressRequest.  # noqa: E501


        :return: The period of this AllocateEipAddressRequest.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this AllocateEipAddressRequest.


        :param period: The period of this AllocateEipAddressRequest.  # noqa: E501
        :type: int
        """

        self._period = period

    @property
    def period_unit(self):
        """Gets the period_unit of this AllocateEipAddressRequest.  # noqa: E501


        :return: The period_unit of this AllocateEipAddressRequest.  # noqa: E501
        :rtype: int
        """
        return self._period_unit

    @period_unit.setter
    def period_unit(self, period_unit):
        """Sets the period_unit of this AllocateEipAddressRequest.


        :param period_unit: The period_unit of this AllocateEipAddressRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                period_unit is not None and period_unit > 2):  # noqa: E501
            raise ValueError("Invalid value for `period_unit`, must be a value less than or equal to `2`")  # noqa: E501
        if (self._configuration.client_side_validation and
                period_unit is not None and period_unit < 1):  # noqa: E501
            raise ValueError("Invalid value for `period_unit`, must be a value greater than or equal to `1`")  # noqa: E501

        self._period_unit = period_unit

    @property
    def security_protection_types(self):
        """Gets the security_protection_types of this AllocateEipAddressRequest.  # noqa: E501


        :return: The security_protection_types of this AllocateEipAddressRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._security_protection_types

    @security_protection_types.setter
    def security_protection_types(self, security_protection_types):
        """Sets the security_protection_types of this AllocateEipAddressRequest.


        :param security_protection_types: The security_protection_types of this AllocateEipAddressRequest.  # noqa: E501
        :type: list[str]
        """

        self._security_protection_types = security_protection_types

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
        if issubclass(AllocateEipAddressRequest, dict):
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
        if not isinstance(other, AllocateEipAddressRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AllocateEipAddressRequest):
            return True

        return self.to_dict() != other.to_dict()
