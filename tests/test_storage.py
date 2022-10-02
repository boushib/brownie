from brownie import accounts, config, Storage


def test_deploy():
  # Arrange -- Act -- Assert
  account = accounts[0]
  storage = Storage.deploy({"from": account})
  assert storage.get() == 0


def test_update():
  account = accounts[0]
  storage = Storage.deploy({"from": account})
  n = 99
  txn = storage.set(n, {"from": account})
  txn.wait(1)
  assert storage.get() == n
