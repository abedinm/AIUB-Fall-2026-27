# Two-way sync between this PC's course folders and this repo.
# PC -> GitHub: each source folder below is mirrored into its repo folder.
# GitHub -> PC: files added or edited on the Mac inside a mirrored folder are copied back to the PC first;
# inbox/ is for anything new from the Mac. Deleting a file on the Mac does not delete it on the PC.
param([switch]$NoPush)

$repo = $PSScriptRoot
$guide = 'D:\Temp\claude\D--Claude-Data-claude-pzs8sxrjxfjjc-scratch-workspaces-bd2dd7d2-36a9-4410-b2b9-ba3022b1cd30-3ec83dbf-3631-4888-9868-980b869964b1-scratch-2026-11-03-482897\9111b79c-a48b-4daa-808e-34ab93d2a512\scratchpad\guide'
$map = [ordered]@{
    'Plan/midterm-plan' = 'F:\outputs\midterm-plan'
    'Plan/routine'      = 'F:\outputs\aiub-routine'
    'Plan/guide-source' = $guide
    'AI/ai-midterm'     = 'F:\outputs\ai-midterm'
    'AI/ai-final'       = 'F:\outputs\ai-final'
    'AI/csc3217-ai'     = 'F:\outputs\csc3217-ai'
    'EM/files'          = 'D:\Personal\Downloads\AIUB Engineering Management Notes'
    'MIS/files'         = 'D:\Personal\Downloads\AIUB Management Information Systems Notes'
    'OOP2/files'        = 'D:\Personal\Downloads\AIUB Object Oriented Programming 2 Notes'
    'OOP2/outputs'      = 'F:\outputs\aiub-oop2'
    'Python/files'      = 'D:\Personal\Downloads\AIUB Programming in Python Notes'
}
# The guide folder holds two Chrome profiles (cookies); never mirror them.
$xd = @('.git', 'node_modules', '__pycache__', '.venv', 'venv', '.pytest_cache', 'bin', 'obj', '.vs', "$guide\chrome-prof", "$guide\cp")
$xf = @('plan-backup-*.html', '*.err', '~$*', 'Thumbs.db', 'desktop.ini', '.DS_Store')

function Invoke-Git { & git.exe -c core.quotepath=false @args; if ($LASTEXITCODE -ne 0) { throw "git $args failed ($LASTEXITCODE)" } }

Set-Location $repo
$before = (& git rev-parse HEAD).Trim()
Invoke-Git pull -q --rebase --autostash origin main
$after = (& git rev-parse HEAD).Trim()

if ($after -ne $before) {
    foreach ($f in (& git -c core.quotepath=false diff --name-only --diff-filter=AM $before $after)) {
        foreach ($k in $map.Keys) {
            if ($f.StartsWith("$k/")) {
                $dst = Join-Path $map[$k] ($f.Substring($k.Length + 1) -replace '/', '\')
                New-Item -ItemType Directory -Force (Split-Path $dst) | Out-Null
                Copy-Item -LiteralPath (Join-Path $repo $f) -Destination $dst -Force
                "From the Mac: $f -> $dst"
            }
        }
    }
}

foreach ($k in $map.Keys) {
    $src = $map[$k]
    # A missing or empty source (e.g. a cleared temp folder) must never wipe the repo copy.
    if (-not (Test-Path -LiteralPath $src) -or -not (Get-ChildItem -LiteralPath $src -File -Recurse -ErrorAction SilentlyContinue | Select-Object -First 1)) {
        "Skipped (missing or empty): $src"
        continue
    }
    $dst = Join-Path $repo ($k -replace '/', '\')
    robocopy $src $dst /MIR /XD @xd /XF @xf /R:1 /W:1 /NFL /NDL /NJH /NJS /NP | Out-Null
    if ($LASTEXITCODE -ge 8) { throw "robocopy failed for $src ($LASTEXITCODE)" }
}

Invoke-Git submodule update -q --init --remote
Invoke-Git add -A
& git diff --cached --quiet
if ($LASTEXITCODE -ne 0) {
    Invoke-Git commit -q -m "Sync from PC $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
    "Committed: $((& git show --stat --oneline HEAD | Select-Object -Last 1).Trim())"
} else { 'No changes.' }
if (-not $NoPush) { Invoke-Git push -q origin main }

$inbox = Get-ChildItem -LiteralPath (Join-Path $repo 'inbox') -File -Recurse | Where-Object Name -ne '.gitkeep'
if ($inbox) { 'Inbox:'; $inbox | ForEach-Object { '  ' + $_.FullName.Substring($repo.Length + 1) } } else { 'Inbox: empty' }
