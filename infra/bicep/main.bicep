param location string = resourceGroup().location
param environment string = 'dev'
@secure()
param sqlAdminPassword string

resource storage 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: 'stdata${environment}${uniqueString(resourceGroup().id)}'
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {
    isHnsEnabled: true
    minimumTlsVersion: 'TLS1_2'
    allowBlobPublicAccess: false
  }
}

resource sqlServer 'Microsoft.Sql/servers@2022-05-01-preview' = {
  name: 'sql-data-${environment}-${uniqueString(resourceGroup().id)}'
  location: location
  properties: {
    administratorLogin: 'sqladminuser'
    administratorLoginPassword: sqlAdminPassword
  }
}

output storageName string = storage.name
output sqlServerName string = sqlServer.name
