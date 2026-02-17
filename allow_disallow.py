from collections import defaultdict

def resolve_effective_allows(n, inherits, allow, disallow):
    parents = defaultdict(list)
    for child, parent in inherits:
        parents[child].append(parent)
    allow_list = [set(x) for x in allow]
    disallow_list = [set(x) for x in disallow]

    memo = {}
    def dfs(u):
        if u in memo:
            return memo[u]
        inherited = set()
        for parent in parents[u]:
            inherited |= dfs(parent)
        eff = (inherited|allow_list[u]) - disallow_list[u]
        memo[u] =eff
        return eff
    return [dfs(u) for u in range(n)]





def run_tests():
    def show(res):
        return [sorted(list(s)) for s in res]

    # Test 1: 你给的例子：只继承 allow，不继承 block；自己的 block override 继承来的 allow
    n = 3
    inherits = [(1, 2)]
    allow = [[], ["A"], ["B"]]
    block = [[], ["B"], []]
    # role2 eff={B}; role1 eff=({B}∪{A})-{B}={A}
    expected = [[], ["A"], ["B"]]

    res = resolve_effective_allows(n, inherits, allow, block)
    assert show(res) == expected, (show(res), expected)

    # Test 2: 父的 block 不会传给子（子仍可 allow 同权限）
    n = 2
    inherits = [(1, 0)]
    allow = [["A"], ["B"]]
    block = [["B"], []]
    # role0 eff={A}; role1 eff=({A}∪{B})-{}={A,B}
    expected = [["A"], ["A", "B"]]

    res = resolve_effective_allows(n, inherits, allow, block)
    assert show(res) == expected, (show(res), expected)



run_tests()