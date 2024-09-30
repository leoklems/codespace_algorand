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
# print(dispenser.address)

creator = algorand.account.random()
# print(creator.address)

# account details before transfer of funds
# print(algorand.account.get_information(creator.address))

algorand.send.payment(
    PayParams(
        sender=dispenser.address,
        receiver=creator.address,
        amount=10_000_000 #10 million microalgos
    )
)

# to get account details of the creator after transfer of funds
# print(algorand.account.get_information(creator.address))

# Create asset
sent_tan = algorand.send.asset_create(
    AssetCreateParams(
        sender=creator.address,
        total=200,
        asset_name="BUILDLEARN",
        unit_name="HER"
    )
)

# Extract the asset id
asset_id = sent_tan["confirmation"]["asset-index"]
print(asset_id)
# print(sent_tan)

# Create a recever account

receiver_acct = algorand.account.random()
print(receiver_acct.address)

# send asset from creator to recever

# Ensure that your receiver has some tokens and optin

algorand.send.payment(
    PayParams(
        sender=dispenser.address,
        receiver=receiver_acct.address,
        amount=10_000_000 #10 million microalgos
    )
)

algorand.send.asset_opt_in(
    AssetOptInParams(
        sender=receiver_acct.address,
        asset_id=asset_id
    )
)

assert_transfer = algorand.send.asset_transfer(
    AssetTransferParams(
        sender=creator.address,
        receiver=receiver_acct.address,
        asset_id=asset_id,
        amount=100
    )
)

print(algorand.account.get_information(receiver_acct.address))