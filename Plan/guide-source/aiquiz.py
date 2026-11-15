import sys
def edit(path, old, new):
    s = open(path, encoding="utf-8").read()
    assert s.count(old) == 1, old
    open(path, "w", encoding="utf-8").write(s.replace(old, new))
edit(sys.argv[1], "AI Quiz 2: uninformed search (BFS, UCS, DFS, DLS, IDS, bidirectional, complexity), short Q&amp;A, date not announced.",
     "AI Quiz 2 (uninformed search): probably already held on Nov 1, so no prep planned.")
edit(sys.argv[2], "Dates not announced yet: AI Quiz 2 (uninformed search), EM Quiz 2", "Dates not announced yet: EM Quiz 2")
print("ok")
