# -*- coding: utf-8 -*-

__author__ = 'Peter Bulman'
__email__ = 'bulmanp@gmail.com'
__version__ = '0.1.0'

import argparse
import bcrypt

from Crypto.Hash import SHA256

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("passwd")
    args = parser.parse_args()
    passwd_ct = args.passwd
    passwd_enc = hash_fn(passwd_ct)
    print(passwd_enc)
    encr_fn(passwd_ct)

def hash_fn(passwd_ct):
    """generate a hashed string from the given cleartext string with SHA256"""
    return(SHA256.new(passwd_ct).hexdigest())

def encr_fn(password):
    print("password_ct: " + password)
    # Hash a password for the first time, with a randomly-generated salt
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    print hashed

    # gensalt's log_rounds parameter determines the complexity.
    # The work factor is 2**log_rounds, and the default is 12
    hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))
    print hashed

    # Check that an unencrypted password matches one that has
    # previously been hashed
    if bcrypt.hashpw(password, hashed) == hashed:
        print "It matches"
    else:
        print "It does not match"

if __name__ == '__main__':
    main()
