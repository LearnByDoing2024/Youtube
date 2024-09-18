Sure! Let’s break down the logic behind the bank's operations, how transactions are recorded in the ledger, and how the financial report is generated. 

### Overview of Accounts and Ledgers:
In this simulation, we are tracking several key accounts that represent the bank’s operations. The goal is to simulate typical banking transactions and maintain accurate records of all account movements in a **ledger**, and generate a **financial report** summarizing the bank’s financial position.

### 1. **Accounts in the Ledger**:
The bank operates with the following key accounts:

#### **Assets (Owned by the Bank)**:
- **Cash Reserves**: Represents the cash the bank holds.
- **Loans Outstanding**: The total amount of money the bank has loaned out to clients (this is an asset because loans generate interest income).
- **NOSTRO Account**: A foreign currency account used by the bank to manage foreign currency liquidity.

#### **Liabilities (Owed by the Bank)**:
- **Customer Deposits**: The money clients have deposited with the bank. These deposits are considered a liability because the bank owes this money to its customers.

#### **Equity (The Bank’s Own Funds)**:
- **Fee Income**: The total income generated by the bank from fees charged on transactions (deposits and loans).
- **Interest Income**: Income generated from loans as customers pay interest on their borrowed amounts.

### 2. **Transactions**:
Each day, various transactions occur, which affect these accounts. Each transaction is recorded using **double-entry bookkeeping** to ensure that every debit (Dr) has a corresponding credit (Cr). 

The major transactions in the simulation include:

#### a. **Deposits**:
- **Customer deposits money into their account**: The deposit increases both the customer’s balance (liability) and the bank’s cash reserves (asset).
- A **10% fee** is charged on deposits:
  - The net deposit is credited to the **Customer Deposits** account.
  - The deposit fee is credited to the **Fee Income** account.
  - The same net deposit amount is debited to the **Cash Reserves** account, meaning the bank’s cash increases by this amount.

#### b. **Loans Disbursed**:
- **Bank grants a loan to a customer**: The amount of the loan increases the **Loans Outstanding** (asset) and decreases the bank’s **Cash Reserves**.
- A **10% fee** is charged on loans:
  - The net loan disbursed is debited to the **Loans Outstanding** account (the bank now owns a larger asset in the form of a loan).
  - The loan fee is credited to the **Fee Income** account.
  - The same net loan amount is credited to the **Cash Reserves**, reducing the bank’s cash.

#### c. **Payments**:
- **Customers make payments using their deposits**: The customer’s deposit balance decreases (liability), and the bank’s cash reserves also decrease (asset).
- For instance, when a customer makes a payment (such as paying a bill), it results in:
  - A debit from the **Customer Deposits** account.
  - A corresponding credit to the **Cash Reserves** account.

#### d. **Treasury Transactions**:
- **Managing liquidity between foreign (NOSTRO) and local accounts**: The bank might transfer money between its foreign and domestic accounts.
  - A debit from the **NOSTRO Account** (foreign asset).
  - A credit to the **Cash Reserves** (domestic asset), increasing liquidity in local currency.

#### e. **Interest Income**:
- **The bank earns interest on outstanding loans**: The interest amount increases the bank’s **Cash Reserves** and is credited to **Interest Income**, representing revenue for the bank.

### 3. **Daily Ledger**:
Each transaction gets recorded in the **ledger** as follows:
- **Date**: The date of the transaction.
- **Transaction Type**: The type of transaction (e.g., deposit, loan disbursed, client payment).
- **Dr/Cr (Debit or Credit)**: Indicates whether the transaction is a debit (Dr) or credit (Cr).
- **Amount**: The amount of the transaction.
- **Account**: The specific account affected by the transaction (e.g., Customer Deposits, Cash Reserves).
- **Balance After**: The balance of the account after the transaction is recorded.

This forms the basis of the **daily ledger** that tracks all movements across the bank’s accounts.

### 4. **Financial Report**:
At the end of each day, the financial report summarizes the bank’s position by providing a snapshot of:
- **Total Assets**: The sum of all assets, including cash reserves, loans outstanding, and the NOSTRO account.
- **Total Liabilities**: The total amount of customer deposits.
- **Total Equity**: The bank’s own funds, which include fee income, interest income, and net balances after deducting liabilities from assets.

The financial report is generated daily and gives an overview of:
1. **Assets**: Including loans outstanding, cash reserves, and the NOSTRO account.
2. **Liabilities**: Including customer deposits (liabilities owed to customers).
3. **Equity**: Including fee income, interest income, and any remaining bank-owned funds.

Each day’s report reflects the updated balances after all transactions have been processed.

### 5. **Monthly Simulation**:
The code simulates these transactions for 30 days (a month). Each day:
- The ledger is updated with all transactions.
- A financial report is generated, showing the bank’s assets, liabilities, and equity.

At the end of the month:
- The **ledger** and **financial reports** are saved into CSV files.
- These files can be used to analyze daily transactions and overall financial performance.

### Example:
Consider this flow:

1. **Day 1**:
   - A client deposits $10,000.
   - A 10% fee ($1,000) is charged, so the net deposit is $9,000.
   - The ledger will show:
     - $9,000 credited to **Customer Deposits**.
     - $9,000 debited to **Cash Reserves**.
     - $1,000 credited to **Fee Income**.

2. **Day 2**:
   - A loan of $20,000 is disbursed.
   - A 10% fee ($2,000) is charged, so the net loan disbursed is $18,000.
   - The ledger will show:
     - $18,000 debited to **Loans Outstanding**.
     - $18,000 credited to **Cash Reserves**.
     - $2,000 credited to **Fee Income**.

3. **Daily Financial Report**:
   - After Day 1, the report shows:
     - Total assets: Cash Reserves + Loans Outstanding + NOSTRO Account.
     - Total liabilities: Customer Deposits.
     - Total equity: Fee Income + any remaining equity.

This way, the simulation continuously tracks the bank’s operations, generating a detailed ledger and a summary report of the bank’s financial health.