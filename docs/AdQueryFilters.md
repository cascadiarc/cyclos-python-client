# AdQueryFilters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner** | **str** | Either id or an identification, such as login name, e-mail, etc, for the advertisement owner. The allowed identification methods are those the authenticated user can use on keywords search.  | [optional] 
**broker** | **str** | Either id or an identification, such as login name, e-mail, etc, for the broker of the advertisement owner. The allowed identification methods are those the authenticated user can use on keywords search.  | [optional] 
**groups** | **list[str]** | Array of either id or internal names of user groups the advertisement owner must belong to  | [optional] 
**return_editable** | **bool** | Whether to return the editable property. Passing &#x60;true&#x60; will impact the performance a bit, as for each returned advertisement some statuses and permissions need to be checked.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


