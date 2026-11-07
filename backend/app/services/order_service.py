"""Order business rules will be implemented here.

Approval must validate invoice status and stock, lock relevant rows,
update stock and order atomically, and reject repeated approvals.
"""
