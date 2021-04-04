# OrderResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OrderStatusEnum**](OrderStatusEnum.md) | The possible statuses for an order Possible values are: * completed: The order was accepted by the seller and/or buyer and the related payment was done. * disposed: The order was marked as disposed because the seller and/or buyer were removed or they do not have any account in the order&#39;s currency. * draft: The order has been created by the seller, but has not yet been sent to the buyer for approval * paymentCanceled: The related payment was not done because was canceled after finish the authorization process. * paymentDenied: The related payment was not done because was denied. * paymentPending: The order was accepted by the seller and/or buyer and the related payment is waiting for authorization. * pendingBuyer: The order is pending by the buyer&#39;s action. * pendingSeller: The order is pending by the seller&#39;s action. * rejectedByBuyer: The order was rejected by the buyer. * rejectedBySeller: The order was rejected by the seller.  | [optional] 
**creation_date** | **datetime** | The creation date corresponding to the date when the first item of  this order was added to the shopping cart.  | [optional] 
**currency** | [**Currency**](Currency.md) | The currency of the order. | [optional] 
**number** | **str** | The generated order number according to the webshop settings. | [optional] 
**total_price** | [**BigDecimal**](BigDecimal.md) | The total price of the order, i.e the sum of the total price of all  of its &#x60;items&#x60; and the delivery method (if any).  | [optional] 
**image** | [**Image**](Image.md) | This represents the first image of the first item in the  order (if any)  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


