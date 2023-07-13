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


class DescribeBandwidthPackagesRequest(object):
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
        'bandwidth_package_ids': 'list[str]',
        'bandwidth_package_name': 'str',
        'isp': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'project_name': 'str',
        'protocol': 'str',
        'security_protection_enabled': 'bool',
        'tag_filters': 'list[TagFilterForDescribeBandwidthPackagesInput]'
    }

    attribute_map = {
        'bandwidth_package_ids': 'BandwidthPackageIds',
        'bandwidth_package_name': 'BandwidthPackageName',
        'isp': 'ISP',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'project_name': 'ProjectName',
        'protocol': 'Protocol',
        'security_protection_enabled': 'SecurityProtectionEnabled',
        'tag_filters': 'TagFilters'
    }

    def __init__(self, bandwidth_package_ids=None, bandwidth_package_name=None, isp=None, page_number=None, page_size=None, project_name=None, protocol=None, security_protection_enabled=None, tag_filters=None, _configuration=None):  # noqa: E501
        """DescribeBandwidthPackagesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bandwidth_package_ids = None
        self._bandwidth_package_name = None
        self._isp = None
        self._page_number = None
        self._page_size = None
        self._project_name = None
        self._protocol = None
        self._security_protection_enabled = None
        self._tag_filters = None
        self.discriminator = None

        if bandwidth_package_ids is not None:
            self.bandwidth_package_ids = bandwidth_package_ids
        if bandwidth_package_name is not None:
            self.bandwidth_package_name = bandwidth_package_name
        if isp is not None:
            self.isp = isp
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if project_name is not None:
            self.project_name = project_name
        if protocol is not None:
            self.protocol = protocol
        if security_protection_enabled is not None:
            self.security_protection_enabled = security_protection_enabled
        if tag_filters is not None:
            self.tag_filters = tag_filters

    @property
    def bandwidth_package_ids(self):
        """Gets the bandwidth_package_ids of this DescribeBandwidthPackagesRequest.  # noqa: E501


        :return: The bandwidth_package_ids of this DescribeBandwidthPackagesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._bandwidth_package_ids

    @bandwidth_package_ids.setter
    def bandwidth_package_ids(self, bandwidth_package_ids):
        """Sets the bandwidth_package_ids of this DescribeBandwidthPackagesRequest.


        :param bandwidth_package_ids: The bandwidth_package_ids of this DescribeBandwidthPackagesRequest.  # noqa: E501
        :type: list[str]
        """

        self._bandwidth_package_ids = bandwidth_package_ids

    @property
    def bandwidth_package_name(self):
        """Gets the bandwidth_package_name of this DescribeBandwidthPackagesRequest.  # noqa: E501


        :return: The bandwidth_package_name of this DescribeBandwidthPackagesRequest.  # noqa: E501
        :rtype: str
        """
        return self._bandwidth_package_name

    @bandwidth_package_name.setter
    def bandwidth_package_name(self, bandwidth_package_name):
        """Sets the bandwidth_package_name of this DescribeBandwidthPackagesRequest.


        :param bandwidth_package_name: The bandwidth_package_name of this DescribeBandwidthPackagesRequest.  # noqa: E501
        :type: str
        """

        self._bandwidth_package_name = bandwidth_package_name

    @property
    def isp(self):
        """Gets the isp of this DescribeBandwidthPackagesRequest.  # noqa: E501


        :return: The isp of this DescribeBandwidthPackagesRequest.  # noqa: E501
        :rtype: str
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this DescribeBandwidthPackagesRequest.


        :param isp: The isp of this DescribeBandwidthPackagesRequest.  # noqa: E501
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
    def page_number(self):
        """Gets the page_number of this DescribeBandwidthPackagesRequest.  # noqa: E501


        :return: The page_number of this DescribeBandwidthPackagesRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeBandwidthPackagesRequest.


        :param page_number: The page_number of this DescribeBandwidthPackagesRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeBandwidthPackagesRequest.  # noqa: E501


        :return: The page_size of this DescribeBandwidthPackagesRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeBandwidthPackagesRequest.


        :param page_size: The page_size of this DescribeBandwidthPackagesRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                page_size is not None and page_size > 100):  # noqa: E501
            raise ValueError("Invalid value for `page_size`, must be a value less than or equal to `100`")  # noqa: E501

        self._page_size = page_size

    @property
    def project_name(self):
        """Gets the project_name of this DescribeBandwidthPackagesRequest.  # noqa: E501


        :return: The project_name of this DescribeBandwidthPackagesRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DescribeBandwidthPackagesRequest.


        :param project_name: The project_name of this DescribeBandwidthPackagesRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def protocol(self):
        """Gets the protocol of this DescribeBandwidthPackagesRequest.  # noqa: E501


        :return: The protocol of this DescribeBandwidthPackagesRequest.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this DescribeBandwidthPackagesRequest.


        :param protocol: The protocol of this DescribeBandwidthPackagesRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["IPv4", "IPv6"]  # noqa: E501
        if (self._configuration.client_side_validation and
                protocol not in allowed_values):
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(protocol, allowed_values)
            )

        self._protocol = protocol

    @property
    def security_protection_enabled(self):
        """Gets the security_protection_enabled of this DescribeBandwidthPackagesRequest.  # noqa: E501


        :return: The security_protection_enabled of this DescribeBandwidthPackagesRequest.  # noqa: E501
        :rtype: bool
        """
        return self._security_protection_enabled

    @security_protection_enabled.setter
    def security_protection_enabled(self, security_protection_enabled):
        """Sets the security_protection_enabled of this DescribeBandwidthPackagesRequest.


        :param security_protection_enabled: The security_protection_enabled of this DescribeBandwidthPackagesRequest.  # noqa: E501
        :type: bool
        """

        self._security_protection_enabled = security_protection_enabled

    @property
    def tag_filters(self):
        """Gets the tag_filters of this DescribeBandwidthPackagesRequest.  # noqa: E501


        :return: The tag_filters of this DescribeBandwidthPackagesRequest.  # noqa: E501
        :rtype: list[TagFilterForDescribeBandwidthPackagesInput]
        """
        return self._tag_filters

    @tag_filters.setter
    def tag_filters(self, tag_filters):
        """Sets the tag_filters of this DescribeBandwidthPackagesRequest.


        :param tag_filters: The tag_filters of this DescribeBandwidthPackagesRequest.  # noqa: E501
        :type: list[TagFilterForDescribeBandwidthPackagesInput]
        """

        self._tag_filters = tag_filters

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
        if issubclass(DescribeBandwidthPackagesRequest, dict):
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
        if not isinstance(other, DescribeBandwidthPackagesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeBandwidthPackagesRequest):
            return True

        return self.to_dict() != other.to_dict()
