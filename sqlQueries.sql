--register query
INSERT INTO User VALUES (12, "Jane", "Smith", "jsmith@gmail.com", "customer", "jane1")

--login query
select * from User where email = ? AND password = ?

--create account
INSERT INTO Account VALUES (10, 12, "Jane", "Debit", 1200.00)

--add transaction
INSERT INTO Transactions VALUES (450, 10, 12, 33.26, "McDonalds", "Pending")

--get_user_accounts
select * from Account where uid = ?

--get_user_disputes
select * from Transactions where uid = 12

--get_user_disputes
select d.tid, d.status, d.user_reason, d.admin_comments from Disputes as d, Transactions as t where uid = ? AND d.tid = t.tid

--get_transaction_by_account
select * from Transactions where uid = 12 AND account_id = 10

--get_dispute_by_account
select d.tid, d.status, d.user_reason, d.admin_comments from Disputes as d, Transactions as t where uid = 12 AND account_id =10 AND d.tid = t.tid

--dispute_transaction
UPDATE Transactions SET status = "Disputed" where tid = ?
INSERT INTO Disputes VALUES (?, "Pending", "Incorrect Card was used", "NULL")

--get_all_disputes
select * from Disputes

--review_dispute
Update Disputes Set status = ?
Update Transactions Set status = "Complete" FROM Disputes WHERE Disputes.tid = ? AND Disputes.tid = Transactions.tid AND Disputes.status = "Pending"
Update Account Set balance = balance + ? FROM Transactions WHERE Transactions.uid = ? AND Transactions.account_id = ? AND Transactions.uid = Account.uid AND Transactions.account_id = Account.account_id

--deposit
Update Account Set balance = balance + 500000.0 where uid = 12 AND account_id = 10
INSERT INTO Transactions VALUES (?, 10, 12, 500000.0, "Deposit", ?)

--withdrawal
Update Account Set balance = balance - 500000.0 where uid = 12 AND account_id = 10
INSERT INTO Transactions VALUES (?, 10, 12, -500000.0, "Withdrawal", ?)


