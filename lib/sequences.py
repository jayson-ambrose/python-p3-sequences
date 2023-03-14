#!/usr/bin/env python3

def print_fibonacci(length):

    fib = []

    if length > 0:
        fib.append(0)

        if length > 1:
            fib.append(1)

            if length > 2 :

                 while(len(fib) < length):
                    fib.append(
                        fib[-1] + fib[-2]
                    )

    print(fib)

    pass