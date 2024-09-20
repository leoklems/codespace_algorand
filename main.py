from algokit_utils.beta.algorand_client import (
    AlgorandClient,
    AssetCreateParams,
    AssetOptInParams,
    AssetTransferParams,
    PayParams,
)

algorand = AlgorandClient.default_local_net()
# Dispenser funds your account initially
dispenser = algorand.account.dispenser()
# KMD is key management deamon which is like your wallet
print(dispenser.address)