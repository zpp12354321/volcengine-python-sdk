# coding: utf-8

"""
    natgateway

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class SnatEntryForDescribeSnatEntriesOutput(object):
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
        'eip_address': 'str',
        'eip_id': 'str',
        'nat_gateway_id': 'str',
        'snat_entry_id': 'str',
        'snat_entry_name': 'str',
        'status': 'str',
        'subnet_id': 'str'
    }

    attribute_map = {
        'eip_address': 'EipAddress',
        'eip_id': 'EipId',
        'nat_gateway_id': 'NatGatewayId',
        'snat_entry_id': 'SnatEntryId',
        'snat_entry_name': 'SnatEntryName',
        'status': 'Status',
        'subnet_id': 'SubnetId'
    }

    def __init__(self, eip_address=None, eip_id=None, nat_gateway_id=None, snat_entry_id=None, snat_entry_name=None, status=None, subnet_id=None, _configuration=None):  # noqa: E501
        """SnatEntryForDescribeSnatEntriesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._eip_address = None
        self._eip_id = None
        self._nat_gateway_id = None
        self._snat_entry_id = None
        self._snat_entry_name = None
        self._status = None
        self._subnet_id = None
        self.discriminator = None

        if eip_address is not None:
            self.eip_address = eip_address
        if eip_id is not None:
            self.eip_id = eip_id
        if nat_gateway_id is not None:
            self.nat_gateway_id = nat_gateway_id
        if snat_entry_id is not None:
            self.snat_entry_id = snat_entry_id
        if snat_entry_name is not None:
            self.snat_entry_name = snat_entry_name
        if status is not None:
            self.status = status
        if subnet_id is not None:
            self.subnet_id = subnet_id

    @property
    def eip_address(self):
        """Gets the eip_address of this SnatEntryForDescribeSnatEntriesOutput.  # noqa: E501


        :return: The eip_address of this SnatEntryForDescribeSnatEntriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._eip_address

    @eip_address.setter
    def eip_address(self, eip_address):
        """Sets the eip_address of this SnatEntryForDescribeSnatEntriesOutput.


        :param eip_address: The eip_address of this SnatEntryForDescribeSnatEntriesOutput.  # noqa: E501
        :type: str
        """

        self._eip_address = eip_address

    @property
    def eip_id(self):
        """Gets the eip_id of this SnatEntryForDescribeSnatEntriesOutput.  # noqa: E501


        :return: The eip_id of this SnatEntryForDescribeSnatEntriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._eip_id

    @eip_id.setter
    def eip_id(self, eip_id):
        """Sets the eip_id of this SnatEntryForDescribeSnatEntriesOutput.


        :param eip_id: The eip_id of this SnatEntryForDescribeSnatEntriesOutput.  # noqa: E501
        :type: str
        """

        self._eip_id = eip_id

    @property
    def nat_gateway_id(self):
        """Gets the nat_gateway_id of this SnatEntryForDescribeSnatEntriesOutput.  # noqa: E501


        :return: The nat_gateway_id of this SnatEntryForDescribeSnatEntriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._nat_gateway_id

    @nat_gateway_id.setter
    def nat_gateway_id(self, nat_gateway_id):
        """Sets the nat_gateway_id of this SnatEntryForDescribeSnatEntriesOutput.


        :param nat_gateway_id: The nat_gateway_id of this SnatEntryForDescribeSnatEntriesOutput.  # noqa: E501
        :type: str
        """

        self._nat_gateway_id = nat_gateway_id

    @property
    def snat_entry_id(self):
        """Gets the snat_entry_id of this SnatEntryForDescribeSnatEntriesOutput.  # noqa: E501


        :return: The snat_entry_id of this SnatEntryForDescribeSnatEntriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._snat_entry_id

    @snat_entry_id.setter
    def snat_entry_id(self, snat_entry_id):
        """Sets the snat_entry_id of this SnatEntryForDescribeSnatEntriesOutput.


        :param snat_entry_id: The snat_entry_id of this SnatEntryForDescribeSnatEntriesOutput.  # noqa: E501
        :type: str
        """

        self._snat_entry_id = snat_entry_id

    @property
    def snat_entry_name(self):
        """Gets the snat_entry_name of this SnatEntryForDescribeSnatEntriesOutput.  # noqa: E501


        :return: The snat_entry_name of this SnatEntryForDescribeSnatEntriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._snat_entry_name

    @snat_entry_name.setter
    def snat_entry_name(self, snat_entry_name):
        """Sets the snat_entry_name of this SnatEntryForDescribeSnatEntriesOutput.


        :param snat_entry_name: The snat_entry_name of this SnatEntryForDescribeSnatEntriesOutput.  # noqa: E501
        :type: str
        """

        self._snat_entry_name = snat_entry_name

    @property
    def status(self):
        """Gets the status of this SnatEntryForDescribeSnatEntriesOutput.  # noqa: E501


        :return: The status of this SnatEntryForDescribeSnatEntriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SnatEntryForDescribeSnatEntriesOutput.


        :param status: The status of this SnatEntryForDescribeSnatEntriesOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def subnet_id(self):
        """Gets the subnet_id of this SnatEntryForDescribeSnatEntriesOutput.  # noqa: E501


        :return: The subnet_id of this SnatEntryForDescribeSnatEntriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this SnatEntryForDescribeSnatEntriesOutput.


        :param subnet_id: The subnet_id of this SnatEntryForDescribeSnatEntriesOutput.  # noqa: E501
        :type: str
        """

        self._subnet_id = subnet_id

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
        if issubclass(SnatEntryForDescribeSnatEntriesOutput, dict):
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
        if not isinstance(other, SnatEntryForDescribeSnatEntriesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SnatEntryForDescribeSnatEntriesOutput):
            return True

        return self.to_dict() != other.to_dict()
