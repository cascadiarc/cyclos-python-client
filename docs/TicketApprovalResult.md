# TicketApprovalResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket_number** | **str** | The ticket number identifier. | [optional] 
**ticket_status** | [**TicketStatusEnum**](TicketStatusEnum.md) | The status of a ticket Possible values are: * approved: The ticket was approved by the payer and is waiting to be processed by the receiver to generate the payment * canceled: The ticket was canceled by the receiver before being approved * expired: The ticket has expired without being approved by a payer or canceled by the receiver until the expiration date * open: The ticket was created, but not approved yet * processed: The ticket was approved and processed and the payment was generated  | [optional] 
**cancel_url** | **str** | The URL to redirect when canceling the accept ticket flow | [optional] 
**success_url** | **str** | The URL to redirect after successfully accepting a ticket | [optional] 
**transaction** | [**Transaction**](Transaction.md) | The generated payment. Only if &#x60;status&#x60; is &#x60;processed&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


