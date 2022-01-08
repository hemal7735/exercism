package account

import "sync"

// Account type
// If any Account method is called on an closed account, it must not modify
// the account and must return ok = false.
type Account struct {
	balance int64
	isOpen  bool
	mutex   sync.Mutex
}

// Open blah blah
// If Open is given a negative initial deposit, it must return nil.
func Open(initialDeposit int64) *Account {

	if initialDeposit < 0 {
		return nil
	}

	var account = Account{
		balance: initialDeposit,
		isOpen:  true,
	}

	return &account
}

// Close blah blah
func (account *Account) Close() (payout int64, ok bool) {

	account.mutex.Lock()

	if account.isOpen {
		payout, ok = account.balance, true

		// cleanup
		account.balance = 0
		account.isOpen = false

	} else {
		payout, ok = 0, false
	}

	account.mutex.Unlock()

	return payout, ok
}

// Balance returns the balance
func (account *Account) Balance() (balance int64, ok bool) {
	account.mutex.Lock()

	if account.isOpen {
		balance, ok = account.balance, true
	} else {
		balance, ok = 0, false
	}

	account.mutex.Unlock()

	return balance, ok
}

// Deposit must handle a negative amount as a withdrawal. Withdrawals must
// not succeed if they result in a negative balance.
func (account *Account) Deposit(amount int64) (newBalance int64, ok bool) {

	account.mutex.Lock()

	if account.isOpen {

		if account.balance+amount < 0 {
			newBalance, ok = account.balance, false
		} else {
			newBalance = account.balance + amount
			account.balance = newBalance
			ok = true
		}
	} else {
		newBalance, ok = 0, false
	}

	account.mutex.Unlock()
	return newBalance, ok

}
