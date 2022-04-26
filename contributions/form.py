from django.forms import ModelForm, ValidationError
from django.contrib import messages
from .models import DailyContribution, TargetContribution, WalletTransaction


class DailyContributionForm(ModelForm):
    class Meta:
        model = DailyContribution
        fields = (
            "transaction_type",
            "amount",
            "bank_account",
            "balance_after_transaction",
        )

    def clean(self) -> None:
        super(DailyContributionForm, self).clean()

        # transaction_type
        transaction_type = self.cleaned_data.get("transaction_type")
        bank_account = self.cleaned_data.get("bank_account")
        amount = self.cleaned_data.get("amount")
        # check if amount is greater than balance raise validationerror
        if transaction_type == 2:
            if amount > bank_account.bank_account_balance:
                raise ValidationError("Insufficient Balance!")
            else:
                pass

        return self.cleaned_data


class WalletTransactionForm(ModelForm):
    class Meta:
        model = WalletTransaction
        fields = (
            "transaction_type",
            "amount",
            "bank_account_user",
            "wallet_account",
            "balance_after_transaction",
        )

    def clean(self) -> None:
        super(WalletTransactionForm, self).clean()

        # transaction_type
        transaction_type = self.cleaned_data.get("transaction_type")
        wallet_account = self.cleaned_data.get("wallet_account")
        amount = self.cleaned_data.get("amount")
        # check if amount is greater than balance raise validationerror
        if transaction_type == 2:
            if amount > wallet_account.wallet_balance:
                raise ValidationError("Insufficient Balance!")
            else:
                pass

        return self.cleaned_data
