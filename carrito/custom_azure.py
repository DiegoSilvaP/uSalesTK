from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'usales' # Must be replaced by your <storage_account_name>
    account_key = 'pZIQs1wP2zHGSTl4M5jPkGe0iXi0fwFh5axjO6wZv4Cp9bWhFoPvUZwlF9gnC+h6UONMUUjw862Ex10uMTFaNg==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'usales' # Must be replaced by your storage_account_name
    account_key = 'pZIQs1wP2zHGSTl4M5jPkGe0iXi0fwFh5axjO6wZv4Cp9bWhFoPvUZwlF9gnC+h6UONMUUjw862Ex10uMTFaNg==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None