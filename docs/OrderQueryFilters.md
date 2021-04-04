# OrderQueryFilters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**related_user** | **str** | Either id or an identification, such as login name, e-mail, etc, for the seller or buyer according whether we are searching for purchases  or sales. The allowed identification methods are those the authenticated user can use on keywords search.      | [optional] 
**statuses** | [**list[OrderStatusEnum]**](OrderStatusEnum.md) | The possible statuses for an order Possibles values for each array element are: * completed: The order was accepted by the seller and/or buyer and the related payment was done. * disposed: The order was marked as disposed because the seller and/or buyer were removed or they do not have any account in the order&#39;s currency. * draft: The order has been created by the seller, but has not yet been sent to the buyer for approval * paymentCanceled: The related payment was not done because was canceled after finish the authorization process. * paymentDenied: The related payment was not done because was denied. * paymentPending: The order was accepted by the seller and/or buyer and the related payment is waiting for authorization. * pendingBuyer: The order is pending by the buyer&#39;s action. * pendingSeller: The order is pending by the seller&#39;s action. * rejectedByBuyer: The order was rejected by the buyer. * rejectedBySeller: The order was rejected by the seller.  | [optional] 
**number** | **str** | The generated order number according to the webshop settings. | [optional] 
**creation_period** | **list[datetime]** | The minimum / maximum order creation date. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
**sales** | **bool** | Are we searching for sales or purchases? If not specified it&#39;s assumed purchases (i.e &#x60;false&#x60;) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


