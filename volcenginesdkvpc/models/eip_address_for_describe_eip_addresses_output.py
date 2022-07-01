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


class EipAddressForDescribeEipAddressesOutput(object):
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
        'allocation_id': 'str',
        'allocation_time': 'str',
        'bandwidth': 'int',
        'bandwidth_package_id': 'str',
        'billing_type': 'int',
        'business_status': 'str',
        'deleted_time': 'str',
        'description': 'str',
        'eip_address': 'str',
        'expired_time': 'str',
        'isp': 'str',
        'instance_id': 'str',
        'instance_type': 'str',
        'lock_reason': 'str',
        'name': 'str',
        'overdue_time': 'str',
        'security_protection_types': 'list[str]',
        'status': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'allocation_id': 'AllocationId',
        'allocation_time': 'AllocationTime',
        'bandwidth': 'Bandwidth',
        'bandwidth_package_id': 'BandwidthPackageId',
        'billing_type': 'BillingType',
        'business_status': 'BusinessStatus',
        'deleted_time': 'DeletedTime',
        'description': 'Description',
        'eip_address': 'EipAddress',
        'expired_time': 'ExpiredTime',
        'isp': 'ISP',
        'instance_id': 'InstanceId',
        'instance_type': 'InstanceType',
        'lock_reason': 'LockReason',
        'name': 'Name',
        'overdue_time': 'OverdueTime',
        'security_protection_types': 'SecurityProtectionTypes',
        'status': 'Status',
        'updated_at': 'UpdatedAt'
    }

    def __init__(self, allocation_id=None, allocation_time=None, bandwidth=None, bandwidth_package_id=None, billing_type=None, business_status=None, deleted_time=None, description=None, eip_address=None, expired_time=None, isp=None, instance_id=None, instance_type=None, lock_reason=None, name=None, overdue_time=None, security_protection_types=None, status=None, updated_at=None, _configuration=None):  # noqa: E501
        """EipAddressForDescribeEipAddressesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allocation_id = None
        self._allocation_time = None
        self._bandwidth = None
        self._bandwidth_package_id = None
        self._billing_type = None
        self._business_status = None
        self._deleted_time = None
        self._description = None
        self._eip_address = None
        self._expired_time = None
        self._isp = None
        self._instance_id = None
        self._instance_type = None
        self._lock_reason = None
        self._name = None
        self._overdue_time = None
        self._security_protection_types = None
        self._status = None
        self._updated_at = None
        self.discriminator = None

        if allocation_id is not None:
            self.allocation_id = allocation_id
        if allocation_time is not None:
            self.allocation_time = allocation_time
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if bandwidth_package_id is not None:
            self.bandwidth_package_id = bandwidth_package_id
        if billing_type is not None:
            self.billing_type = billing_type
        if business_status is not None:
            self.business_status = business_status
        if deleted_time is not None:
            self.deleted_time = deleted_time
        if description is not None:
            self.description = description
        if eip_address is not None:
            self.eip_address = eip_address
        if expired_time is not None:
            self.expired_time = expired_time
        if isp is not None:
            self.isp = isp
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_type is not None:
            self.instance_type = instance_type
        if lock_reason is not None:
            self.lock_reason = lock_reason
        if name is not None:
            self.name = name
        if overdue_time is not None:
            self.overdue_time = overdue_time
        if security_protection_types is not None:
            self.security_protection_types = security_protection_types
        if status is not None:
            self.status = status
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def allocation_id(self):
        """Gets the allocation_id of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501


        :return: The allocation_id of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :rtype: str
        """
        return self._allocation_id

    @allocation_id.setter
    def allocation_id(self, allocation_id):
        """Sets the allocation_id of this EipAddressForDescribeEipAddressesOutput.


        :param allocation_id: The allocation_id of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :type: str
        """

        self._allocation_id = allocation_id

    @property
    def allocation_time(self):
        """Gets the allocation_time of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501


        :return: The allocation_time of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :rtype: str
        """
        return self._allocation_time

    @allocation_time.setter
    def allocation_time(self, allocation_time):
        """Sets the allocation_time of this EipAddressForDescribeEipAddressesOutput.


        :param allocation_time: The allocation_time of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :type: str
        """

        self._allocation_time = allocation_time

    @property
    def bandwidth(self):
        """Gets the bandwidth of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501


        :return: The bandwidth of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this EipAddressForDescribeEipAddressesOutput.


        :param bandwidth: The bandwidth of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :type: int
        """

        self._bandwidth = bandwidth

    @property
    def bandwidth_package_id(self):
        """Gets the bandwidth_package_id of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501


        :return: The bandwidth_package_id of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :rtype: str
        """
        return self._bandwidth_package_id

    @bandwidth_package_id.setter
    def bandwidth_package_id(self, bandwidth_package_id):
        """Sets the bandwidth_package_id of this EipAddressForDescribeEipAddressesOutput.


        :param bandwidth_package_id: The bandwidth_package_id of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :type: str
        """

        self._bandwidth_package_id = bandwidth_package_id

    @property
    def billing_type(self):
        """Gets the billing_type of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501


        :return: The billing_type of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :rtype: int
        """
        return self._billing_type

    @billing_type.setter
    def billing_type(self, billing_type):
        """Sets the billing_type of this EipAddressForDescribeEipAddressesOutput.


        :param billing_type: The billing_type of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :type: int
        """

        self._billing_type = billing_type

    @property
    def business_status(self):
        """Gets the business_status of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501


        :return: The business_status of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :rtype: str
        """
        return self._business_status

    @business_status.setter
    def business_status(self, business_status):
        """Sets the business_status of this EipAddressForDescribeEipAddressesOutput.


        :param business_status: The business_status of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :type: str
        """

        self._business_status = business_status

    @property
    def deleted_time(self):
        """Gets the deleted_time of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501


        :return: The deleted_time of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :rtype: str
        """
        return self._deleted_time

    @deleted_time.setter
    def deleted_time(self, deleted_time):
        """Sets the deleted_time of this EipAddressForDescribeEipAddressesOutput.


        :param deleted_time: The deleted_time of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :type: str
        """

        self._deleted_time = deleted_time

    @property
    def description(self):
        """Gets the description of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501


        :return: The description of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EipAddressForDescribeEipAddressesOutput.


        :param description: The description of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def eip_address(self):
        """Gets the eip_address of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501


        :return: The eip_address of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :rtype: str
        """
        return self._eip_address

    @eip_address.setter
    def eip_address(self, eip_address):
        """Sets the eip_address of this EipAddressForDescribeEipAddressesOutput.


        :param eip_address: The eip_address of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :type: str
        """

        self._eip_address = eip_address

    @property
    def expired_time(self):
        """Gets the expired_time of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501


        :return: The expired_time of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :rtype: str
        """
        return self._expired_time

    @expired_time.setter
    def expired_time(self, expired_time):
        """Sets the expired_time of this EipAddressForDescribeEipAddressesOutput.


        :param expired_time: The expired_time of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :type: str
        """

        self._expired_time = expired_time

    @property
    def isp(self):
        """Gets the isp of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501


        :return: The isp of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :rtype: str
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this EipAddressForDescribeEipAddressesOutput.


        :param isp: The isp of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :type: str
        """

        self._isp = isp

    @property
    def instance_id(self):
        """Gets the instance_id of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501


        :return: The instance_id of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this EipAddressForDescribeEipAddressesOutput.


        :param instance_id: The instance_id of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def instance_type(self):
        """Gets the instance_type of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501


        :return: The instance_type of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this EipAddressForDescribeEipAddressesOutput.


        :param instance_type: The instance_type of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :type: str
        """

        self._instance_type = instance_type

    @property
    def lock_reason(self):
        """Gets the lock_reason of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501


        :return: The lock_reason of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :rtype: str
        """
        return self._lock_reason

    @lock_reason.setter
    def lock_reason(self, lock_reason):
        """Sets the lock_reason of this EipAddressForDescribeEipAddressesOutput.


        :param lock_reason: The lock_reason of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :type: str
        """

        self._lock_reason = lock_reason

    @property
    def name(self):
        """Gets the name of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501


        :return: The name of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EipAddressForDescribeEipAddressesOutput.


        :param name: The name of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def overdue_time(self):
        """Gets the overdue_time of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501


        :return: The overdue_time of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :rtype: str
        """
        return self._overdue_time

    @overdue_time.setter
    def overdue_time(self, overdue_time):
        """Sets the overdue_time of this EipAddressForDescribeEipAddressesOutput.


        :param overdue_time: The overdue_time of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :type: str
        """

        self._overdue_time = overdue_time

    @property
    def security_protection_types(self):
        """Gets the security_protection_types of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501


        :return: The security_protection_types of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._security_protection_types

    @security_protection_types.setter
    def security_protection_types(self, security_protection_types):
        """Sets the security_protection_types of this EipAddressForDescribeEipAddressesOutput.


        :param security_protection_types: The security_protection_types of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :type: list[str]
        """

        self._security_protection_types = security_protection_types

    @property
    def status(self):
        """Gets the status of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501


        :return: The status of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EipAddressForDescribeEipAddressesOutput.


        :param status: The status of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def updated_at(self):
        """Gets the updated_at of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501


        :return: The updated_at of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this EipAddressForDescribeEipAddressesOutput.


        :param updated_at: The updated_at of this EipAddressForDescribeEipAddressesOutput.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

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
        if issubclass(EipAddressForDescribeEipAddressesOutput, dict):
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
        if not isinstance(other, EipAddressForDescribeEipAddressesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EipAddressForDescribeEipAddressesOutput):
            return True

        return self.to_dict() != other.to_dict()
