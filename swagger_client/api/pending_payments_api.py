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


class PendingPaymentsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def authorize_pending_payment(self, key, params, **kwargs):  # noqa: E501
        """Authorizes a pending payment.  # noqa: E501

        Authorizes a payment / scheduled payment / recurring payment whose authorization status is `pending`.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authorize_pending_payment(key, params, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str key: Either the id or transaction number. (required)
        :param PendingPaymentActionParams params: Contains the action comments (required)
        :param list[str] fields: Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).  
        :param str confirmation_password: The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel. 
        :return: TransactionAuthorizationLevelData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.authorize_pending_payment_with_http_info(key, params, **kwargs)  # noqa: E501
        else:
            (data) = self.authorize_pending_payment_with_http_info(key, params, **kwargs)  # noqa: E501
            return data

    def authorize_pending_payment_with_http_info(self, key, params, **kwargs):  # noqa: E501
        """Authorizes a pending payment.  # noqa: E501

        Authorizes a payment / scheduled payment / recurring payment whose authorization status is `pending`.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authorize_pending_payment_with_http_info(key, params, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str key: Either the id or transaction number. (required)
        :param PendingPaymentActionParams params: Contains the action comments (required)
        :param list[str] fields: Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).  
        :param str confirmation_password: The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel. 
        :return: TransactionAuthorizationLevelData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key', 'params', 'fields', 'confirmation_password']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method authorize_pending_payment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'key' is set
        if self.api_client.client_side_validation and ('key' not in params or
                                                       params['key'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `key` when calling `authorize_pending_payment`")  # noqa: E501
        # verify the required parameter 'params' is set
        if self.api_client.client_side_validation and ('params' not in params or
                                                       params['params'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `params` when calling `authorize_pending_payment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'key' in params:
            path_params['key'] = params['key']  # noqa: E501

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
            collection_formats['fields'] = 'multi'  # noqa: E501

        header_params = {}
        if 'confirmation_password' in params:
            header_params['confirmationPassword'] = params['confirmation_password']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'params' in params:
            body_params = params['params']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessClient', 'basic', 'session']  # noqa: E501

        return self.api_client.call_api(
            '/pending-payments/{key}/authorize', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TransactionAuthorizationLevelData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def cancel_pending_payment(self, key, params, **kwargs):  # noqa: E501
        """Cancels the authorization process of a pending payment.  # noqa: E501

        Cancels a payment / scheduled payment / recurring payment whose authorization status is `pending`. This action is performed by the payer.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_pending_payment(key, params, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str key: Either the id or transaction number. (required)
        :param PendingPaymentActionParams params: Contains the action comments (required)
        :param str confirmation_password: The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cancel_pending_payment_with_http_info(key, params, **kwargs)  # noqa: E501
        else:
            (data) = self.cancel_pending_payment_with_http_info(key, params, **kwargs)  # noqa: E501
            return data

    def cancel_pending_payment_with_http_info(self, key, params, **kwargs):  # noqa: E501
        """Cancels the authorization process of a pending payment.  # noqa: E501

        Cancels a payment / scheduled payment / recurring payment whose authorization status is `pending`. This action is performed by the payer.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_pending_payment_with_http_info(key, params, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str key: Either the id or transaction number. (required)
        :param PendingPaymentActionParams params: Contains the action comments (required)
        :param str confirmation_password: The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key', 'params', 'confirmation_password']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_pending_payment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'key' is set
        if self.api_client.client_side_validation and ('key' not in params or
                                                       params['key'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `key` when calling `cancel_pending_payment`")  # noqa: E501
        # verify the required parameter 'params' is set
        if self.api_client.client_side_validation and ('params' not in params or
                                                       params['params'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `params` when calling `cancel_pending_payment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'key' in params:
            path_params['key'] = params['key']  # noqa: E501

        query_params = []

        header_params = {}
        if 'confirmation_password' in params:
            header_params['confirmationPassword'] = params['confirmation_password']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'params' in params:
            body_params = params['params']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessClient', 'basic', 'session']  # noqa: E501

        return self.api_client.call_api(
            '/pending-payments/{key}/cancel', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def deny_pending_payment(self, key, params, **kwargs):  # noqa: E501
        """Denies a pending payment.  # noqa: E501

        Denies a payment / scheduled payment / recurring payment whose authorization status is `pending`.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deny_pending_payment(key, params, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str key: Either the id or transaction number. (required)
        :param PendingPaymentActionParams params: Contains the action comments (required)
        :param str confirmation_password: The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.deny_pending_payment_with_http_info(key, params, **kwargs)  # noqa: E501
        else:
            (data) = self.deny_pending_payment_with_http_info(key, params, **kwargs)  # noqa: E501
            return data

    def deny_pending_payment_with_http_info(self, key, params, **kwargs):  # noqa: E501
        """Denies a pending payment.  # noqa: E501

        Denies a payment / scheduled payment / recurring payment whose authorization status is `pending`.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deny_pending_payment_with_http_info(key, params, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str key: Either the id or transaction number. (required)
        :param PendingPaymentActionParams params: Contains the action comments (required)
        :param str confirmation_password: The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key', 'params', 'confirmation_password']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method deny_pending_payment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'key' is set
        if self.api_client.client_side_validation and ('key' not in params or
                                                       params['key'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `key` when calling `deny_pending_payment`")  # noqa: E501
        # verify the required parameter 'params' is set
        if self.api_client.client_side_validation and ('params' not in params or
                                                       params['params'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `params` when calling `deny_pending_payment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'key' in params:
            path_params['key'] = params['key']  # noqa: E501

        query_params = []

        header_params = {}
        if 'confirmation_password' in params:
            header_params['confirmationPassword'] = params['confirmation_password']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'params' in params:
            body_params = params['params']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessClient', 'basic', 'session']  # noqa: E501

        return self.api_client.call_api(
            '/pending-payments/{key}/deny', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
