# Bank
A bank wants to implement a customer account management system that 
supports the following operations:

Add funds to a customer account.

Withdraw money from an account.

Query the balance of funds on an account.

Transfer money between customer accounts.

Calculate interest for all customers.

You need to implement such a system. The bank's customers are 
identified by names (a unique string that does not contain spaces). 
Initially, the bank does not have any customers. As soon as a 
customer is refilled, withdrawn or transferred money, an account 
with a zero balance is created for him. All further operations are 
carried out only with this account. The amount on the account can 
be both positive and negative, but is always an integer.

## Input format
The input file contains a sequence of operations. The following 
operations are possible: DEPOSIT name sum - credit the amount sum 
to the account of the customer name. If the customer does not have 
an account, the account is created. WITHDRAW name sum - withdraw 
the amount sum from the account of the customer name. If the 
customer does not have an account, the account is created. BALANCE 
name - find out the balance of funds on the account of the client 
name. TRANSFER name1 name2 sum - transfer the amount sum from the 
account of the client name1 to the account of the client name2. If 
any client does not have an account, then an account is created for 
him. INCOME p - accrue p% of the account amount to all clients who 
have open accounts. Interest is accrued only to clients with a 
positive balance on the account; if the client has a negative 
balance, then his account does not change. After accrual of 
interest, the amount on the account remains whole, that is, only a 
whole number of monetary units is accrued. The fractional part of 
the accrued interest is discarded.

## Output format
For each BALANCE request, the program must display the account 
balance of this client. If the client with the requested name does 
not have an open account in the bank, display ERROR.