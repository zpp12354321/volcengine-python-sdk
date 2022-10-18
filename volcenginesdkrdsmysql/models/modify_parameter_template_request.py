# coding: utf-8

"""
    rds_mysql

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ModifyParameterTemplateRequest(object):
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
        'template_desc': 'str',
        'template_id': 'str',
        'template_name': 'str',
        'template_params': 'list[TemplateParamForModifyParameterTemplateInput]'
    }

    attribute_map = {
        'template_desc': 'TemplateDesc',
        'template_id': 'TemplateId',
        'template_name': 'TemplateName',
        'template_params': 'TemplateParams'
    }

    def __init__(self, template_desc=None, template_id=None, template_name=None, template_params=None, _configuration=None):  # noqa: E501
        """ModifyParameterTemplateRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._template_desc = None
        self._template_id = None
        self._template_name = None
        self._template_params = None
        self.discriminator = None

        if template_desc is not None:
            self.template_desc = template_desc
        self.template_id = template_id
        if template_name is not None:
            self.template_name = template_name
        if template_params is not None:
            self.template_params = template_params

    @property
    def template_desc(self):
        """Gets the template_desc of this ModifyParameterTemplateRequest.  # noqa: E501


        :return: The template_desc of this ModifyParameterTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._template_desc

    @template_desc.setter
    def template_desc(self, template_desc):
        """Sets the template_desc of this ModifyParameterTemplateRequest.


        :param template_desc: The template_desc of this ModifyParameterTemplateRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                template_desc is not None and len(template_desc) > 200):
            raise ValueError("Invalid value for `template_desc`, length must be less than or equal to `200`")  # noqa: E501

        self._template_desc = template_desc

    @property
    def template_id(self):
        """Gets the template_id of this ModifyParameterTemplateRequest.  # noqa: E501


        :return: The template_id of this ModifyParameterTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this ModifyParameterTemplateRequest.


        :param template_id: The template_id of this ModifyParameterTemplateRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and template_id is None:
            raise ValueError("Invalid value for `template_id`, must not be `None`")  # noqa: E501

        self._template_id = template_id

    @property
    def template_name(self):
        """Gets the template_name of this ModifyParameterTemplateRequest.  # noqa: E501


        :return: The template_name of this ModifyParameterTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this ModifyParameterTemplateRequest.


        :param template_name: The template_name of this ModifyParameterTemplateRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                template_name is not None and len(template_name) > 64):
            raise ValueError("Invalid value for `template_name`, length must be less than or equal to `64`")  # noqa: E501
        if (self._configuration.client_side_validation and
                template_name is not None and len(template_name) < 2):
            raise ValueError("Invalid value for `template_name`, length must be greater than or equal to `2`")  # noqa: E501

        self._template_name = template_name

    @property
    def template_params(self):
        """Gets the template_params of this ModifyParameterTemplateRequest.  # noqa: E501


        :return: The template_params of this ModifyParameterTemplateRequest.  # noqa: E501
        :rtype: list[TemplateParamForModifyParameterTemplateInput]
        """
        return self._template_params

    @template_params.setter
    def template_params(self, template_params):
        """Sets the template_params of this ModifyParameterTemplateRequest.


        :param template_params: The template_params of this ModifyParameterTemplateRequest.  # noqa: E501
        :type: list[TemplateParamForModifyParameterTemplateInput]
        """

        self._template_params = template_params

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
        if issubclass(ModifyParameterTemplateRequest, dict):
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
        if not isinstance(other, ModifyParameterTemplateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyParameterTemplateRequest):
            return True

        return self.to_dict() != other.to_dict()
