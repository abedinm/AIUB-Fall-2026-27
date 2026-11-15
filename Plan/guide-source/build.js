const fs = require('fs');
const vm = require('vm');
const path = require('path');

const PLAN = 'F:\\outputs\\midterm-plan\\Midterm-Study-Plan.html';
const OUT = process.argv[2];
const PAGES = process.argv[3] && fs.existsSync(process.argv[3]) ? JSON.parse(fs.readFileSync(process.argv[3], 'utf8')) : {};

const src = fs.readFileSync(PLAN, 'utf8');
const m = src.match(/const DAYS = (\[[\s\S]*?\]);\s*\n\s*const KEY/);
if (!m) throw new Error('DAYS not found in plan');
const DAYS = vm.runInNewContext('(' + m[1] + ')');

const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const pg = key => (PAGES[key] ? 'p. ' + PAGES[key] : 'p. --');

const META = {
  'Tue Nov 3':  { day: 'Tuesday',   n: '03', badge: 'Quizzes tomorrow · 5 days to AI + EM', one: "Get enough C# into your head for tomorrow's OOP2 quiz, and lock in the EM capacity maths." },
  'Wed Nov 4':  { day: 'Wednesday', n: '04', badge: 'Quiz day · 4 days to AI + EM', one: 'Two quizzes and your Slide 4. After that, prepare for the AI lab test.' },
  'Thu Nov 5':  { day: 'Thursday',  n: '05', badge: 'AI lab test 15:00 · 3 days to AI + EM', one: 'Walk into the 15:00 lab test able to code Lab 01 and Lab 02 from a blank notebook.' },
  'Fri Nov 6':  { day: 'Friday',    n: '06', badge: 'MIS assignment due · 2 days to AI + EM', one: 'MIS Assignment 1 visible on the Teams wall by 21:00.' },
  'Sat Nov 7':  { day: 'Saturday',  n: '07', badge: 'AI + EM tomorrow', one: 'AI first, then EM math from zero. Slept 01:15.' },
  'Sun Nov 8':  { day: 'Sunday',    n: '08', badge: 'Exam day · AI 09:00 · EM 15:00', one: 'Two exams. AI read-only in the morning, EM blocks between the exams.' },
  'Mon Nov 9':  { day: 'Monday',    n: '09', badge: 'MIS tomorrow 09:00', one: 'MIS from zero: two study packs, chapter by chapter, sleep at 23:00.' },
  'Tue Nov 10': { day: 'Tuesday',   n: '10', badge: 'Exam day · MIS 09:00', one: 'MIS exam, then start the Python project with your group.' },
  'Wed Nov 11': { day: 'Wednesday', n: '11', badge: '4 days to OOP2 · Python due in 3', one: 'OOP2 Weeks 1-3 in the morning, Python build in the afternoon.' },
  'Thu Nov 12': { day: 'Thursday',  n: '12', badge: '3 days to OOP2 · Python due in 2', one: 'OOP2 Weeks 4-5 and coding, then the Python library feature.' },
  'Fri Nov 13': { day: 'Friday',    n: '13', badge: '2 days to OOP2 · Python due tomorrow', one: 'Sit the OOP2 mock exam. Make the Python project crash-proof.' },
  'Sat Nov 14': { day: 'Saturday',  n: '14', badge: 'Python submission today · OOP2 tomorrow', one: 'Email the Python project by 16:00. Then OOP2 final revision.' },
  'Sun Nov 15': { day: 'Sunday',    n: '15', badge: 'Exam day · OOP2 12:00', one: 'OOP2 exam. Read only in the morning.' },
  'Mon Nov 16': { day: 'Monday',    n: '16', badge: 'Python demo today', one: 'Demo the project, then prepare for Python Quiz 2.' }
};

const COURSE = {
  'EM': { cls: 'em', label: 'EM', helper: 'Engineering Management' },
  'AI': { cls: 'ai', label: 'AI', helper: 'AI mid note' },
  'AI lab': { cls: 'ai', label: 'AI LAB', helper: 'AI mid note' },
  'MIS': { cls: 'mis', label: 'MIS', helper: 'Management Information Systems' },
  'OOP2': { cls: 'oop', label: 'OOP2', helper: 'Object-Oriented Programming 2' },
  'Python': { cls: 'py', label: 'PYTHON', helper: 'Programming in Python' },
  'Admin': { cls: 'adm', label: 'ADMIN', helper: '' },
  'EXAM': { cls: 'exam', label: 'EXAM', helper: '' }
};

const EXTRA = {
  'Tue Nov 3': `<div class="callout oop"><b>OOP2 tonight = one 19-page PDF, plain C#:</b> <code>F:\\outputs\\aiub-oop2\\OOP2-Quiz2-90-Minutes.pdf</code>. Page numbers = the number at the bottom. Answers on p. 17-18.</div>`,
  'Wed Nov 4': `<div class="callout em"><b>Slide 4 rule:</b> the course allows AI only for analysis and preparation. You build and say your own slide; the EM session only checks your numbers and asks you questions.</div>`
};

function splitTime(t) {
  const p = t.split('-');
  return p.length === 2 ? `${esc(p[0])}<span>to ${esc(p[1])}</span>` : esc(t);
}

function kind(row) {
  const [time, course, task, check] = row;
  if (course === '-') return 'rest';
  if (course === 'EXAM') return 'exam';
  if (/^Class/.test(task) && /Quiz/.test(task)) return 'quiz';
  if (/^(Class|Theory class)/.test(task) || time === 'Lab class') return 'class';
  return 'study';
}

