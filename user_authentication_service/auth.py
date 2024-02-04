#!/usr/bin/env python3
""" auth module """

import bcrypt


def _hash_password(password: str) -> str:
    """hash password"""
    return bcrypt.hashpw(
        password.encode('utf-8'),
        bcrypt.gensalt()
        ).decode('utf-8')
