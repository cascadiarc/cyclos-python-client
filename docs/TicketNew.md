# TicketNew

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payer** | **str** | An identification for the user which will pay the ticket. Is optional, and in most cases, should be left empty. If empty, at the moment the client will pay the ticket, both user identification and password will be entered, and the ticket will be confirmed. If specified, when confirming, only that user will be able to pay the ticket.   | [optional] 
**cancel_url** | **str** | The url to redirect when canceling the approve ticket flow. If an &#x60;orderId&#x60; is given then it will be added as a query parameter to this url when redirect as well as the ticket number too.  | [optional] 
**success_url** | **str** | The url to redirect after successful approving a ticket.  If an &#x60;orderId&#x60; is given then it will be added as a query parameter to this url when redirect as well as the ticket number too.  | [optional] 
**success_webhook** | **str** | The url to be invoked by the server after successfully approving a  ticket. If an &#x60;orderId&#x60; is given then it will be added as a query parameter to this url when redirect as well as the ticket number too.            | [optional] 
**order_id** | **str** | An optional order identifier given by the ticket&#39;s creator. If given  then that identifier will be used at ticket processing to ensure the  ticket is for that order. This attribute is usefull in case the client doesn&#39;t want to reflect  the generated ticket number in its database after creating the ticket,  | [optional] 
**expires_after** | [**TimeInterval**](TimeInterval.md) | Defines the expiration interval. If none is given, it is assumed that the ticket expires in one day.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


