"""Hermetic socket isolation for pytest test runner.

Raises SocketBlockedError on any outbound TCP/UDP network connection attempts.
Ensures 100% deterministic, offline, and hermetic execution across all test tiers.
"""

import socket
import pytest


class SocketBlockedError(RuntimeError):
    """Raised when an outbound network call is attempted under hermetic test isolation."""
    pass


_orig_connect = socket.socket.connect
_orig_connect_ex = socket.socket.connect_ex
_orig_create_connection = socket.create_connection
_orig_sendto = socket.socket.sendto


def _guarded_connect(self, address):
    raise SocketBlockedError(
        f"Hermetic socket isolation: Outbound network connection to {address} is strictly forbidden."
    )


def _guarded_connect_ex(self, address):
    raise SocketBlockedError(
        f"Hermetic socket isolation: Outbound network connection to {address} is strictly forbidden."
    )


def _guarded_create_connection(address, timeout=None, source_address=None):
    raise SocketBlockedError(
        f"Hermetic socket isolation: Outbound connection creation to {address} is strictly forbidden."
    )


def _guarded_sendto(self, data, *args):
    if args:
        target = args[-1]
        raise SocketBlockedError(
            f"Hermetic socket isolation: Outbound UDP sendto {target} is strictly forbidden."
        )
    return _orig_sendto(self, data, *args)


@pytest.fixture(autouse=True, scope="session")
def enforce_hermetic_socket_isolation():
    """Session-wide fixture intercepting all socket outbound network traffic."""
    socket.socket.connect = _guarded_connect
    socket.socket.connect_ex = _guarded_connect_ex
    socket.create_connection = _guarded_create_connection
    socket.socket.sendto = _guarded_sendto
    try:
        yield
    finally:
        socket.socket.connect = _orig_connect
        socket.socket.connect_ex = _orig_connect_ex
        socket.create_connection = _orig_create_connection
        socket.socket.sendto = _orig_sendto