function renderRow(row) {
  const [time, course, task, check] = row;
  const c = COURSE[course] || COURSE.Admin;
  const k = kind(row);
  if (k === 'rest') return `<div class="rest"><span>${esc(time)}</span>${esc(task)}</div>`;
  if (k === 'exam') return `<div class="exam card-x"><div class="time">${splitTime(time)}</div><div class="etxt"><span class="xlabel">EXAM</span>${esc(task)}</div><div class="xbadge">GO</div></div>`;
  if (k === 'quiz' || k === 'class') {
    const lab = k === 'quiz' ? 'QUIZ' : (/demo/i.test(task) ? 'DEMO' : 'CLASS');
    return `<div class="card ${k} c-${c.cls}"><div class="time">${splitTime(time)}</div><div class="body"><span class="pill">${c.label}</span><span class="pill p-${k}">${lab}</span><div class="task">${esc(task)}</div></div><div class="box ghost"></div></div>`;
  }
  return `<div class="card c-${c.cls}"><div class="time">${splitTime(time)}</div><div class="body"><span class="pill">${c.label}</span><div class="task">${esc(task)}</div>${check ? `<div class="done"><b>DONE WHEN</b>${esc(check)}</div>` : ''}</div><div class="box"></div></div>`;
}

function renderDay(day, i) {
  const meta = META[day.d] || { day: day.d, n: '', badge: '', one: '' };
  const study = day.r.filter(r => kind(r) === 'study');
  const helpers = [...new Set(study.map(r => (COURSE[r[1]] || {}).helper).filter(Boolean))];
  const squares = study.map(() => '<i></i>').join('');
  const label = `DAY ${String(i + 1).padStart(2, '0')} OF ${DAYS.length}`;
  return `
<section class="day" id="day-${i}">
  <h2 class="sr">${esc(meta.day)} ${esc(meta.n)} November</h2>
  <div class="dhead">
    <div>
      <div class="dnum">${label}</div>
      <div class="dname">${esc(meta.day.toUpperCase())} <em>${esc(meta.n)}</em></div>
      <div class="dmonth">NOVEMBER 2026</div>
    </div>
    <div class="dright">
      <div class="badge">${esc(meta.badge)}</div>
      <div class="tally"><span>${study.length} boxes today</span><div class="sq">${squares}</div></div>
    </div>
  </div>
  <div class="one"><span>TODAY'S ONE THING</span>${esc(meta.one)}</div>
  <div class="focus"><b>Phone in another room</b><b>Timer on</b><b>One box at a time</b><b>Tick only when "done when" is true</b></div>
  ${EXTRA[day.d] || ''}
  <div class="rows">${day.r.map(renderRow).join('\n')}</div>
  <div class="foot">
    <div class="park"><div class="plabel">PARKING LOT <span>a stray thought? write it here, then go straight back to the box</span></div></div>
    <div class="stuck"><b>Stuck for 10 minutes?</b> Circle the step, move to the next one, and ask after the block. Today's Claude sessions: ${helpers.map(h => `<span class="chip">${esc(h)}</span>`).join(' ') || '<span class="chip">none needed</span>'}</div>
  </div>
</section>`;
}

const dayTiles = DAYS.map((d, i) => {
  const meta = META[d.d] || { day: d.d, n: '' };
  const key = `DAY ${String(i + 1).padStart(2, '0')} OF ${DAYS.length}`;
  const exam = d.r.some(r => r[1] === 'EXAM');
  return `<a class="tile${exam ? ' t-exam' : ''}" href="#day-${i}"><span>${esc(meta.day.slice(0, 3).toUpperCase())}</span><b>${esc(meta.n)}</b><em>${pg(key)}</em></a>`;
}).join('');

