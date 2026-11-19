@echo off
rem Laptop side of the hub. Double-click: gets the PC's latest, then sends anything you changed here.
rem Edit files in the course folders or drop new ones in inbox\; the PC copies them over on its 3-hourly sync.
cd /d "%~dp0"
git pull -q --rebase --autostash origin main || goto :fail
rem A file changed on both machines: git reports success but leaves conflict markers, so stop before committing them.
for /f "delims=" %%f in ('git diff --name-only --diff-filter^=U') do goto :conflict
git submodule update -q --init || goto :fail
git add -A
git diff --cached --quiet || (git commit -q -m "From the laptop" && git push -q origin main) || goto :fail
echo Up to date with the PC.
pause
exit /b 0
:conflict
echo The same file changed here and on the PC:
git diff --name-only --diff-filter=U
echo Nothing was sent. Your laptop version is safe in the git stash. Ask Claude to sort it out.
pause
exit /b 1
:fail
echo Sync failed. Nothing was deleted. Send Claude the message above.
pause
exit /b 1
