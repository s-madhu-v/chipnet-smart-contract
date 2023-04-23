import tkinter as tk
from tkinter import ttk

from brownie import accounts
from chipnetapp.data import (
    setMyAccount,
    contractData,
    getMyAccount,
    availabeNetworks,
    getCurrentNetwork,
    changeToNetwork,
)


class settingsPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.createWidgets()
        self.layoutWidgets()

    def createWidgets(self):
        # Account Selector
        self.accountSelectorFrame = tk.Frame(self)
        self.selectLabel = tk.Label(
            self.accountSelectorFrame, text="Select your Account: "
        )
        self.accountComboBox = ttk.Combobox(
            self.accountSelectorFrame, values=[x.address for x in accounts]
        )
        self.accountComboBox.set(getMyAccount().address)
        self.accountComboBox.bind(
            "<<ComboboxSelected>>", lambda event: self.onAccountSelect(event)
        )
        self.accountBalanceLabel = tk.Label(
            self.accountSelectorFrame, text=f"Balance: {getMyAccount().balance()}"
        )
        # Account Creator & Loader
        self.accountCreator = tk.Frame(self)
        self.createLabel = tk.Label(self.accountCreator, text="Create a new Account: ")
        self.keyEntry = tk.Entry(self.accountCreator)
        self.createAccountButton = tk.Button(
            self.accountCreator, text="Create Account", command=self.createAccount
        )

    def layoutWidgets(self):
        self.accountSelectorFrame.grid(row=1, column=0, padx=5, pady=5)
        self.selectLabel.pack(side="left")
        self.accountComboBox.pack(side="left")
        self.accountBalanceLabel.pack()
        self.accountCreator.grid(row=2, column=0, padx=5, pady=5)
        self.createLabel.pack(side="left")
        self.keyEntry.pack(side="left")
        self.createAccountButton.pack(side="left")
        # self.columnconfigure(0, weight=1)
        # self.rowconfigure(0, weight=1)

    def createAccount(self):
        privateKey = self.keyEntry.get()
        if privateKey == "":
            privateKey = None
        accounts.add(privateKey)

    def onAccountSelect(self, event):
        selectedAccount = accounts.at(self.accountComboBox.get())
        setMyAccount(selectedAccount)
        contractData.updateAll()

    def refresh(self):  # TODO: fix this
        print("refreshing")
