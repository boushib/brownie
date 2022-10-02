from brownie import accounts, config, Storage, network


def get_account():
  if network.show_active() == "development":
    return accounts[0]
  else:
    return accounts.add(config["wallets"]["from_key"])


def deploy_storage_contract():
  account = get_account()
  storage = Storage.deploy({"from": account})
  dataStore = storage.get()
  print("dataStore: ", dataStore)
  transaction = storage.set(99, {"from": account})
  transaction.wait(1)
  dataStore = storage.get()
  print("dataStore: ", dataStore)


def main():
  deploy_storage_contract()