const CHEATS = [
  { id: 'em', key: 'CHEAT EM', name: 'Engineering Management', sub: 'Midterm Sun 8 Nov, 15:00-17:00 · Quiz 2, case study, presentations after midterms', body: `
<div class="blk"><h4>Productivity</h4>
<div class="f">Productivity = Output / Input</div>
<div class="f">Labour productivity = Output / Labour hours</div>
<div class="f">MFP = Output / (Labour + Materials + Overhead + Energy ...) in money</div>
<div class="f">Growth % = (This period - Last period) / Last period x 100</div></div>
<div class="blk"><h4>Forecasting</h4>
<div class="f">Naive: F(t) = A(t-1)</div>
<div class="f">Moving average: F(t) = (A(t-1) + ... + A(t-n)) / n</div>
<div class="f">Weighted MA: F(t) = sum of w x A, weights add to 1</div>
<div class="f">Exp. smoothing: F(t) = F(t-1) + alpha [A(t-1) - F(t-1)]</div>
<div class="f">Trend: F(t) = a + b t</div>
<div class="f">b = (n Sum ty - Sum t Sum y) / (n Sum t&sup2; - (Sum t)&sup2;)</div>
<div class="f">a = (Sum y - b Sum t) / n</div>
<div class="f">e = A - F &nbsp; MAD = Sum|e| / n</div>
<div class="f">MSE = Sum e&sup2; / (n - 1) &nbsp;(your slides use n - 1)</div>
<div class="f">MAPE = Sum(|e| / A x 100) / n</div>
<p>Lower MAD, MSE or MAPE = the more accurate method.</p></div>
<div class="blk"><h4>Capacity</h4>
<div class="f">Efficiency = Actual output / Effective capacity</div>
<div class="f">Utilization = Actual output / Design capacity</div>
<div class="f">Machines = Sum(Demand x Time per unit) / Hours per machine per year &rarr; ROUND UP</div>
<p>Design &ge; Effective &ge; Actual.</p></div>
<div class="blk"><h4>Cost-volume and make/buy</h4>
<div class="f">TC = FC + vQ &nbsp; TR = RQ</div>
<div class="f">Profit P = Q(R - v) - FC</div>
<div class="f">Break-even Q = FC / (R - v)</div>
<div class="f">Q for target profit = (P + FC) / (R - v)</div>
<div class="f">Price for target profit = (P + FC) / Q + v</div>
<div class="f">Make vs buy: Q = FC / (Buy price - v) &rarr; above: make, below: buy</div>
<div class="f">Two options: Q = (FC_A - FC_B) / (v_B - v_A)</div></div>
<div class="blk"><h4>Theory lists</h4>
<p><b>8 determinants:</b> facilities, product/service, process, human, policy, operational, supply chain, external.</p>
<p><b>8 planning steps:</b> estimate requirements · evaluate existing capacity and gaps · identify alternatives · financial analysis · qualitative issues · select the best · implement · monitor.</p>
<p><b>3 strategies:</b> leading (build ahead of demand) · following (build after demand exceeds capacity) · tracking (small steps).</p></div>
<div class="blk trap"><h4>MCQ traps</h4>
<p>Effective vs design in the denominator. Machines always round UP. It is R - v, not R + v. Percent vs decimal. MSE divides by n - 1 in your slides. At break-even TR = TC.</p></div>` },
  { id: 'ai', key: 'CHEAT AI', name: 'AI and Expert System', sub: 'Midterm Sun 8 Nov, 09:00-11:00 (Ch 1-3) · Lab test Thu 5 Nov, 15:00', body: `
<div class="blk"><h4>Ch 1-2 lists</h4>
<p><b>4 approaches:</b> thinking humanly · thinking rationally · acting humanly (Turing test) · acting rationally (rational agent).</p>
<p><b>PEAS:</b> Performance measure, Environment, Actuators, Sensors.</p>
<p><b>Environment pairs:</b> fully / partially observable · single / multi-agent · deterministic / stochastic · episodic / sequential · static / dynamic · discrete / continuous.</p>
<p><b>Agents:</b> simple reflex &rarr; model-based reflex &rarr; goal-based &rarr; utility-based, plus the learning agent.</p>
<p><b>A problem has 5 parts:</b> initial state, actions, transition model, goal test, path cost.</p></div>
<div class="blk trap"><h4>Exam traps</h4>
<p>UCS tests the goal when a node is popped, not when it is generated. Expand children left first (your class order). Graph search keeps an explored (closed) set. Bidirectional is b<sup>d/2</sup>, not b<sup>d</sup>/2.</p>
<p>Tree vs graph search: graph search never re-expands a state already in the explored set.</p></div>
<div class="blk wide"><h4>Uninformed search</h4>
<table class="t"><tr><th></th><th>BFS</th><th>UCS</th><th>DFS</th><th>DLS</th><th>IDS</th><th>Bidirectional</th></tr>
<tr><th>Complete</th><td>Yes</td><td>Yes*</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td></tr>
<tr><th>Optimal</th><td>Yes**</td><td>Yes</td><td>No</td><td>No</td><td>Yes**</td><td>Yes**</td></tr>
<tr><th>Time</th><td>b<sup>d</sup></td><td>b<sup>1+C*/&epsilon;</sup></td><td>b<sup>m</sup></td><td>b<sup>l</sup></td><td>b<sup>d</sup></td><td>b<sup>d/2</sup></td></tr>
<tr><th>Space</th><td>b<sup>d</sup></td><td>b<sup>1+C*/&epsilon;</sup></td><td>bm</td><td>bl</td><td>bd</td><td>b<sup>d/2</sup></td></tr></table>
<p class="small">All are O(...). * if every step cost &ge; &epsilon; &gt; 0. ** if all step costs are equal. b = branching factor, d = goal depth, m = max depth, l = depth limit.</p></div>
<div class="blk"><h4>Informed search</h4>
<div class="f">Greedy best-first: f(n) = h(n) &nbsp;(not optimal)</div>
<div class="f">A*: f(n) = g(n) + h(n)</div>
<div class="f">Admissible: h(n) &le; h*(n) &nbsp;(never overestimates)</div>
<div class="f">Consistent: h(n) &le; c(n, n') + h(n')</div>
<p>Consistent &rArr; admissible. A* is optimal with an admissible h (tree search) or a consistent h (graph search).</p></div>
<div class="blk"><h4>Lab test (Python)</h4>
<div class="f">stack: s.append(x); s.pop()</div>
<div class="f">queue: q.append(x); q.pop(0)</div>
<div class="f">count: d[k] = d.get(k, 0) + 1</div>
<div class="f">unique: set(words) &nbsp; reverse: L[::-1]</div>
<div class="f">evens = [x for x in L if x % 2 == 0]</div>
<div class="f">print(f"{total:.2f}")</div></div>` },
  { id: 'mis', key: 'CHEAT MIS', name: 'Management Information Systems', sub: 'Midterm Tue 10 Nov, 09:00-11:00 · Assignment 1 due Fri 6 Nov, 23:00', body: `
<div class="blk"><h4>Ch 1 · Information systems</h4>
<p><b>IS:</b> components that collect, process, store and distribute information to support decisions, coordination and control.</p>
<p><b>3 dimensions:</b> organization, management, technology. Data &rarr; information &rarr; knowledge.</p>
<p><b>6 business objectives:</b> operational excellence · new products, services and business models · customer and supplier intimacy · improved decision making · competitive advantage · survival.</p></div>
<div class="blk"><h4>Ch 2 · Systems by level</h4>
<p><b>TPS</b> operational managers, daily transactions · <b>MIS</b> middle managers, routine reports · <b>DSS</b> middle managers, non-routine decisions · <b>ESS</b> senior managers, strategy.</p>
<p><b>Enterprise apps:</b> ERP · SCM · CRM · KMS.</p></div>
<div class="blk"><h4>Ch 3 · Competitive advantage</h4>
<p><b>5 forces:</b> traditional competitors · new market entrants · substitute products and services · customers · suppliers.</p>
<p><b>4 strategies:</b> low-cost leadership · product differentiation · focus on market niche · customer and supplier intimacy.</p>
<p><b>Value chain:</b> primary (inbound logistics, operations, outbound logistics, sales and marketing, service) and support (infrastructure, HR, technology, procurement). Value web = network of firms.</p></div>
<div class="blk"><h4>Ch 5 · IT infrastructure</h4>
<p><b>7 components:</b> hardware platforms · OS platforms · enterprise software · data management and storage · networking/telecom · internet platforms · consulting and integration services.</p>
<p><b>Drivers:</b> Moore's law · digital storage · Metcalfe's law · falling communication costs · standards. <b>Cloud:</b> IaaS · PaaS · SaaS; public · private · hybrid.</p></div>
<div class="blk"><h4>Ch 6 · Databases</h4>
<p><b>File problems:</b> redundancy and inconsistency · program-data dependence · inflexibility · poor security · little sharing.</p>
<p>Primary key = unique row ID. Foreign key = links tables. Normalization · ERD · data warehouse · OLAP · data mining. <b>Blockchain:</b> shared ledger of hash-linked blocks agreed by consensus.</p></div>
<div class="blk"><h4>Ch 7 and Ch 9</h4>
<p>LAN / MAN / WAN · client/server · packet switching · TCP/IP · DNS · Wi-Fi vs Bluetooth · RFID.</p>
<p><b>ERP:</b> one database across functions. <b>SCM:</b> bullwhip effect, push (build-to-stock) vs pull (build-to-order), JIT. <b>CRM:</b> operational vs analytical.</p></div>
<div class="blk trap"><h4>Long answer recipe (five forces)</h4>
<p>Name the company &rarr; each force: strong or low + one reason &rarr; draw the diagram &rarr; one IS-based strategy per force &rarr; one-line conclusion.</p></div>` },
  { id: 'oop', key: 'CHEAT OOP2', name: 'OOP2 (C#)', sub: 'Midterm Sun 15 Nov, 12:00-14:00 · Quiz 2 Wed 18 Nov (inheritance, polymorphism)', body: `
<div class="blk"><h4>The C# words</h4>
<p><code>class B : A</code> = B inherits A &nbsp; <code>: base(...)</code> = run A's constructor first &nbsp; <code>base.M()</code> = A's version &nbsp; <code>sealed</code> = no more inheriting</p>
<p>Methods are NOT virtual unless marked <code>virtual</code>, and the child must write <code>override</code>.</p></div>
<div class="blk"><h4>Also know</h4>
<p><b>Overloading:</b> same name, different parameters, decided at compile time. <b>Overriding:</b> same signature, virtual/override, decided at run time.</p>
<p><b>Casting:</b> upcast is automatic (<code>Animal a = dog;</code>); downcast needs <code>(Dog)a</code>, <code>as</code> or <code>is</code>.</p>
<p><b>Access:</b> private (class only) · protected (class + children) · public.</p></div>
<div class="blk wide"><h4>The pattern</h4>
<pre>class Animal {
    protected string name;
    public Animal(string n) { name = n; Console.WriteLine("Animal ctor"); }
    public virtual void Speak() { Console.WriteLine("..."); }
}
class Dog : Animal {
    public Dog(string n) : base(n) { Console.WriteLine("Dog ctor"); }
    public override void Speak() { Console.WriteLine("Woof"); }
}</pre>
<p><code>new Dog("Rex")</code> prints <b>Animal ctor</b> then <b>Dog ctor</b>: the parent's constructor always runs first.</p></div>
<div class="blk"><h4>Which method runs?</h4>
<div class="f">Animal a = new Dog("Rex"); a.Speak();</div>
<p><b>virtual + override</b> &rarr; the object's version (Dog): "Woof".</p>
<p><b>new (hiding) or not virtual</b> &rarr; the variable's type (Animal).</p>
<p><b>base.Speak()</b> inside Dog &rarr; Animal's version.</p></div>
<div class="blk trap"><h4>Won't compile</h4>
<p>override on a non-virtual method · <code>new</code> on an abstract class · an abstract method with a body · a non-abstract child that skips an abstract method · inheriting a sealed class · a Dog-only method called through an Animal variable · no <code>: base(...)</code> when the parent has no parameterless constructor · two base classes.</p>
<p class="small">Hiding without the <code>new</code> keyword is only a warning: it still compiles.</p></div>
<div class="blk"><h4>Quiz 2 pages</h4><p><code>F:\\outputs\\aiub-oop2\\OOP2-Quiz2-90-Minutes.pdf</code> (19 pages, plain C#). The 53-page booklet is reference only.</p></div>` },
  { id: 'py', key: 'CHEAT PYTHON', name: 'Programming in Python', sub: 'No midterm exam · Project email Sat 14 Nov (deadline Sun 15) · Demo Mon 16 Nov · Quiz 2 after midterms', body: `
<div class="blk wide"><h4>Project rubric (40 marks)</h4>
<table class="t"><tr><th>Problem overview and design</th><td>4</td><th>Data structures</th><td>5</td></tr>
<tr><th>User interaction and interface</th><td>5</td><th>File handling</th><td>4</td></tr>
<tr><th>Variables, operators, conditionals, loops</th><td>4</td><th>Exceptions and validation</th><td>3</td></tr>
<tr><th>Functions and modularity</th><td>4</td><th>OOP</th><td>5</td></tr>
<tr><th>Library use and analysis</th><td>4</td><th>Code quality, report, presentation</th><td>2</td></tr></table></div>
<div class="blk"><h4>Must be in the code</h4>
<p>At least 5 functions · at least 1 class · a list, tuple, set and dict, each with a purpose · save and load from a file · try/except for the 6 error cases · one approved library: NumPy, Tkinter or Pygame.</p></div>
<div class="blk trap"><h4>Submission (penalty if wrong)</h4>
<p>Email the .py files, data files and the report PDF (5 pages max).</p>
<div class="f">22-xxxx-3_23-xxxx-2_21-xxxx-1_mid-term_project.pdf</div>
<p>Subject = the same text without .pdf. Use your group's real IDs.</p></div>
<div class="blk"><h4>Quiz 2 syntax</h4>
<div class="f">class B(A): def __init__(self, x): super().__init__(x)</div>
<div class="f">try: ... except ValueError: ... else: ... finally: ...</div>
<p>else runs only if no exception; finally always runs.</p>
<div class="f">with open("f.txt", "r" | "w" | "a" | "x") as f:</div>
<p>r: missing file &rarr; FileNotFoundError · w: overwrites · a: appends · x: fails if the file exists.</p>
<div class="f">a = np.array([[1,2],[3,4]]); a.shape; a.reshape(4, 1)</div>
<p>A slice is a view (changes the original); <code>.copy()</code> is independent. Iterate with <code>for x in np.nditer(a):</code></p></div>` }
];

