import html, os, re, subprocess, sys
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import CSharpLexer
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
MISS = r"D:\Personal\Downloads\AIUB Object Oriented Programming 2 Notes\Miss-Log.md"
OUT = r"F:\outputs\aiub-oop2\OOP2-Midterm-Final-Review.pdf"
esc = html.escape
FMT = HtmlFormatter(cssclass="hl", style="default")


def inline(t):
    parts = re.split(r"`([^`]*)`", t)
    return "".join(esc(p) if i % 2 == 0 else "<code>%s</code>" % esc(p) for i, p in enumerate(parts))


def code(name):
    return highlight(open(os.path.join(HERE, name + ".cs"), encoding="utf-8").read(), CSharpLexer(), FMT)


def run(name):
    out = subprocess.run([os.path.join(HERE, name + ".exe")], capture_output=True, text=True, check=True).stdout
    return "<pre class='out'>%s</pre>" % esc(out.rstrip("\n"))


TF = [
    ("A class member with no access modifier is private.", "T", "Default for members. A top-level class with no modifier is internal."),
    ("A top-level class with no access modifier is public.", "F", "It is internal."),
    ("A const field can get its value in a constructor.", "F", "const: only in its declaration. readonly: declaration or constructor."),
    ("A const field is automatically static.", "T", "One fixed value for the whole class."),
    ("var gets its type while the program runs.", "F", "Compile time. dynamic is the one checked at run time."),
    ("A struct is a value type.", "T", "Classes and arrays are reference types."),
    ("Arrays in C# are reference types.", "T", "Copying an array variable copies the link, not the items."),
    ("Rows of a jagged array can have the same length.", "T", "They CAN differ; nothing forces them to. 'Can' + allowed = True."),
    ("Every class inherits from System.Object.", "T", "So every object has public ToString(), Equals(), GetHashCode(), GetType()."),
    ("A derived class can access private members of its base class.", "F", "They exist in the child object but only the base class's own code can use them. Use protected or a public property."),
    ("An abstract class can have a constructor.", "T", "It runs when a child object is created."),
    ("An abstract class can be created with new.", "F", "Only its non-abstract children can."),
    ("A sealed class can be inherited.", "F", "sealed = no children."),
    ("An overriding method can change the access modifier of the virtual method.", "F", "Same name, same parameters, same return type, same access."),
    ("A static constructor runs once, before the class is first used.", "T", "No access modifier, no parameters."),
    ("An out parameter must get a value inside the method before it returns.", "T", "ref must have a value before the call; out gets it inside."),
    ("A method can have more than one out parameter.", "T", "Only params is limited: one per method, and it must be last."),
    ("A constructor can have the return type void.", "F", "With void it is an ordinary method and never runs on new."),
    ("Structures can have methods, constructors and properties.", "T", ""),
    ("Overloading = same method name, different parameters.", "T", "Overriding = child replaces a virtual method with the same signature."),
]

