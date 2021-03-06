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


class CaptchaApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_captcha_content(self, id, **kwargs):  # noqa: E501
        """Returns a captcha image content  # noqa: E501

        Returns the image content of a captcha text. When neither `width` nor `height` are specified, returns the original size. The original ratio is always maintained. When only of one of  the dimensions is specified, it is used as maximum, and the other is calculated. When both are informed, the maximum size with the original ratio that fits both dimensions is used.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_captcha_content(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The object identification (required)
        :param str group: On public / user registration, it is possible to specify a destination group, so the captcha background image will be taken from this new group's configured theme. 
        :param int width: The requested image width
        :param int height: The requested file height
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_captcha_content_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_captcha_content_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_captcha_content_with_http_info(self, id, **kwargs):  # noqa: E501
        """Returns a captcha image content  # noqa: E501

        Returns the image content of a captcha text. When neither `width` nor `height` are specified, returns the original size. The original ratio is always maintained. When only of one of  the dimensions is specified, it is used as maximum, and the other is calculated. When both are informed, the maximum size with the original ratio that fits both dimensions is used.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_captcha_content_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The object identification (required)
        :param str group: On public / user registration, it is possible to specify a destination group, so the captcha background image will be taken from this new group's configured theme. 
        :param int width: The requested image width
        :param int height: The requested file height
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'group', 'width', 'height']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_captcha_content" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `get_captcha_content`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'group' in params:
            query_params.append(('group', params['group']))  # noqa: E501
        if 'width' in params:
            query_params.append(('width', params['width']))  # noqa: E501
        if 'height' in params:
            query_params.append(('height', params['height']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'image/jpeg', 'image/gif', 'image/png'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/captcha/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def new_captcha(self, **kwargs):  # noqa: E501
        """Returns a new captcha challenge  # noqa: E501

        Only allowed when internal captchas are in use.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.new_captcha(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group: On public / user registration, it is possible to specify a destination group, so the captcha background image will be taken from this new group's configured theme. 
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.new_captcha_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.new_captcha_with_http_info(**kwargs)  # noqa: E501
            return data

    def new_captcha_with_http_info(self, **kwargs):  # noqa: E501
        """Returns a new captcha challenge  # noqa: E501

        Only allowed when internal captchas are in use.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.new_captcha_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group: On public / user registration, it is possible to specify a destination group, so the captcha background image will be taken from this new group's configured theme. 
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method new_captcha" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'group' in params:
            query_params.append(('group', params['group']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/captcha', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