const cheatTiles = CHEATS.map(c => `<a class="ctile c-${c.id}" href="#cheat-${c.id}"><b>${esc(c.name)}</b><em>${pg(c.key)}</em></a>`).join('');

const cheatPages = CHEATS.map(c => `
<section class="cheat c-${c.id}" id="cheat-${c.id}">
  <h2 class="sr">${esc(c.name)} cheat sheet</h2>
  <div class="chead"><div class="ckey">${c.key}</div><div class="cname">${esc(c.name)}</div><div class="csub">${esc(c.sub)}</div></div>
  <div class="cbody">${c.body}</div>
</section>`).join('\n');

const css = `
@font-face { font-family: "Bahn"; src: url("file:///C:/Windows/Fonts/bahnschrift.ttf"); font-weight: 300 700; font-stretch: 75% 100%; }
:root {
  --ink: #15151b; --muted: #6b6b76; --line: #e6e3dc; --soft: #f7f5f0; --gold: #facc15;
  --em: #2563eb; --ai: #7c3aed; --mis: #ea580c; --oop: #059669; --py: #b7791f; --exam: #dc2626; --adm: #6b7280;
  --em-t: #eaf1ff; --ai-t: #f2ecff; --mis-t: #fff0e6; --oop-t: #e6f6ef; --py-t: #fbf3dc; --exam-t: #fdecec; --adm-t: #f1f2f4;
}
@page { size: A4; margin: 11mm 12mm 13mm;
  @bottom-left { content: "MIDTERM MODE  ·  open today's page, do the next box"; font: 7pt "Segoe UI"; color: #a3a3ab; }
  @bottom-right { content: "p. " counter(page); font: 600 8pt "Segoe UI"; color: #8a8a93; } }
@page cover { margin: 0; @bottom-left { content: none; } @bottom-right { content: none; } }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { margin: 0; font: 9.4pt/1.36 "Segoe UI", sans-serif; color: var(--ink); }
.d, .dname, .badge, .cname, .tile b, .time, .bigt, .rule b, .step b, h3 { font-family: "Bahn", "Segoe UI", sans-serif; font-stretch: 75%; font-weight: 700; }
.sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); margin: 0; }
code, pre, .f { font-family: "Cascadia Mono", Consolas, monospace; }
a { color: inherit; text-decoration: none; }

/* cover */
.cover { page: cover; width: 210mm; height: 297mm; background: var(--ink); color: #fff; padding: 20mm 18mm 16mm; position: relative; overflow: hidden; break-after: page; }
.spines { position: absolute; right: 0; top: 0; bottom: 0; display: flex; }
.spines i { width: 5mm; height: 100%; display: block; }
.kicker { font: 600 8.5pt "Segoe UI"; letter-spacing: .32em; color: #b9b9c4; }
.bigt { font-size: 96pt; line-height: .82; margin: 8mm 0 0; letter-spacing: -.01em; }
.bigt span { color: var(--gold); display: block; }
.lede { font-size: 14pt; margin: 7mm 0 10mm; color: #e8e8ee; max-width: 150mm; }
.lede b { color: var(--gold); }
.xgrid { display: grid; grid-template-columns: 1fr 1fr; gap: 4mm; width: 160mm; }
.xt { padding: 5mm 5.5mm; border-radius: 3mm; }
.xt .k { font: 700 8pt "Segoe UI"; letter-spacing: .2em; opacity: .9; }
.xt .w { font-family: "Bahn"; font-stretch: 75%; font-weight: 700; font-size: 26pt; line-height: 1; margin-top: 2mm; }
.xt .h { font-size: 11pt; margin-top: 1mm; opacity: .95; }
.pystrip { width: 160mm; margin-top: 4mm; border: .5mm solid var(--py); color: #f5d98b; border-radius: 3mm; padding: 3mm 5mm; font-size: 10pt; }
.rules { position: absolute; left: 18mm; right: 30mm; bottom: 16mm; }
.rules h3 { font-size: 15pt; letter-spacing: .06em; color: var(--gold); margin: 0 0 3mm; }
.rule { display: grid; grid-template-columns: 11mm 1fr; align-items: baseline; font-size: 13pt; margin: 2mm 0; }
.rule b { font-size: 26pt; color: var(--gold); line-height: 1; }
.only { margin-top: 5mm; font: 600 10pt "Segoe UI"; color: #b9b9c4; letter-spacing: .04em; }

/* how-to page */
.howto h1 { font-family: "Bahn"; font-stretch: 75%; font-size: 30pt; margin: 0 0 1mm; letter-spacing: .01em; }
.howto .sub { color: var(--muted); margin: 0 0 5mm; }
.steps { display: grid; grid-template-columns: repeat(4, 1fr); gap: 3mm; margin-bottom: 6mm; }
.step { border: 1px solid var(--line); border-radius: 3mm; padding: 4mm; background: var(--soft); }
.step b { display: block; font-size: 30pt; line-height: 1; color: var(--exam); }
.step p { margin: 2mm 0 0; font-weight: 600; }
.trio { display: grid; grid-template-columns: repeat(3, 1fr); gap: 3mm; margin-bottom: 6mm; }
.tri { border-left: 1.6mm solid var(--ink); padding: 1mm 0 1mm 3.5mm; }
.tri h3 { margin: 0 0 1mm; font-size: 14pt; }
.tri p { margin: 0; font-size: 9pt; }
.howto h2.sec { font-family: "Bahn"; font-stretch: 75%; font-size: 15pt; letter-spacing: .06em; margin: 0 0 2.5mm; }
.tiles { display: grid; grid-template-columns: repeat(7, 1fr); gap: 2mm; margin-bottom: 6mm; }
.tile { border: 1px solid var(--line); border-radius: 2.5mm; padding: 2mm 2.5mm; text-align: center; background: #fff; }
.tile span { display: block; font: 700 7pt "Segoe UI"; letter-spacing: .15em; color: var(--muted); }
.tile b { display: block; font-size: 22pt; line-height: 1.05; }
.tile em { font: italic 600 8pt "Segoe UI"; color: var(--muted); }
.tile.t-exam { border-color: var(--exam); background: var(--exam-t); }
.tile.t-exam b { color: var(--exam); }
.ctiles { display: grid; grid-template-columns: repeat(5, 1fr); gap: 2mm; margin-bottom: 6mm; }
.ctile { border-radius: 2.5mm; padding: 3mm; color: #fff; }
.ctile b { display: block; font-size: 9.5pt; line-height: 1.2; }
.ctile em { font: italic 600 8pt "Segoe UI"; opacity: .9; }
.ctile.c-em { background: var(--em); } .ctile.c-ai { background: var(--ai); } .ctile.c-mis { background: var(--mis); } .ctile.c-oop { background: var(--oop); } .ctile.c-py { background: var(--py); }
.where { display: grid; grid-template-columns: 1fr 1fr; gap: 3mm 6mm; font-size: 8.6pt; }
.where div { border-top: 1px solid var(--line); padding-top: 1.5mm; }
.where b { display: block; font-size: 8pt; letter-spacing: .08em; text-transform: uppercase; color: var(--muted); }

/* day pages */
.day { break-before: page; }
.dhead { display: flex; justify-content: space-between; align-items: flex-end; border-bottom: 1.3mm solid var(--ink); padding-bottom: 2mm; margin-bottom: 3mm; }
.dnum { font: 700 7.5pt "Segoe UI"; letter-spacing: .25em; color: var(--muted); }
.dname { font-size: 36pt; line-height: .95; letter-spacing: .01em; }
.dname em { font-style: normal; color: var(--exam); }
.dmonth { font: 700 7.5pt "Segoe UI"; letter-spacing: .3em; color: var(--muted); }
.dright { text-align: right; }
.badge { display: inline-block; background: var(--exam); color: #fff; font-size: 12.5pt; padding: 1.4mm 3.5mm; border-radius: 1.6mm; text-transform: uppercase; letter-spacing: .03em; }
.tally { margin-top: 2mm; font: 600 8pt "Segoe UI"; color: var(--muted); }
.tally .sq { display: flex; gap: 1.2mm; justify-content: flex-end; margin-top: 1mm; flex-wrap: wrap; max-width: 80mm; margin-left: auto; }
.tally .sq i { width: 3.6mm; height: 3.6mm; border: .45mm solid var(--ink); border-radius: .8mm; display: block; }
.one { background: var(--ink); color: #fff; padding: 3mm 4.5mm; border-radius: 2.5mm; font-size: 12.5pt; font-weight: 600; margin-bottom: 2mm; }
.one span { display: block; font: 700 7.5pt "Segoe UI"; letter-spacing: .25em; color: var(--gold); margin-bottom: .6mm; }
.focus { display: flex; flex-wrap: wrap; gap: 1.6mm; margin-bottom: 3mm; }
.focus b { font: 700 7pt "Segoe UI"; letter-spacing: .08em; text-transform: uppercase; border: .35mm solid var(--ink); border-radius: 10mm; padding: .6mm 2.4mm; }
.callout { border-radius: 2mm; padding: 2.2mm 3.2mm; margin-bottom: 3mm; font-size: 8.8pt; border-left: 1.6mm solid; }
.callout.oop { background: var(--oop-t); border-color: var(--oop); }
.callout.em { background: var(--em-t); border-color: var(--em); }
.callout code { font-size: 8pt; }
.card { display: grid; grid-template-columns: 19mm 1fr 8mm; gap: 3mm; align-items: start; padding: 2.1mm 3mm; border: 1px solid var(--line); border-left: 2.2mm solid var(--c); border-radius: 2.4mm; margin-bottom: 1.6mm; break-inside: avoid; background: #fff; }
.time { font-size: 16pt; line-height: 1; color: var(--c); }
.time span { display: block; font: 600 7.5pt "Segoe UI"; color: var(--muted); margin-top: .8mm; }
.pill { display: inline-block; font: 700 6.8pt "Segoe UI"; letter-spacing: .12em; color: #fff; background: var(--c); padding: .4mm 2mm; border-radius: 1mm; margin: 0 1.2mm .9mm 0; }
.task { font-weight: 600; font-size: 9.4pt; }
.done { margin-top: 1.1mm; background: var(--t); border-radius: 1.2mm; padding: 1mm 2.2mm; font-size: 8.4pt; }
.done b { font: 700 6.6pt "Segoe UI"; letter-spacing: .14em; color: var(--c); margin-right: 1.8mm; }
.box { width: 7mm; height: 7mm; border: .55mm solid var(--ink); border-radius: 1.3mm; align-self: center; }
.box.ghost { border: none; }
.card.class { border: 1px dashed #a8a8b0; border-left: 2.2mm solid #a8a8b0; background: var(--soft); }
.card.class .time { color: #7a7a84; }
.card.quiz { border: .55mm solid var(--exam); border-left: 2.2mm solid var(--exam); background: var(--exam-t); }
.card.quiz .time { color: var(--exam); }
.pill.p-quiz { background: var(--exam); }
.pill.p-class { background: #7a7a84; }
.c-em { --c: var(--em); --t: var(--em-t); } .c-ai { --c: var(--ai); --t: var(--ai-t); } .c-mis { --c: var(--mis); --t: var(--mis-t); }
.c-oop { --c: var(--oop); --t: var(--oop-t); } .c-py { --c: var(--py); --t: var(--py-t); } .c-adm { --c: var(--adm); --t: var(--adm-t); } .c-exam { --c: var(--exam); --t: var(--exam-t); }
.exam.card-x { display: grid; grid-template-columns: 19mm 1fr 14mm; gap: 3mm; align-items: center; background: var(--exam); color: #fff; border-radius: 2.4mm; padding: 3.2mm 3mm; margin: 2.4mm 0; break-inside: avoid; }
.exam .time { color: #fff; font-size: 18pt; }
.exam .time span { color: #ffd6d6; }
.etxt { font-size: 12pt; font-weight: 700; }
.xlabel { display: inline-block; background: #fff; color: var(--exam); font: 700 7pt "Segoe UI"; letter-spacing: .16em; padding: .5mm 2mm; border-radius: 1mm; margin-right: 2.5mm; vertical-align: middle; }
.xbadge { font-family: "Bahn"; font-stretch: 75%; font-weight: 700; font-size: 18pt; text-align: center; border: .6mm solid #fff; border-radius: 2mm; padding: .5mm 0; }
.rest { display: flex; gap: 3mm; align-items: center; font-size: 8pt; color: var(--muted); margin: 1.2mm 0 2mm; padding-left: 3mm; }
.rest span { font-weight: 700; min-width: 19mm; }
.rest::after { content: ""; flex: 1; border-top: 1px dotted #c9c6bf; }
.foot { margin-top: 3mm; break-inside: avoid; }
.park { border: 1px solid var(--line); border-radius: 2.4mm; height: 24mm; padding: 2mm 3mm; background: repeating-linear-gradient(to bottom, #fff 0, #fff 6.3mm, #ece9e2 6.3mm, #ece9e2 6.6mm); }
.plabel { font: 700 7.5pt "Segoe UI"; letter-spacing: .2em; }
.plabel span { font-weight: 400; letter-spacing: .02em; color: var(--muted); margin-left: 2mm; }
.stuck { margin-top: 2mm; font-size: 8.4pt; }
.chip { display: inline-block; font: 600 7.4pt "Segoe UI"; border: 1px solid var(--line); background: var(--soft); border-radius: 10mm; padding: .3mm 2.2mm; margin: .6mm .6mm 0 0; }

/* cheat sheets */
.cheat { break-before: page; }
.chead { background: var(--c); color: #fff; border-radius: 3mm; padding: 5mm 6mm; margin-bottom: 4mm; }
.ckey { font: 700 7.5pt "Segoe UI"; letter-spacing: .3em; opacity: .85; }
.cname { font-size: 30pt; line-height: 1; margin-top: 1mm; }
.csub { font-size: 9.5pt; margin-top: 1.5mm; opacity: .95; }
.cbody { column-count: 2; column-gap: 5mm; }
.blk { break-inside: avoid; border: 1px solid var(--line); border-radius: 2.4mm; padding: 2.6mm 3mm; margin: 0 0 3mm; background: #fff; }
.blk.wide { column-span: all; }
.blk h4 { margin: 0 0 1.4mm; font-family: "Bahn"; font-stretch: 75%; font-weight: 700; font-size: 12.5pt; color: var(--c); text-transform: uppercase; letter-spacing: .04em; }
.blk p { margin: 1mm 0; font-size: 8.7pt; }
.blk .f { background: var(--t); border-radius: 1.2mm; padding: .9mm 2mm; margin: .9mm 0; font-size: 8.1pt; }
.blk.trap { border: .5mm solid var(--exam); background: var(--exam-t); }
.blk.trap h4 { color: var(--exam); }
.small { font-size: 7.6pt !important; color: var(--muted); }
pre { background: var(--t); border-radius: 1.6mm; padding: 2.4mm 3mm; font-size: 8pt; line-height: 1.4; margin: 1mm 0 1.6mm; white-space: pre; }
table.t { width: 100%; border-collapse: collapse; font-size: 8.4pt; margin: 1mm 0; }
table.t th, table.t td { border-bottom: 1px solid var(--line); padding: 1.1mm 1.6mm; text-align: left; }
table.t th { font-weight: 600; color: var(--ink); background: var(--soft); }
table.t td { font-family: "Cascadia Mono", Consolas, monospace; }

/* exam day */
.examday { break-before: page; }
.examday .chead { background: var(--exam); }
.ck { display: grid; grid-template-columns: 9mm 1fr; gap: 3mm; align-items: center; padding: 2.4mm 0; border-bottom: 1px solid var(--line); font-size: 11pt; font-weight: 600; }
.ck i { width: 7mm; height: 7mm; border: .55mm solid var(--ink); border-radius: 1.3mm; display: block; }
.ck small { display: block; font-weight: 400; font-size: 8.8pt; color: var(--muted); }
.two { display: grid; grid-template-columns: 1fr 1fr; gap: 8mm; }
.two h3 { font-size: 16pt; margin: 0 0 1mm; letter-spacing: .04em; }
`;

