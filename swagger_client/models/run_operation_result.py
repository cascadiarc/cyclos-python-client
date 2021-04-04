# coding: utf-8

"""
    Cyclos 4.11.5 API

    The REST API for Cyclos 4.11.5  # noqa: E501

    OpenAPI spec version: 4.11.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class RunOperationResult(object):
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
        'result_type': 'OperationResultTypeEnum',
        'title': 'str',
        'content': 'str',
        'notification': 'str',
        'notification_level': 'NotificationLevelEnum',
        'url': 'str',
        'back_to': 'EntityReference',
        'back_to_root': 'bool',
        're_run': 'bool',
        'auto_run_action_id': 'str',
        'columns': 'list[RunOperationResultColumn]',
        'rows': 'list[RunOperationResultRow]',
        'actions': 'list[RunOperationAction]'
    }

    attribute_map = {
        'result_type': 'resultType',
        'title': 'title',
        'content': 'content',
        'notification': 'notification',
        'notification_level': 'notificationLevel',
        'url': 'url',
        'back_to': 'backTo',
        'back_to_root': 'backToRoot',
        're_run': 'reRun',
        'auto_run_action_id': 'autoRunActionId',
        'columns': 'columns',
        'rows': 'rows',
        'actions': 'actions'
    }

    def __init__(self, result_type=None, title=None, content=None, notification=None, notification_level=None, url=None, back_to=None, back_to_root=None, re_run=None, auto_run_action_id=None, columns=None, rows=None, actions=None, _configuration=None):  # noqa: E501
        """RunOperationResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._result_type = None
        self._title = None
        self._content = None
        self._notification = None
        self._notification_level = None
        self._url = None
        self._back_to = None
        self._back_to_root = None
        self._re_run = None
        self._auto_run_action_id = None
        self._columns = None
        self._rows = None
        self._actions = None
        self.discriminator = None

        if result_type is not None:
            self.result_type = result_type
        if title is not None:
            self.title = title
        if content is not None:
            self.content = content
        if notification is not None:
            self.notification = notification
        if notification_level is not None:
            self.notification_level = notification_level
        if url is not None:
            self.url = url
        if back_to is not None:
            self.back_to = back_to
        if back_to_root is not None:
            self.back_to_root = back_to_root
        if re_run is not None:
            self.re_run = re_run
        if auto_run_action_id is not None:
            self.auto_run_action_id = auto_run_action_id
        if columns is not None:
            self.columns = columns
        if rows is not None:
            self.rows = rows
        if actions is not None:
            self.actions = actions

    @property
    def result_type(self):
        """Gets the result_type of this RunOperationResult.  # noqa: E501

        The kind of data a custom operation execution is expected to return Possible values are: * externalRedirect: The main execution returns an URL for another service. Then a second execution is expected when this other service redirects the client back to Cyclos * fileDownload: Returns a file, which can be downloaded * notification: Returns a text to be displayed as a simple notification * plainText: Returns a plain text to be displayed in a page, and optionally printed * resultPage: Returns a page or list of results, which should be displayed in a table like any other search / list * richText: Returns an HTML formatted text to be displayed in a page, and optionally printed * url: The result should be an URL to which the client should be redirected to   # noqa: E501

        :return: The result_type of this RunOperationResult.  # noqa: E501
        :rtype: OperationResultTypeEnum
        """
        return self._result_type

    @result_type.setter
    def result_type(self, result_type):
        """Sets the result_type of this RunOperationResult.

        The kind of data a custom operation execution is expected to return Possible values are: * externalRedirect: The main execution returns an URL for another service. Then a second execution is expected when this other service redirects the client back to Cyclos * fileDownload: Returns a file, which can be downloaded * notification: Returns a text to be displayed as a simple notification * plainText: Returns a plain text to be displayed in a page, and optionally printed * resultPage: Returns a page or list of results, which should be displayed in a table like any other search / list * richText: Returns an HTML formatted text to be displayed in a page, and optionally printed * url: The result should be an URL to which the client should be redirected to   # noqa: E501

        :param result_type: The result_type of this RunOperationResult.  # noqa: E501
        :type: OperationResultTypeEnum
        """

        self._result_type = result_type

    @property
    def title(self):
        """Gets the title of this RunOperationResult.  # noqa: E501

        The text title. May be returned only if `resultType` is either `plainText`, `richText` or `resultPage`.   # noqa: E501

        :return: The title of this RunOperationResult.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this RunOperationResult.

        The text title. May be returned only if `resultType` is either `plainText`, `richText` or `resultPage`.   # noqa: E501

        :param title: The title of this RunOperationResult.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def content(self):
        """Gets the content of this RunOperationResult.  # noqa: E501

        The execution result content. Only returned if `resultType` is either `plainText` or  `richText`.   # noqa: E501

        :return: The content of this RunOperationResult.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this RunOperationResult.

        The execution result content. Only returned if `resultType` is either `plainText` or  `richText`.   # noqa: E501

        :param content: The content of this RunOperationResult.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def notification(self):
        """Gets the notification of this RunOperationResult.  # noqa: E501

        The execution result as string that should be shown as a notification. Only returned if `resultType` is `notification`.   # noqa: E501

        :return: The notification of this RunOperationResult.  # noqa: E501
        :rtype: str
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """Sets the notification of this RunOperationResult.

        The execution result as string that should be shown as a notification. Only returned if `resultType` is `notification`.   # noqa: E501

        :param notification: The notification of this RunOperationResult.  # noqa: E501
        :type: str
        """

        self._notification = notification

    @property
    def notification_level(self):
        """Gets the notification_level of this RunOperationResult.  # noqa: E501

        Only returned if `resultType` is `notification`. Possible values are: * error: An error message, when some operation went wrong   * information: A general informative message * warning: A warning message, when special caution is required   # noqa: E501

        :return: The notification_level of this RunOperationResult.  # noqa: E501
        :rtype: NotificationLevelEnum
        """
        return self._notification_level

    @notification_level.setter
    def notification_level(self, notification_level):
        """Sets the notification_level of this RunOperationResult.

        Only returned if `resultType` is `notification`. Possible values are: * error: An error message, when some operation went wrong   * information: A general informative message * warning: A warning message, when special caution is required   # noqa: E501

        :param notification_level: The notification_level of this RunOperationResult.  # noqa: E501
        :type: NotificationLevelEnum
        """

        self._notification_level = notification_level

    @property
    def url(self):
        """Gets the url of this RunOperationResult.  # noqa: E501

        The execution result as an URL, to which the client should be redirected. Only returned if `resultType` is either `externalRedirect` or `url`.   # noqa: E501

        :return: The url of this RunOperationResult.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this RunOperationResult.

        The execution result as an URL, to which the client should be redirected. Only returned if `resultType` is either `externalRedirect` or `url`.   # noqa: E501

        :param url: The url of this RunOperationResult.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def back_to(self):
        """Gets the back_to of this RunOperationResult.  # noqa: E501

        Either the id or internal name of the custom operation to go back after run the operation.   # noqa: E501

        :return: The back_to of this RunOperationResult.  # noqa: E501
        :rtype: EntityReference
        """
        return self._back_to

    @back_to.setter
    def back_to(self, back_to):
        """Sets the back_to of this RunOperationResult.

        Either the id or internal name of the custom operation to go back after run the operation.   # noqa: E501

        :param back_to: The back_to of this RunOperationResult.  # noqa: E501
        :type: EntityReference
        """

        self._back_to = back_to

    @property
    def back_to_root(self):
        """Gets the back_to_root of this RunOperationResult.  # noqa: E501

        A boolean value indicating if the client application must go back to the page that originated the custom  operation executions.        # noqa: E501

        :return: The back_to_root of this RunOperationResult.  # noqa: E501
        :rtype: bool
        """
        return self._back_to_root

    @back_to_root.setter
    def back_to_root(self, back_to_root):
        """Sets the back_to_root of this RunOperationResult.

        A boolean value indicating if the client application must go back to the page that originated the custom  operation executions.        # noqa: E501

        :param back_to_root: The back_to_root of this RunOperationResult.  # noqa: E501
        :type: bool
        """

        self._back_to_root = back_to_root

    @property
    def re_run(self):
        """Gets the re_run of this RunOperationResult.  # noqa: E501

        A boolean value indicating if the custom operation we went back to or the current action container operation must be re-run before display it.   # noqa: E501

        :return: The re_run of this RunOperationResult.  # noqa: E501
        :rtype: bool
        """
        return self._re_run

    @re_run.setter
    def re_run(self, re_run):
        """Sets the re_run of this RunOperationResult.

        A boolean value indicating if the custom operation we went back to or the current action container operation must be re-run before display it.   # noqa: E501

        :param re_run: The re_run of this RunOperationResult.  # noqa: E501
        :type: bool
        """

        self._re_run = re_run

    @property
    def auto_run_action_id(self):
        """Gets the auto_run_action_id of this RunOperationResult.  # noqa: E501

        If it is present, it indicates the id of the action that should be executed automatically.   # noqa: E501

        :return: The auto_run_action_id of this RunOperationResult.  # noqa: E501
        :rtype: str
        """
        return self._auto_run_action_id

    @auto_run_action_id.setter
    def auto_run_action_id(self, auto_run_action_id):
        """Sets the auto_run_action_id of this RunOperationResult.

        If it is present, it indicates the id of the action that should be executed automatically.   # noqa: E501

        :param auto_run_action_id: The auto_run_action_id of this RunOperationResult.  # noqa: E501
        :type: str
        """

        self._auto_run_action_id = auto_run_action_id

    @property
    def columns(self):
        """Gets the columns of this RunOperationResult.  # noqa: E501

        Contains the definitions for each column in the result. Only returned if `resultType` is `resultPage`.    # noqa: E501

        :return: The columns of this RunOperationResult.  # noqa: E501
        :rtype: list[RunOperationResultColumn]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this RunOperationResult.

        Contains the definitions for each column in the result. Only returned if `resultType` is `resultPage`.    # noqa: E501

        :param columns: The columns of this RunOperationResult.  # noqa: E501
        :type: list[RunOperationResultColumn]
        """

        self._columns = columns

    @property
    def rows(self):
        """Gets the rows of this RunOperationResult.  # noqa: E501

        Each row is an object containing the cells for that row, keyed by each column's `property`. Only returned if `resultType` is `resultPage`.   # noqa: E501

        :return: The rows of this RunOperationResult.  # noqa: E501
        :rtype: list[RunOperationResultRow]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this RunOperationResult.

        Each row is an object containing the cells for that row, keyed by each column's `property`. Only returned if `resultType` is `resultPage`.   # noqa: E501

        :param rows: The rows of this RunOperationResult.  # noqa: E501
        :type: list[RunOperationResultRow]
        """

        self._rows = rows

    @property
    def actions(self):
        """Gets the actions of this RunOperationResult.  # noqa: E501

        Actions are other internal custom operations that can be executed from this custom operation. The returned parameters should be passed to the server when running this action.   # noqa: E501

        :return: The actions of this RunOperationResult.  # noqa: E501
        :rtype: list[RunOperationAction]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this RunOperationResult.

        Actions are other internal custom operations that can be executed from this custom operation. The returned parameters should be passed to the server when running this action.   # noqa: E501

        :param actions: The actions of this RunOperationResult.  # noqa: E501
        :type: list[RunOperationAction]
        """

        self._actions = actions

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
        if issubclass(RunOperationResult, dict):
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
        if not isinstance(other, RunOperationResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RunOperationResult):
            return True

        return self.to_dict() != other.to_dict()
