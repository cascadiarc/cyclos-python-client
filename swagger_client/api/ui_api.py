# coding: utf-8

"""
    Cyclos 4.11.5 API

    The REST API for Cyclos 4.11.5  # noqa: E501

    OpenAPI spec version: 4.11.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class UIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def data_for_ui(self, **kwargs):  # noqa: E501
        """Returns useful data required to properly display a user interface  # noqa: E501

        The returned data contains settings and also content like header, footer  and theme.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_for_ui(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] fields: Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).  
        :param str kind: Specifies the kind of user interface to get data for. If null then no  data related to the UI will be returned. Possible values are: * custom: A custom front-end application. Has no headers, footers or theme * main: The main web user interface * mobile: The mobile application user interface * pay: The Ticket / Easy invoice confirmation application user interface 
        :param str cyclos_version: The last known Cyclos version. Sometimes, data to be cached depends on the version of the Cyclos application, and this helps controlling such cases 
        :param str header_if: Controls the header cache. If is a boolean value (`true` or `false`) will forcibly return or skip the content. Otherwise, it should be a string in the form `id|version`. In this case, the content will be returned only when changed. When blank will always return it. 
        :param str footer_if: Controls the footer cache. If is a boolean value (`true` or `false`) will forcibly return or skip the content. Otherwise, it should be a string in the form `id|version`. In this case, the content will be returned only when changed. When blank will always return it. 
        :param str theme_if: Controls the theme cache. If is a boolean value (`true` or `false`) will forcibly return or skip the content. Otherwise, it should be a string in the form `id|version`. In this case, the content will be returned only when changed. When blank will always return it. 
        :param bool theme_by_components: Flag used to indicate how the theme must be returned (if returned): true means the theme components (base / advanced definitions and custom style) will be filled. Otherwise the final CSS (i. e the theme content). Only valid if the kind of the user interface is NOT `mobile`. For that kind the theme es always returned by its components. 
        :return: DataForUi
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.data_for_ui_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.data_for_ui_with_http_info(**kwargs)  # noqa: E501
            return data

    def data_for_ui_with_http_info(self, **kwargs):  # noqa: E501
        """Returns useful data required to properly display a user interface  # noqa: E501

        The returned data contains settings and also content like header, footer  and theme.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_for_ui_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] fields: Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).  
        :param str kind: Specifies the kind of user interface to get data for. If null then no  data related to the UI will be returned. Possible values are: * custom: A custom front-end application. Has no headers, footers or theme * main: The main web user interface * mobile: The mobile application user interface * pay: The Ticket / Easy invoice confirmation application user interface 
        :param str cyclos_version: The last known Cyclos version. Sometimes, data to be cached depends on the version of the Cyclos application, and this helps controlling such cases 
        :param str header_if: Controls the header cache. If is a boolean value (`true` or `false`) will forcibly return or skip the content. Otherwise, it should be a string in the form `id|version`. In this case, the content will be returned only when changed. When blank will always return it. 
        :param str footer_if: Controls the footer cache. If is a boolean value (`true` or `false`) will forcibly return or skip the content. Otherwise, it should be a string in the form `id|version`. In this case, the content will be returned only when changed. When blank will always return it. 
        :param str theme_if: Controls the theme cache. If is a boolean value (`true` or `false`) will forcibly return or skip the content. Otherwise, it should be a string in the form `id|version`. In this case, the content will be returned only when changed. When blank will always return it. 
        :param bool theme_by_components: Flag used to indicate how the theme must be returned (if returned): true means the theme components (base / advanced definitions and custom style) will be filled. Otherwise the final CSS (i. e the theme content). Only valid if the kind of the user interface is NOT `mobile`. For that kind the theme es always returned by its components. 
        :return: DataForUi
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fields', 'kind', 'cyclos_version', 'header_if', 'footer_if', 'theme_if', 'theme_by_components']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method data_for_ui" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
            collection_formats['fields'] = 'multi'  # noqa: E501
        if 'kind' in params:
            query_params.append(('kind', params['kind']))  # noqa: E501
        if 'cyclos_version' in params:
            query_params.append(('cyclosVersion', params['cyclos_version']))  # noqa: E501
        if 'header_if' in params:
            query_params.append(('headerIf', params['header_if']))  # noqa: E501
        if 'footer_if' in params:
            query_params.append(('footerIf', params['footer_if']))  # noqa: E501
        if 'theme_if' in params:
            query_params.append(('themeIf', params['theme_if']))  # noqa: E501
        if 'theme_by_components' in params:
            query_params.append(('themeByComponents', params['theme_by_components']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/ui/data-for-ui', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DataForUi',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
