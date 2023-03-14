# coding: utf-8

"""
    cen

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CenSummaryRouteEntryForDescribeCenSummaryRouteEntriesOutput(object):
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
        'cen_id': 'str',
        'creation_time': 'str',
        'description': 'str',
        'destination_cidr_block': 'str',
        'status': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'cen_id': 'CenId',
        'creation_time': 'CreationTime',
        'description': 'Description',
        'destination_cidr_block': 'DestinationCidrBlock',
        'status': 'Status',
        'update_time': 'UpdateTime'
    }

    def __init__(self, cen_id=None, creation_time=None, description=None, destination_cidr_block=None, status=None, update_time=None, _configuration=None):  # noqa: E501
        """CenSummaryRouteEntryForDescribeCenSummaryRouteEntriesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cen_id = None
        self._creation_time = None
        self._description = None
        self._destination_cidr_block = None
        self._status = None
        self._update_time = None
        self.discriminator = None

        if cen_id is not None:
            self.cen_id = cen_id
        if creation_time is not None:
            self.creation_time = creation_time
        if description is not None:
            self.description = description
        if destination_cidr_block is not None:
            self.destination_cidr_block = destination_cidr_block
        if status is not None:
            self.status = status
        if update_time is not None:
            self.update_time = update_time

    @property
    def cen_id(self):
        """Gets the cen_id of this CenSummaryRouteEntryForDescribeCenSummaryRouteEntriesOutput.  # noqa: E501


        :return: The cen_id of this CenSummaryRouteEntryForDescribeCenSummaryRouteEntriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._cen_id

    @cen_id.setter
    def cen_id(self, cen_id):
        """Sets the cen_id of this CenSummaryRouteEntryForDescribeCenSummaryRouteEntriesOutput.


        :param cen_id: The cen_id of this CenSummaryRouteEntryForDescribeCenSummaryRouteEntriesOutput.  # noqa: E501
        :type: str
        """

        self._cen_id = cen_id

    @property
    def creation_time(self):
        """Gets the creation_time of this CenSummaryRouteEntryForDescribeCenSummaryRouteEntriesOutput.  # noqa: E501


        :return: The creation_time of this CenSummaryRouteEntryForDescribeCenSummaryRouteEntriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this CenSummaryRouteEntryForDescribeCenSummaryRouteEntriesOutput.


        :param creation_time: The creation_time of this CenSummaryRouteEntryForDescribeCenSummaryRouteEntriesOutput.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def description(self):
        """Gets the description of this CenSummaryRouteEntryForDescribeCenSummaryRouteEntriesOutput.  # noqa: E501


        :return: The description of this CenSummaryRouteEntryForDescribeCenSummaryRouteEntriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CenSummaryRouteEntryForDescribeCenSummaryRouteEntriesOutput.


        :param description: The description of this CenSummaryRouteEntryForDescribeCenSummaryRouteEntriesOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def destination_cidr_block(self):
        """Gets the destination_cidr_block of this CenSummaryRouteEntryForDescribeCenSummaryRouteEntriesOutput.  # noqa: E501


        :return: The destination_cidr_block of this CenSummaryRouteEntryForDescribeCenSummaryRouteEntriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._destination_cidr_block

    @destination_cidr_block.setter
    def destination_cidr_block(self, destination_cidr_block):
        """Sets the destination_cidr_block of this CenSummaryRouteEntryForDescribeCenSummaryRouteEntriesOutput.


        :param destination_cidr_block: The destination_cidr_block of this CenSummaryRouteEntryForDescribeCenSummaryRouteEntriesOutput.  # noqa: E501
        :type: str
        """

        self._destination_cidr_block = destination_cidr_block

    @property
    def status(self):
        """Gets the status of this CenSummaryRouteEntryForDescribeCenSummaryRouteEntriesOutput.  # noqa: E501


        :return: The status of this CenSummaryRouteEntryForDescribeCenSummaryRouteEntriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CenSummaryRouteEntryForDescribeCenSummaryRouteEntriesOutput.


        :param status: The status of this CenSummaryRouteEntryForDescribeCenSummaryRouteEntriesOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def update_time(self):
        """Gets the update_time of this CenSummaryRouteEntryForDescribeCenSummaryRouteEntriesOutput.  # noqa: E501


        :return: The update_time of this CenSummaryRouteEntryForDescribeCenSummaryRouteEntriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this CenSummaryRouteEntryForDescribeCenSummaryRouteEntriesOutput.


        :param update_time: The update_time of this CenSummaryRouteEntryForDescribeCenSummaryRouteEntriesOutput.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

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
        if issubclass(CenSummaryRouteEntryForDescribeCenSummaryRouteEntriesOutput, dict):
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
        if not isinstance(other, CenSummaryRouteEntryForDescribeCenSummaryRouteEntriesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CenSummaryRouteEntryForDescribeCenSummaryRouteEntriesOutput):
            return True

        return self.to_dict() != other.to_dict()