MCQ = [
    ("Which keyword calls the parent's constructor from the child's constructor?", "a) this  b) base  c) new  d) override", "b) base", ": base(...) sends values up; the parent's body runs first."),
    ("Same method name, different parameter lists, in one class:", "a) overriding  b) overloading  c) hiding  d) inheritance", "b) overloading", ""),
    ("A child class gives its own version of a method already defined in its base class:", "a) method hiding  b) encapsulation  c) method overriding  d) interface inheritance", "c) method overriding", "Parent method virtual, child method override."),
    ("Accessible only within the same class or a derived class:", "a) public  b) private  c) static  d) protected", "d) protected", ""),
    ("Commonly used to enforce encapsulation by restricting access to class members:", "a) public  b) private  c) static  d) abstract", "b) private", ""),
    ("Accessible anywhere in the same assembly, nowhere else:", "a) internal  b) protected  c) private  d) public", "a) internal", "protected internal = same assembly OR derived classes."),
    ("Casting a value type to a reference type is called:", "a) boxing  b) unboxing  c) both  d) none", "a) boxing", "Unboxing is the way back."),
    ("Which converts a value to a string?", "a) ToInt64()  b) ToByte()  c) ToSingle()  d) ToString()", "d) ToString()", ""),
    ("What does encapsulation primarily do?", "a) hides data  b) allows inheritance  c) enables polymorphism  d) improves performance", "a) hides data", ""),
    ("Which keyword lets a method be overridden?", "a) static  b) sealed  c) virtual  d) const", "c) virtual", "abstract also works, and must be overridden."),
    ("A constructor that takes no parameters is called:", "a) parameterized  b) static  c) default  d) copy", "c) default", "Copy constructor takes an object of the same class."),
    ("If enum members get no values, the compiler gives ___ values starting with ___:", "a) int, 0  b) int, 1  c) null, 0  d) long, 0", "a) int, 0", "enum { a, b, c }: a = 0, b = 1, c = 2."),
    ("int[][] j = new int[2][]; j[0] = new int[] {1, 2}; j[1] = new int[] {3, 4, 5}; Console.WriteLine(j[1][3]);", "a) 3  b) 4  c) 5  d) exception", "d) exception", "Row 1 has indexes 0, 1, 2 only. [3] is out of range."),
    ("'Is-a' relationship between two classes means:", "a) polymorphism  b) inheritance  c) abstraction  d) encapsulation", "b) inheritance", "Has-a = a field."),
    ("Which keyword groups related classes?", "a) new  b) namespace  c) using  d) package", "b) namespace", "using only brings a namespace in."),
    ("Which is an explicit cast?", "a) int a = 10.5;  b) double b = 5;  c) int a = (int)10.5;  d) byte b = (bool)1;", "c)", "Type in brackets = explicit. (int)10.5 = 10, it cuts, never rounds."),
]


def tf_html():
    rows = "".join("<tr><td class='n'>%d</td><td>%s</td><td class='a'>%s</td><td class='w'>%s</td></tr>" % (i, esc(s), a, esc(w))
                   for i, (s, a, w) in enumerate(TF, 1))
    return "<table class='key'><tr><th>#</th><th>Statement</th><th></th><th>Why</th></tr>%s</table>" % rows


def mcq_html():
    out = []
    for i, (q, o, a, w) in enumerate(MCQ, 1):
        out.append("<div class='mcq'><b>%d.</b> %s<div class='opts'>%s</div><div class='ans'>Answer: <b>%s</b>%s</div></div>"
                   % (i, inline(q) if "`" in q else esc(q), esc(o), esc(a), (" &middot; " + esc(w)) if w else ""))
    return "".join(out)


def miss_html():
    rows = []
    for line in open(MISS, encoding="utf-8"):
        if not line.startswith("| ") or line.startswith("| Q |"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split(" | ")]
        if len(cells) != 4:
            sys.exit("bad miss-log row: " + line)
        rows.append("<tr>%s</tr>" % "".join("<td>%s</td>" % inline(c) for c in cells))
    return len(rows), "<table class='miss'><tr><th>Q</th><th>You wrote</th><th>Right</th><th>Rule</th></tr>%s</table>" % "".join(rows)


n_miss, miss = miss_html()
CSS = """
@page { size: A4; margin: 13mm 14mm 14mm 14mm; }
body { font-family: 'Segoe UI', Arial, sans-serif; font-size: 10pt; color: #1a1a1a; line-height: 1.35; }
h1 { font-size: 18pt; margin: 0 0 2pt; } h2 { font-size: 13pt; margin: 14pt 0 5pt; border-bottom: 1.5pt solid #1f4e79; color: #1f4e79; }
.sub { color: #555; margin-bottom: 8pt; }
table { border-collapse: collapse; width: 100%; } td, th { border: 0.6pt solid #bbb; padding: 3pt 5pt; vertical-align: top; text-align: left; }
th { background: #eef3f8; } tr { break-inside: avoid; }
.key td.n { width: 16pt; color: #555; } .key td.a { width: 14pt; font-weight: bold; text-align: center; } .key td.w { color: #333; width: 45%; }
.mcq { margin: 0 0 6pt; break-inside: avoid; } .opts { color: #333; margin-left: 14pt; } .ans { margin-left: 14pt; color: #14532d; }
code, pre { font-family: Consolas, monospace; font-size: 8.8pt; } code { background: #f3f3f3; padding: 0 2pt; }
pre { margin: 0; white-space: pre-wrap; } .hl { background: #fafafa; border: 0.6pt solid #ddd; padding: 5pt 7pt; }
.out { background: #111; color: #eee; padding: 5pt 7pt; border-radius: 3pt; }
.box { border-left: 3pt solid #1f4e79; background: #f4f8fb; padding: 5pt 8pt; margin: 6pt 0; break-inside: avoid; }
.miss { font-size: 8.8pt; } .miss td:first-child { width: 34pt; white-space: nowrap; }
.cols { display: flex; gap: 10pt; } .cols > div { flex: 1; min-width: 0; }
""" + FMT.get_style_defs(".hl")