const spines = ['--em', '--ai', '--mis', '--oop', '--py'].map(v => `<i style="background: var(${v})"></i>`).join('');

const html = `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Midterm Mode: Fall 2026-27 study guide</title><style>${css}</style></head>
<body>
<section class="cover">
  <div class="spines">${spines}</div>
  <div class="kicker">AIUB · FALL 2026-27 · NOV 3 TO NOV 16</div>
  <h2 class="sr">Cover</h2>
  <div class="bigt">MIDTERM<span>MODE</span></div>
  <div class="lede">One guide. <b>Open today's page. Do the next box.</b> No new plans, no re-planning: the planning is finished.</div>
  <div class="xgrid">
    <div class="xt" style="background: var(--ai)"><div class="k">AI AND EXPERT SYSTEM</div><div class="w">SUN 8 NOV</div><div class="h">09:00 to 11:00</div></div>
    <div class="xt" style="background: var(--em)"><div class="k">ENGINEERING MANAGEMENT</div><div class="w">SUN 8 NOV</div><div class="h">15:00 to 17:00</div></div>
    <div class="xt" style="background: var(--mis)"><div class="k">MANAGEMENT INFO SYSTEMS</div><div class="w">TUE 10 NOV</div><div class="h">09:00 to 11:00</div></div>
    <div class="xt" style="background: var(--oop)"><div class="k">OOP2 (C#)</div><div class="w">SUN 15 NOV</div><div class="h">12:00 to 14:00</div></div>
  </div>
  <div class="pystrip"><b>PYTHON</b> has no exam: project email Sat 14 Nov, demo Mon 16 Nov. Before that: OOP2 + EM quizzes Wed 4 Nov, AI lab test Thu 5 Nov, MIS assignment Fri 6 Nov.</div>
  <div class="rules">
    <h3>THE ONLY THREE RULES</h3>
    <div class="rule"><b>1</b><span>When your calendar pops up, open today's page.</span></div>
    <div class="rule"><b>2</b><span>Phone in another room, timer on, do the next empty box.</span></div>
    <div class="rule"><b>3</b><span>Tick it only when its "done when" line is true. Then the next one.</span></div>
    <div class="only">This is the only plan. Don't make another one.</div>
  </div>
</section>

<section class="howto">
  <h2 class="sr">How this works</h2>
  <h1>HOW THIS WORKS</h1>
  <p class="sub">Every day has its own page. Every box is one block of study with a clear finish line.</p>
  <div class="steps">
    <div class="step"><b>1</b><p>Calendar pops up. Open today's page.</p></div>
    <div class="step"><b>2</b><p>Phone away. Start a timer for the block.</p></div>
    <div class="step"><b>3</b><p>Do the box. Check its "done when" line.</p></div>
    <div class="step"><b>4</b><p>Tick. 10-minute break. Next box.</p></div>
  </div>
  <div class="trio">
    <div class="tri"><h3>MIND DRIFTING?</h3><p>Write the thought in the parking lot at the bottom of the page. Say the box's task out loud. Restart the timer for just 10 minutes.</p></div>
    <div class="tri"><h3>STUCK?</h3><p>10 minutes on one step is the limit. Circle it, do the next step, and ask that course's Claude session after the block.</p></div>
    <div class="tri"><h3>MISSED A BLOCK?</h3><p>Don't start over and don't catch up now. Jump to the box for the current time. The 22:51 check-in moves what you missed.</p></div>
  </div>
  <h2 class="sec">FIND YOUR DAY</h2>
  <div class="tiles">${dayTiles}</div>
  <h2 class="sec">CHEAT SHEETS</h2>
  <div class="ctiles">${cheatTiles}</div>
  <h2 class="sec">WHERE EVERYTHING IS</h2>
  <div class="where">
    <div><b>Course files</b>D:\\Personal\\Downloads\\AIUB &lt;course&gt; Notes\\</div>
    <div><b>AI notes</b>F:\\outputs\\ai-midterm\\AI-Midterm-Study-Notes-Ch1-3.pdf</div>
    <div><b>OOP2 Quiz 2 (19 pages)</b>F:\\outputs\\aiub-oop2\\OOP2-Quiz2-90-Minutes.pdf</div>
    <div><b>OOP2 slides and code</b>Slides.zip and Codes.zip on your Desktop (unzip Wed 11 Nov)</div>
    <div><b>Plan with tick boxes</b>F:\\outputs\\midterm-plan\\Midterm-Study-Plan.html</div>
    <div><b>Claude sessions</b>Engineering Management · AI mid note · Management Information Systems · Object-Oriented Programming 2 · Programming in Python</div>
  </div>
</section>

${DAYS.map(renderDay).join('\n')}

${cheatPages}

<section class="examday c-exam">
  <h2 class="sr">Exam day checklist</h2>
  <div class="chead"><div class="ckey">EXAM DAY</div><div class="cname">Exam morning checklist</div><div class="csub">AI and EM Sun 8 Nov · MIS Tue 10 Nov · OOP2 Sun 15 Nov · venue: AIUB, All Annexes</div></div>
  <div class="two">
    <div>
      <h3>BEFORE YOU LEAVE</h3>
      <div class="ck"><i></i><span>Exam permit<small>No permit, no exam.</small></span></div>
      <div class="ck"><i></i><span>Two pens, pencil, eraser</span></div>
      <div class="ck"><i></i><span>Calculator<small>EM especially.</small></span></div>
      <div class="ck"><i></i><span>Watch and water</span></div>
      <div class="ck"><i></i><span>The 30-minute exam-morning box done<small>Read only. No new material.</small></span></div>
      <div class="ck"><i></i><span>At the venue 20 minutes early</span></div>
    </div>
    <div>
      <h3>IN THE HALL</h3>
      <div class="ck"><i></i><span>Read the whole paper first (3 minutes)</span></div>
      <div class="ck"><i></i><span>Do the questions you're sure of first</span></div>
      <div class="ck"><i></i><span>Split your time by marks</span></div>
      <div class="ck"><i></i><span>Show every step of a calculation<small>Method marks count even if the final number is off.</small></span></div>
      <div class="ck"><i></i><span>Check units, rounding and percent vs decimal</span></div>
      <div class="ck"><i></i><span>Last 10 minutes: review, don't start anything new</span></div>
    </div>
  </div>
  <div class="callout em" style="margin-top: 8mm; font-size: 10pt;"><b>After the exam:</b> no post-mortem. Eat, rest 20 minutes, then open the next page of this guide.</div>
</section>
</body></html>`;

fs.writeFileSync(OUT, html, 'utf8');
console.log('days', DAYS.length, 'rows', DAYS.reduce((a, d) => a + d.r.length, 0), 'bytes', html.length);
