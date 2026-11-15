param([string]$Render = "none")
$g = $PSScriptRoot
$chrome = "C:\Program Files\Google\Chrome\Application\chrome.exe"
$url = "file:///" + ($g -replace '\\', '/') + "/guide.html"

function Print-Guide {
    $cargs = @("--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--generate-pdf-document-outline",
               "--virtual-time-budget=5000", "--user-data-dir=$g\cp", "--print-to-pdf=$g\guide.pdf", $url)
    Start-Process -FilePath $chrome -ArgumentList $cargs -Wait -NoNewWindow -RedirectStandardError "$g\chrome.err" | Out-Null
}

Remove-Item "$g\pages.json" -ErrorAction SilentlyContinue
node "$g\build.js" "$g\guide.html" "$g\pages.json"
Print-Guide
python -I "$g\pages.py" "$g\guide.pdf" "$g\pages.json" "$g\png" "none"
node "$g\build.js" "$g\guide.html" "$g\pages.json"
Print-Guide
python -I "$g\pages.py" "$g\guide.pdf" "$g\pages2.json" "$g\png" $Render
if ((Get-Content "$g\pages.json" -Raw) -ne (Get-Content "$g\pages2.json" -Raw)) { "WARNING: page numbers moved between passes" } else { "page numbers stable" }
