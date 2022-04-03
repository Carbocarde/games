from multiprocessing.connection import Client

import sys

args = sys.argv

if len(args) != 2:
    print("incorrect usage! do: python client.py <port>")

port = int(args[1])
address = ("localhost", port)
conn = Client(address)

while 1:
    x = conn.recv()
    print(x)

    # really bad way to check / respond to messages from the bs bot,
    # but this small snippet should give you enough to figure out how
    # to create your own client.
    if x != "Provide space seperated list of cards you want to play":
        conn.send("0")
