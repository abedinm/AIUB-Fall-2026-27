@echo off
rem Laptop side of the hub. Double-click: gets the PC's latest, then sends anything you changed here.
rem Edit files in the course folders or drop new ones in inbox\; the PC copies them over on its 3-hourly sync.
cd /d "%~dp0"
git pull -q --rebase --autostash origin main || goto :fail
git submodule update -q --init || goto :fail
git add -A
git diff --cached --quiet || (git commit -q -m "From the laptop" && git push -q origin main) || goto :fail
echo Up to date with the PC.
pause
exit /b 0
:fail
echo Sync failed. Nothing was deleted. Send Claude the message above.
pause
exit /b 1
