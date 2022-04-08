from graphviz import Digraph
import itertools
import queue


class Transition:
    def __init__(self, current_node, symbol, next_node):
        self.current = current_node
        self.symbol = symbol
        self.next = next_node


class DFA:
    def __init__(self, title, sigma, q, delta, q0, f):
        self.title = title
        self.sigma = sigma
        self.q = q
        self.delta = delta
        self.q0 = q0
        self.f = f

    def compare(self, other):
        if set(self.sigma) != set(other.sigma):
            return False
        if set(self.q) != set(other.q):
            return False
        d1_list = []
        for t in self.delta:
            d1_list.append((t.current, t.symbol, t.next))
        d2_list = []
        for t in other.delta:
            d2_list.append((t.current, t.symbol, t.next))
        if set(d1_list) != set(d2_list):
            return False
        if set(self.q0) != set(other.q0):
            return False
        if set(self.f) != set(other.f):
            return False
        return True

    def view(self, result_format='png', show_nodes=True, save=False, filename=''):
        graph = Digraph(self.title, format=result_format, node_attr={'shape': 'circle'})
        graph.graph_attr['rankdir'] = 'LR'
        graph.node('0', shape='point')
        graph.edge('0', ','.join(sorted(self.q0)))
        if show_nodes:
            for state in self.q:
                node_label = ','.join(sorted(state))
                if state in self.f:
                    graph.node(node_label, shape='doublecircle')
                else:
                    graph.node(node_label)
        for state in self.q:
            dict = {}
            for symbol in self.sigma:
                _next = self.next_all(state, symbol)
                if len(_next) > 0:
                    for _n in _next:
                        k = ','.join(sorted(_n))
                        if k in dict:
                            dict[k].append(symbol)
                        else:
                            dict[k] = [symbol]
            for k in dict:
                graph.edge(','.join(sorted(state)), ''.join(k), ', '.join(dict[k]))
        if save:
            if not filename:
                filename = 'test.dot'
            graph.render(filename)
        else:
            graph.view()
            from time import sleep
            sleep(1)

    def next(self, state, symbol):
        for d in self.delta:
            if d.current == state and d.symbol == symbol:
                return d.next

    def next_all(self, state, symbol):
        next_list = []
        for d in self.delta:
            if d.current == state and d.symbol == symbol:
                next_list.append(d.next)
        return next_list

    def cross_product(self, dfa2, title, f):
        sigma = self.sigma.union(dfa2.sigma)
        q = list(itertools.product(self.q, dfa2.q))
        q0 = self.q0 + dfa2.q0
        delta = []
        history = []
        for state in q:
            for symbol in sigma:
                delta.append(Transition(state, symbol, (self.next(state[0], symbol), dfa2.next(state[1], symbol))))
            history.append(DFA(title, sigma, q, delta.copy(), q0, f))
        return DFA(title, sigma, q, delta, q0, f), history

    def intersection(self, dfa2):
        title = self.title + ' intersection ' + dfa2.title
        f = list(itertools.product(self.f, dfa2.f))
        return self.cross_product(dfa2, title, f)

    def union(self, dfa2):
        title = self.title + ' union ' + dfa2.title
        f = list(set(list(itertools.product(self.f, dfa2.q))).union(set(list(itertools.product(self.q, dfa2.f)))))
        return self.cross_product(dfa2, title, f)

    def difference(self, dfa2):
        title = self.title + ' difference ' + dfa2.title
        f = list(itertools.product(set(self.f), set(dfa2.q).difference(set(dfa2.f))))
        return self.cross_product(dfa2, title, f)

    def thompson(self):
        q = queue.Queue()
        q.put(set(self.q0))
        last = [set(self.q0)]
        delta = []
        f = []
        history = []
        while not q.empty():
            node_set = q.get()
            for symbol in self.sigma:
                q_next = []
                is_node_final = False
                for node in node_set:
                    if node in self.f:
                        is_node_final = True
                    q_next.extend(self.next_all(node, symbol))
                if is_node_final:
                    f.append(set(q_next))
                delta.append(Transition(node_set, symbol, set(q_next)))
                if set(q_next) not in last:
                    q.put(set(q_next))
                    last.append(set(q_next))
            history.append(DFA("NFA to DFA", self.sigma, last, delta.copy(), self.q0, f))
        return DFA("NFA to DFA", self.sigma, last, delta, self.q0, f), history
