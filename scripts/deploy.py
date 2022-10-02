from brownie import accounts, config, Storage
import os


def deploy_storage_contract():
  account = accounts.add(config["wallets"]["from_key"])
  storage = Storage.deploy({"from": account})
  dataStore = storage.get()
  print("dataStore: ", dataStore)
  transaction = storage.set(99, {"from": account})
  transaction.wait(1)
  dataStore = storage.get()
  print("dataStore: ", dataStore)


def main():
  deploy_storage_contract()
