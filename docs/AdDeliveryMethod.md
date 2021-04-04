# AdDeliveryMethod

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_type** | [**AdDeliveryMethodChargeEnum**](AdDeliveryMethodChargeEnum.md) | The possible charge types for a delivery method of a webshop ad. Possible values are: * fixed: The delivery method charge is fixed set by the seller. * negotiated: The delivery method charge can be be negotiated between the seller and the buyer.  | [optional] 
**delivery_time** | [**TimeInterval**](TimeInterval.md) | The delivery time. | [optional] 
**description** | **str** | Description of the delivery method (if any). | [optional] 
**charge_amount** | [**BigDecimal**](BigDecimal.md) | The delivery method charge amount. Required if &#x60;chargeType&#x60; is  &#x60;fixed&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


