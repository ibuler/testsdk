# coding: utf-8

"""
    Jumpserver API Docs

    Jumpserver Restful api docs  # noqa: E501

    OpenAPI spec version: v1
    Contact: support@fit2cloud.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class NodeAssets(object):
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
        'assets': 'list[str]'
    }

    attribute_map = {
        'assets': 'assets'
    }

    def __init__(self, assets=None):  # noqa: E501
        """NodeAssets - a model defined in Swagger"""  # noqa: E501

        self._assets = None
        self.discriminator = None

        self.assets = assets

    @property
    def assets(self):
        """Gets the assets of this NodeAssets.  # noqa: E501


        :return: The assets of this NodeAssets.  # noqa: E501
        :rtype: list[str]
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this NodeAssets.


        :param assets: The assets of this NodeAssets.  # noqa: E501
        :type: list[str]
        """
        if assets is None:
            raise ValueError("Invalid value for `assets`, must not be `None`")  # noqa: E501

        self._assets = assets

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NodeAssets):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
