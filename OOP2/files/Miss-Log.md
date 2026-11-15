# Miss log

Reread this Saturday night and Sunday at 10:00. Nothing else.

| Q | You wrote | Right | Rule |
|---|---|---|---|
| Q1 | an empty line after `94` | no empty line | `WriteLine()` after `Write()` just ends that line. It makes an empty line only if the line is already empty. |
| Q1 | `49` | `4 9` | `{0}`, `{1}` = position in the list after the text, counting from 0. The space between them prints too. |
| Q2 | `error` | `67` | `(int)` on a letter gives its code. Never an error. A = 65, a = 97. |
| Q2 | `false` | `False` | A bool prints `True` / `False` with a capital. |
| Q3 | `sum = ...` after every pass | printed once, after the loop | A line is inside the loop only if it sits between the loop's `{` and its matching `}`. Match the braces before you trace. |
| Q3 | `1`, `3`, `5` on separate lines | `1 3 5` on one line | `Write` stays on the same line. Only `WriteLine` moves down. |
| Q3 | `sum = 10` | `sum = 6` | `i % 2 == 0` means even. Only even i is added (2 + 4). Odd i goes to `else` and never touches sum. Fill the table; don't guess. |
| Q5 | `6 17` (worked 14, copied 17) | `6 14` | Copying slip. Before you hand in, check every number in your final answer against your working table, line by line. |
| D1 | `using system;`, `staff` in some places | `using System;`, `Staff` every time | C# is case-sensitive. `System`, `Console`, `WriteLine` and the class name always start with a capital. |
| D1 | property `public int staffID` | `public int StaffID` | Field lowercase, property capitalized. Using the same name twice is a compile error. |
| D1 | `get { return basePay }`, `set { basePay = value }` | `return basePay;`, `basePay = value;` | Every statement ends with `;`, including inside `get { }` and `set { }`. |
| D1 | `This.name = name;` | `this.name = name;` | `this` is all lowercase. |
| D1 | parameter `int staff` | `int staffID` | The parameter must have the exact name used on the right of `this.staffID = staffID;`. Otherwise 101 is never stored and s2 prints ID 0. |
| D1 | output `Base Pay: 0.0` | `Base pay: 0` | A whole-number double prints without `.0` (`0.0` → `0`, `45000.50` → `45000.5`). Copy the label exactly as it appears inside the quotes. |
| D3 | `Console` and `courseTitle` were right but read as `console` and `CourseTitle` | clear letters | The examiner marks what they can read. Don't write over a letter. Cross it out with one line and write the word again next to it. Make capitals clearly bigger than lowercase. |
| Q8 | `AIUB`, `-1 unknown` and `7 Nila` printed as each object was made | constructors print only their own `WriteLine` text | Only `Console.WriteLine` prints. Setting a value (`uni = "AIUB"`, `id = -1`) prints nothing. Values appear only when `Show()` runs. |
| Q8 | no `copy constructor` line | `copy constructor` | `new Student(b)` passes a Student, so the copy constructor runs, and it prints too. |
| Q8 | `Show()` lines mixed in with the constructors, no `AIUB` at the end | all 4 constructor lines first, then `-1 unknown AIUB`, `7 Nila AIUB`, `7 Rafi AIUB` | Print in the order Main runs its lines. `Show()` prints `id name uni` on one line. |
| Q8 | `8 Rafi` | `7 Rafi` | A copy takes the other object's values exactly (`id = other.id`). Nothing adds 1. |
| 2.3 | `"Nila"` flows down from Person to Student | `"Nila"` goes UP: Student receives it, then `: base(name)` hands it to Person | `: base(...)` sends values from the child's constructor up to the parent's constructor. The parent's body runs first and stores them. |
| D5 | `private int playerID;` | `private string playerId;` | Take each field's type from what Main passes: in quotes (`"P-1"`) means string, a whole number means int, a number with a point means double. |
| D5 | `return False;` | `return false;` | In code, `true` and `false` are lowercase. Only the printed output shows `True` and `False`. |
| D5 | `public void Player(...)` (fixed after review) | `public Player(...)` | A constructor has no return type, not even `void`. With `void` it becomes an ordinary method and never runs on `new`. |
| D5 | In Batsman and Bowler, `}` closes ShowInfo right after the prints, so the `if/else` sits outside it | the `if/else` inside ShowInfo, with ShowInfo's `}` after the `else` block | A method's `}` goes after its LAST statement. Anything below it is outside the method and won't compile. You also did this in D1. Before you hand in, point at each `{` and find its own `}`. |
| D5 | Bowler: `public override bool` with no name | `public override bool PlayerPerformance()` | Every method header needs access, `override` or `virtual` if any, the return type, then the name and `()`. |
| D5 | AllRounder: parameter `string teamName`, but `: base(playerID, playerName, playerTeam)` | the same name in both places | `: base(...)` can only pass names from your own parameter list. Pick one name and keep it everywhere. |
| D5 | `if (PlayerPerformance)` | `if (PlayerPerformance())` | Calling a method always needs `()`. And `if` is all lowercase. |
| 3.1 quiz | no modifier on a member = public | private | A member with no modifier is `private`. A class with no modifier (not inside another class) is `internal`. |
| 3.2 quiz | const can be set in the constructor; readonly can't | the opposite | `const`: value only in its declaration, fixed forever, automatically static. `readonly`: value in its declaration OR in a constructor, then fixed. Hook: const = Carved at compile time; readonly = Ready once the constructor finishes. |
| Old A4 | `var` gets its type while running: T | F | `var` = the compiler picks the type at compile time, and it never changes. `dynamic` is the one checked while running. |
| Old A5 | jagged rows "can have a same length": F | T | Jagged rows CAN differ in length, but nothing stops them being equal. "Can" questions: if it's allowed, it's True. |
| Old A8 | `GetType()` is public in Object: F | T | Every class inherits from `System.Object`, so every object has `ToString()`, `Equals()`, `GetHashCode()`, `GetType()`, all public. |
| Q6 | rows `4.3 5.8` and `6.2 7.7` | `4.3` and `6.2 7.7 8.2` | `j < jaggedArray[i].Length - 1` uses EACH row's own length, minus 1: row 0 (3 items) prints 2, row 1 (2 items) prints 1, row 2 (4 items) prints 3. Count each row separately; it always drops just that row's last item. |
| Q6 | no empty line before `Element1: 1.5` | an empty line, then `Element1: 1.5` | `\n` inside quotes is a new line right there. `"\nElement1: "` starts by moving down one line, so a blank line appears first. |
| Q6 | `Element3:` with no value | `Element3: 9.4` | `[2][3]` = row 2, item 3, counting both from 0: row `{6.2, 7.7, 8.2, 9.4}`, item 3 = `9.4`. The loop skipping it doesn't matter; the array still holds it. |
| Q8 | `count =` blank | `count = 3` | `count` is static: one shared box. Each of the 3 `new`s runs `count++` on that same box. |
| Q33 | `string cgpa` in the Undergraduate constructor | `double cgpa` | Second time (D5 too). Main passes `3.86`, a number with a point, so it's double. Copy the parent's parameter types exactly, then add the child's own. |
| Q33 | `cgpa += 3.75 && completedCredits += 30` | `Cgpa >= 3.75 && completedCredits >= 30` | "at least" = `>=`. `+=` means "add to" and changes the value. "more than" = `>`, "at most" = `<=`. |
| Q33 | `cgpa` used inside Undergraduate | `Cgpa` (the property) | `cgpa` is private in Student, so the child can't touch it (compile error). Use the parent's public property `Cgpa`. The child's own fields (`completedCredits`) are fine. |
| Q33 | `base.ShowInfo()` | `base.ShowInfo();` | Every statement ends with `;`. |
| Q33 | `Eligible: yes` / `Eligible: No` | `Scholarship: Yes` / `Scholarship: No` | The question says exactly what to print. Copy its words. "Every point" of the scenario is marked. |
| Q33 | `return False;` | `return false;` | Second time (D5 too). In code, `false` is lowercase. |
