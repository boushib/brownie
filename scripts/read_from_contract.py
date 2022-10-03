from brownie import Storage, accounts, config


def read_from_contract():
  if not Storage:
    print("Storage contract not found!")
    return

  storage = Storage[-1]
  dataStore = storage.get()
  print("dataStore: ", dataStore)
  storage.set(dataStore + 10,
              {"from": accounts.add(config["wallets"]["from_key"])})
  dataStore = storage.get()
  print("dataStore: ", dataStore)


def main():
  read_from_contract()
