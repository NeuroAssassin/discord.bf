import argparse

r = AttributeError
I = Exception
N = staticmethod
J = filter
h = enumerate
F = False
H = list
Y = None
U = len
p = SyntaxError
d = chr
Og = str
Oi = input
Oa = ord
OA = range
OW = callable
Ow = KeyError
Ov = open
On = exit
u = argparse.ArgumentParser
import requests

j = requests.request
import sys

l = sys.stdout
B = sys.maxsize


def t(a, *extras):
    O = a["network"]["request"]
    g = j(method=O["method"], url=O["url"], json=O["body"], headers=O["headers"])
    a["network"].update({"response": g})


def C(a, attribute, *extras):
    if attribute == "STATUS":
        i = a["mapping"]["cellptr"] + 11
        try:
            a["mapping"]["cells"][i] = a["network"]["response"].status_code
        except r:
            raise I("No response object found.")
        return a
    else:
        raise I(f"Unknown/unregistered response attribute: {attribute}")


A = {
    231: {
        232: {
            234: lambda a, *extra: a["network"].update(
                {"request": {"url": "", "headers": {}, "body": {}, "method": ""}}
            ),
            243: {236: lambda a, url, *extra: a["network"]["request"].update({"url": url})},
            222: {
                236: lambda a, key, value, *extra: a["network"]["request"]["headers"].update(
                    {key: value}
                )
            },
            223: {
                236: lambda a, key, value, *extra: a["network"]["request"]["body"].update(
                    {key: value}
                )
            },
            229: lambda a, method, *extra: a["network"]["request"].update({"method": method}),
            150: t,
        },
        234: {224: C},
    }
}


class L:
    @N
    def E(o):
        return "".join(
            J(lambda x: x in [",", ".", "!", "[", "]", "<", ">", "+", "-", "*", "#", ";", "\n"], o)
        )

    @N
    def s(o):
        W, w = [], {}
        for v, f in h(o):
            if f == "[":
                W.append(v)
            elif f == "]":
                n = W.pop()
                w[n] = v
                w[v] = n
        return w

    @N
    def D(o, debug: bool = F):
        o = L.E(H(o))
        w = L.s(o)
        y, c, Q, P, X = [0], 0, 0, -1, -1
        G = []
        a = {"network": {"request": Y, "response": Y}}
        ln = 1
        lc = 1
        while c < U(o):
            f = o[c]
            if f == "\n":
                ln += 1
                lc = 0
            elif f == ">":
                Q += 1
                if Q == U(y):
                    y.append(0)
            elif f == "<":
                Q = 0 if Q <= 0 else Q - 1
            elif f == "+":
                y[Q] = y[Q] + 1
            elif f == "-":
                y[Q] = y[Q] - 1 if y[Q] > 0 else (B * 2 + 1)
            elif f == "[":
                if y[Q] == 0:
                    c = w[c]
                else:
                    P = y[Q]
                    X = Q
            elif f == "]":
                if y[Q] == 0:
                    P = -1
                    X = -1
                else:
                    if y[Q] == P and Q == X:
                        V = "".join(o).split("\n")
                        raise p("Infinite loop: []", ("program.bf", ln, lc, V[ln - 1]))
                    else:
                        c = w[c]
            elif f == ".":
                l.write(d(y[Q]))
            elif f == "!":
                l.write(Og(y[Q]))
            elif f == ",":
                while not G:
                    i = Oi("")
                    for b in i:
                        G.append(b)
                    if i:
                        G.append(0)
                y[Q] = Oa(G[0]) if G[0] != 0 else 0
                G.pop(0)
            elif f == "#":
                if Q < 256:
                    y[Q] = Q
                else:
                    z = Q
                    for _ in OA(0, z // 255):
                        y[Q] = 255
                        Q += 1
                    y[Q] = z % 255
                    for _ in OA(0, z // 255):
                        Q -= 1
            elif f == "*":
                S = Q
                x = A
                while not OW(x):
                    try:
                        K = y[S]
                        x = x[K]
                    except Ow:
                        V = "".join(o).split("\n")
                        raise p(
                            f"Unknown Interrupt: {interrupt_code}",
                            ("program.bf", ln, lc, V[ln - 1]),
                        )
                    S += 1
                S += 1
                q = []
                k = ""
                for m in OA(S, U(y)):
                    if y[m] == 0:
                        if not k:
                            continue
                        q.append(k)
                        k = ""
                    else:
                        k += d(y[m])
                if k:
                    q.append(k)
                a["mapping"] = {"cells": y, "cellptr": Q}
                try:
                    e = x(a, *q)
                except I as e:
                    V = "".join(o).split("\n")
                    raise p(f"Interrupt failure: {str(e)}", ("program.bf", ln, lc, V[ln - 1]))
                if e:
                    a = e
                    y = a["mapping"]["cells"]
                    Q = a["mapping"]["cellptr"]
            elif f == ";" and debug:
                print(f"{cells} - {cellptr}")
                print(a)
            c += 1
            lc += 1


def T():
    M = u(description="Argument Processor for Brainfuck interpreter")
    M.add_argument("file", help="Brainfuck file to run.")
    M.add_argument("--debug", dest="debug", action="store_true", help="Run in Debug mode.")
    R = M.parse_args()
    try:
        f = Ov(R.file, "r")
    except FileNotFoundError:
        print(f"Error: file {args.file} does not exist.  Exiting.")
        On()
    o = f.read()
    f.close()
    L.D(o, R.debug)


if __name__ == "__main__":
    T()
# Created by pyminifier (https://github.com/liftoff/pyminifier)
