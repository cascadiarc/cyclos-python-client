# FullProfileEdit

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**UserEdit**](UserEdit.md) | The basic fields. If null, the fields are not modified | [optional] 
**create_land_line_phones** | [**list[PhoneNew]**](PhoneNew.md) | Land-line phones to be created. If not sent / empty, no land-line phones are created.  | [optional] 
**create_mobile_phones** | [**list[PhoneNew]**](PhoneNew.md) | Mobile phones to be created. If not sent / empty, no mobile phones are created.  | [optional] 
**modify_land_line_phones** | [**list[PhoneEditWithId]**](PhoneEditWithId.md) | Land-line phones to be modified. If not sent / empty, no land-line phones are modified  | [optional] 
**modify_mobile_phones** | [**list[PhoneEditWithId]**](PhoneEditWithId.md) | Mobile phones to be modified. If not sent / empty, no mobile phones are modified.  | [optional] 
**remove_phones** | **list[str]** | Phones (both land-line and mobile) to be removed. If not sent / empty, no phones are removed.  | [optional] 
**create_addresses** | [**list[AddressNew]**](AddressNew.md) | Addresses to be created. If not sent / empty, no  addresses are created.  | [optional] 
**modify_addresses** | [**list[AddressEditWithId]**](AddressEditWithId.md) | Addresses to be modified. If not sent / empty, no  addresses are modified.  | [optional] 
**remove_addresses** | **list[str]** | Addresses to be removed. If not sent / empty, no addresses are removed.  | [optional] 
**create_contact_infos** | [**list[ContactInfoNew]**](ContactInfoNew.md) | Additional contacts to be created. If not sent / empty, no additional contacts are created.  | [optional] 
**modify_contact_infos** | [**list[ContactInfoEditWithId]**](ContactInfoEditWithId.md) | Additional contacts to be modified. If not sent / empty, no  additional contacts are modified.  | [optional] 
**remove_contact_infos** | **list[str]** | Additional contacts to be removed. If not sent / empty, no additional contacts are removed.  | [optional] 
**add_images** | **list[str]** | Identifiers of previously uploaded temporary images to be added as profile images. If not sent / empty, no images are added.  | [optional] 
**remove_images** | **list[str]** | Identifiers of existing profile images to be removed. If not sent / empty, no images are removed.  | [optional] 
**reorder_images** | **list[str]** | Identifiers of either existing or added profile images in the order they should be listed.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


