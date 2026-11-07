"""Inventory rules belong here, not in the agent layer.

Implement stock changes inside a DB transaction with row locking when
adding order approval. Never subtract stock in a chat tool directly.
"""
