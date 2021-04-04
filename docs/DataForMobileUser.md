# DataForMobileUser

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_complete_results** | **int** | Number of search results for user autocomplete component | [optional] 
**hide_users_search_menu** | **bool** | Indicates if the user search menu should be hidden. | [optional] 
**auth** | [**Auth**](Auth.md) | The authenticated user | [optional] 
**name_of_user** | **str** | The name of the current user (if any) | [optional] 
**mobile_help** | [**UIElementWithContent**](UIElementWithContent.md) | The help content for mobile mode | [optional] 
**pos_help** | [**UIElementWithContent**](UIElementWithContent.md) | The help content for mobile mode | [optional] 
**map_browser_api_key** | **str** | The Google Maps browser API key | [optional] 
**pages** | [**list[MobilePage]**](MobilePage.md) | The visible mobile pages | [optional] 
**operations** | [**list[Operation]**](Operation.md) | The custom operations the user can run | [optional] 
**can_receive_from_nfc_tag** | **bool** | Indicates whether there is at least one NFC tag the user can use to receive payments  | [optional] 
**personalize_other_users** | **bool** | Indicates if the current user can personalize NFC tags for other users (as member) | [optional] 
**mobile_camera_on_payment** | **bool** | Indicates whether the scan QR code option should be displayed for payments           | [optional] 
**principals_allowing_qr_code** | [**list[Principal]**](Principal.md) | Indicates the possible principals which are allowed to be used in QR code generation | [optional] 
**shopping_cart_web_shop_count** | **int** | The total number of webshop ads present in the shopping cart | [optional] 
**notifications_status** | [**NotificationsStatus**](NotificationsStatus.md) | Status of user notifications, like new received or unread notifications | [optional] 
**allowed_operations** | [**list[MobileOperationEnum]**](MobileOperationEnum.md) | The possible operations the mobile application can perform Possibles values for each array element are: * acceptTicket: Accepts a generated QR code for performing a payment * activateNfcDevice: Activate the phone as NFC device * assignPos: Assign an access client for POS mode * boughtVouchers: View bought vouchers * buyVoucher: Buy a voucher * createTicket: Generate a QR Code for receive payment * deactivateNfcDevice: Deactivate the phone as NFC device * formatNfc: Format NFC tags * initializeNfc: Initialize NFC tags * makeSystemPayment: Perform payments to system * makeUserPayment: Perform payments to other users * manageContacts: Manage own contacts * manageOperators: Manage own/user operators * managePasswords: Manage passwords * mapDirectory: View the user directory (map) * paymentRequests: Search and view payment requests * personalizeNfc: Personalize NFC tags  * personalizeNfcSelf: Personalize NFC tags for the logged user or its operators * purchases: Search and view purchased webshops * readNfc: Read NFC tags * receivePayment: Receive payments from other users * redeemVoucher: Redeem vouchers * registerUsersAsManager: Register other users as user manager * registerUsersAsMember: Register other users as member or operator * sendPaymentRequestToSystem: Send payment requests to system * sendPaymentRequestToUser: Send payment requests to users * unassignPos: Unassign the current access client from POS mode * usersSearch: Search other users * viewAccountInformation: View own accounts * viewAdvertisements: Search and view advertisements and webshop * viewRedeemed: View redeemed vouchers * viewUserProfile: View the profile of other users  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


