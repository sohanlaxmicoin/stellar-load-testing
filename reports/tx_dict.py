#!/usr/bin/env python
"""Load transactions from print_txs.py then create and print a {tx_hash: tx} dictionary.

This will be used to lookup transaction information by their hash when generating reports.
"""
import fileinput
import json
import logging


TX_FIELDS = ("id", "ledger", "source_account", "created_at")


logging.basicConfig(level=logging.DEBUG)


def generate_tx_dict():
    """Read files from stdin generated by print_txs.py and return a {tx_hash: tx} dictionary."""
    txs = {}
    for i, raw_line in enumerate(fileinput.input()):
        if i % 100 == 0:
            logging.debug('processing tx %d', i)

        json_line = json.loads(raw_line)

        # omit 'hash' sub-key from dictionary,
        # since it's also the key of this entry
        txs[json_line['hash']] = {k: json_line[k] for k in TX_FIELDS}

    return txs


if __name__ == '__main__':
    TXS = generate_tx_dict()
    print(json.dumps(TXS))
