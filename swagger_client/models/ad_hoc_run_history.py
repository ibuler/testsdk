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


class AdHocRunHistory(object):
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
        'id': 'str',
        'task': 'str',
        'adhoc_short_id': 'str',
        'stat': 'str',
        'date_start': 'datetime',
        'date_finished': 'datetime',
        'timedelta': 'float',
        'is_finished': 'bool',
        'is_success': 'bool',
        'adhoc': 'str',
        'summary': 'str',
        'short_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'task': 'task',
        'adhoc_short_id': 'adhoc_short_id',
        'stat': 'stat',
        'date_start': 'date_start',
        'date_finished': 'date_finished',
        'timedelta': 'timedelta',
        'is_finished': 'is_finished',
        'is_success': 'is_success',
        'adhoc': 'adhoc',
        'summary': 'summary',
        'short_id': 'short_id'
    }

    def __init__(self, id=None, task=None, adhoc_short_id=None, stat=None, date_start=None, date_finished=None, timedelta=None, is_finished=None, is_success=None, adhoc=None, summary=None, short_id=None):  # noqa: E501
        """AdHocRunHistory - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._task = None
        self._adhoc_short_id = None
        self._stat = None
        self._date_start = None
        self._date_finished = None
        self._timedelta = None
        self._is_finished = None
        self._is_success = None
        self._adhoc = None
        self._summary = None
        self._short_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if task is not None:
            self.task = task
        if adhoc_short_id is not None:
            self.adhoc_short_id = adhoc_short_id
        if stat is not None:
            self.stat = stat
        if date_start is not None:
            self.date_start = date_start
        if date_finished is not None:
            self.date_finished = date_finished
        if timedelta is not None:
            self.timedelta = timedelta
        if is_finished is not None:
            self.is_finished = is_finished
        if is_success is not None:
            self.is_success = is_success
        if adhoc is not None:
            self.adhoc = adhoc
        if summary is not None:
            self.summary = summary
        if short_id is not None:
            self.short_id = short_id

    @property
    def id(self):
        """Gets the id of this AdHocRunHistory.  # noqa: E501


        :return: The id of this AdHocRunHistory.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AdHocRunHistory.


        :param id: The id of this AdHocRunHistory.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def task(self):
        """Gets the task of this AdHocRunHistory.  # noqa: E501


        :return: The task of this AdHocRunHistory.  # noqa: E501
        :rtype: str
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this AdHocRunHistory.


        :param task: The task of this AdHocRunHistory.  # noqa: E501
        :type: str
        """

        self._task = task

    @property
    def adhoc_short_id(self):
        """Gets the adhoc_short_id of this AdHocRunHistory.  # noqa: E501


        :return: The adhoc_short_id of this AdHocRunHistory.  # noqa: E501
        :rtype: str
        """
        return self._adhoc_short_id

    @adhoc_short_id.setter
    def adhoc_short_id(self, adhoc_short_id):
        """Sets the adhoc_short_id of this AdHocRunHistory.


        :param adhoc_short_id: The adhoc_short_id of this AdHocRunHistory.  # noqa: E501
        :type: str
        """

        self._adhoc_short_id = adhoc_short_id

    @property
    def stat(self):
        """Gets the stat of this AdHocRunHistory.  # noqa: E501


        :return: The stat of this AdHocRunHistory.  # noqa: E501
        :rtype: str
        """
        return self._stat

    @stat.setter
    def stat(self, stat):
        """Sets the stat of this AdHocRunHistory.


        :param stat: The stat of this AdHocRunHistory.  # noqa: E501
        :type: str
        """

        self._stat = stat

    @property
    def date_start(self):
        """Gets the date_start of this AdHocRunHistory.  # noqa: E501


        :return: The date_start of this AdHocRunHistory.  # noqa: E501
        :rtype: datetime
        """
        return self._date_start

    @date_start.setter
    def date_start(self, date_start):
        """Sets the date_start of this AdHocRunHistory.


        :param date_start: The date_start of this AdHocRunHistory.  # noqa: E501
        :type: datetime
        """

        self._date_start = date_start

    @property
    def date_finished(self):
        """Gets the date_finished of this AdHocRunHistory.  # noqa: E501


        :return: The date_finished of this AdHocRunHistory.  # noqa: E501
        :rtype: datetime
        """
        return self._date_finished

    @date_finished.setter
    def date_finished(self, date_finished):
        """Sets the date_finished of this AdHocRunHistory.


        :param date_finished: The date_finished of this AdHocRunHistory.  # noqa: E501
        :type: datetime
        """

        self._date_finished = date_finished

    @property
    def timedelta(self):
        """Gets the timedelta of this AdHocRunHistory.  # noqa: E501


        :return: The timedelta of this AdHocRunHistory.  # noqa: E501
        :rtype: float
        """
        return self._timedelta

    @timedelta.setter
    def timedelta(self, timedelta):
        """Sets the timedelta of this AdHocRunHistory.


        :param timedelta: The timedelta of this AdHocRunHistory.  # noqa: E501
        :type: float
        """

        self._timedelta = timedelta

    @property
    def is_finished(self):
        """Gets the is_finished of this AdHocRunHistory.  # noqa: E501


        :return: The is_finished of this AdHocRunHistory.  # noqa: E501
        :rtype: bool
        """
        return self._is_finished

    @is_finished.setter
    def is_finished(self, is_finished):
        """Sets the is_finished of this AdHocRunHistory.


        :param is_finished: The is_finished of this AdHocRunHistory.  # noqa: E501
        :type: bool
        """

        self._is_finished = is_finished

    @property
    def is_success(self):
        """Gets the is_success of this AdHocRunHistory.  # noqa: E501


        :return: The is_success of this AdHocRunHistory.  # noqa: E501
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this AdHocRunHistory.


        :param is_success: The is_success of this AdHocRunHistory.  # noqa: E501
        :type: bool
        """

        self._is_success = is_success

    @property
    def adhoc(self):
        """Gets the adhoc of this AdHocRunHistory.  # noqa: E501


        :return: The adhoc of this AdHocRunHistory.  # noqa: E501
        :rtype: str
        """
        return self._adhoc

    @adhoc.setter
    def adhoc(self, adhoc):
        """Sets the adhoc of this AdHocRunHistory.


        :param adhoc: The adhoc of this AdHocRunHistory.  # noqa: E501
        :type: str
        """

        self._adhoc = adhoc

    @property
    def summary(self):
        """Gets the summary of this AdHocRunHistory.  # noqa: E501


        :return: The summary of this AdHocRunHistory.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this AdHocRunHistory.


        :param summary: The summary of this AdHocRunHistory.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def short_id(self):
        """Gets the short_id of this AdHocRunHistory.  # noqa: E501


        :return: The short_id of this AdHocRunHistory.  # noqa: E501
        :rtype: str
        """
        return self._short_id

    @short_id.setter
    def short_id(self, short_id):
        """Sets the short_id of this AdHocRunHistory.


        :param short_id: The short_id of this AdHocRunHistory.  # noqa: E501
        :type: str
        """

        self._short_id = short_id

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
        if not isinstance(other, AdHocRunHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