BODY = f"""
<h1>OOP2 Midterm: final read-through</h1>
<div class="sub">CSC 3115 &middot; about 25 minutes &middot; read top to bottom, answers included. Nothing new: this is what you already practised.</div>

<div class="box"><b>In the exam (2 hours):</b> Part A first, fast (about 30 min, 1.5 marks each, never leave one blank) &middot;
Part C code next (about 50 min): fields, constructors, methods first, properties last &middot; Part B trace: pick the one you can draw a table for &middot;
Part D last. Before handing in: every <code>{{</code> has its <code>}}</code>, every statement ends with <code>;</code>, capitals on <code>System</code>, <code>Console</code>, class names.</div>

<h2>1 &middot; True / False (20)</h2>
{tf_html()}

<h2>2 &middot; MCQ (16)</h2>
{mcq_html()}

<h2 style="break-before:page">3 &middot; Output tracing</h2>
<div class="cols"><div>{code("trace")}</div><div>
<p><b>Output:</b></p>{run("trace")}
<div class="box">
<b>Why, line by line</b><br>
1. <code>new Student("Nila", 3.80)</code>: <code>: base(name)</code> sends "Nila" UP, so Person's body runs first: <code>count</code> becomes 1, prints <code>Person Nila</code>. Then Student's body: <code>Student 3.8</code>.<br>
2. A double prints without trailing zeros: <code>3.80</code> &rarr; <code>3.8</code>.<br>
3. <code>p</code> is a Person variable but holds a Student, and Show is virtual/override, so <b>Student's</b> Show runs: <code>base.Show()</code> uses <code>Write</code> (stays on the line), then <code>WriteLine(cgpa)</code> &rarr; <code>Nila 3.8</code>.<br>
4. Same for Rafi; <code>count</code> becomes 2.<br>
5. <code>count</code> is static: ONE shared box for all objects &rarr; <code>count = 2</code>.
</div></div></div>

<h2 style="break-before:page">4 &middot; Code writing (Fall 2022-23 Part C, adapted)</h2>
<div class="box">An IT company keeps employee data. Every <b>Employee</b> has id, name, salary and a joining date. Joining date is a <b>custom type</b> you must create (<code>MyDate</code>: day, month, year).
<b>FullTime</b> employees also have a bonus; <b>PartTime</b> employees have a commission. <code>ShowInfo()</code> shows all information. <code>GrossIncome()</code> prints the income:
FullTime = 12 months' salary + 2 bonuses; PartTime = salary + commission. Main is given.</div>
<p><b>The two new things vs D5 and Q33:</b> (1) Main uses <code>new MyDate(...)</code>, a class the question only names, so you write it: fields, constructor, one print method; Employee gets a field of that type. (2) The child needs the parent's private <code>salary</code>, so it uses the public property <code>Salary</code>. Note <code>09</code> prints as <code>9</code>.</p>
{code("code")}
<p><b>Output:</b></p>{run("code")}

<h2 style="break-before:page">5 &middot; Your Miss log ({n_miss} rows)</h2>
<p class="sub">Every mistake you actually made this week. Read the Right and Rule columns.</p>
{miss}
"""

doc = "<!doctype html><html><head><meta charset='utf-8'><title>OOP2 Final Review</title><style>%s</style></head><body>%s</body></html>" % (CSS, BODY)
tmp = os.path.join(HERE, "review.html")
open(tmp, "w", encoding="utf-8").write(doc)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    pg.goto("file:///" + tmp.replace("\\", "/"))
    pg.pdf(path=OUT, format="A4", print_background=True, prefer_css_page_size=True,
           display_header_footer=True, header_template="<div></div>",
           footer_template="<div style='font-size:8pt;width:100%;text-align:center;color:#777'><span class='pageNumber'></span> / <span class='totalPages'></span></div>")
    b.close()
print(OUT, n_miss)
