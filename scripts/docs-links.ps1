param(
    [switch]$DumpOnly
)

# Run Lychee link checker in Docker. Uses lychee.toml config.
$patterns = @(
    'README.md',
    'docs/**/*.md',
    '.github/**/*.md'
)

$patternsJoined = $patterns -join ' '

function Invoke-LycheeDocker {
    param(
        [string]$Args
    )
    docker run --rm -w /input -v "${PWD}:/input" lycheeverse/lychee:latest --config lychee.toml --no-progress $Args
}

function Invoke-LycheeLocal {
    param(
        [string]$Args
    )
    lychee --config lychee.toml --no-progress $Args
}

function Test-DockerAvailable {
    try {
        $null = docker version 2>$null
        return $true
    }
    catch {
        return $false
    }
}

function Test-LycheeLocalAvailable {
    try {
        $null = Get-Command lychee -ErrorAction Stop
        return $true
    }
    catch {
        return $false
    }
}

if ($DumpOnly) {
    Write-Host 'Lychee (dump links only)...' -ForegroundColor Cyan
    $args = "--dump $patternsJoined"

    if (Test-DockerAvailable) {
        Invoke-LycheeDocker -Args $args
    }
    elseif (Test-LycheeLocalAvailable) {
        Invoke-LycheeLocal -Args $args
    }
    else {
        Write-Host "Link check requires either Docker (to run lycheeverse/lychee) or a local 'lychee' install." -ForegroundColor Yellow
        Write-Host "- Option A: Start Docker Desktop and rerun this script" -ForegroundColor Yellow
        Write-Host "- Option B: Install Lychee locally and rerun (https://github.com/lycheeverse/lychee)" -ForegroundColor Yellow
        exit 1
    }
}
else {
    Write-Host 'Lychee (validate links)...' -ForegroundColor Cyan
    $args = "$patternsJoined"

    if (Test-DockerAvailable) {
        Invoke-LycheeDocker -Args $args
    }
    elseif (Test-LycheeLocalAvailable) {
        Invoke-LycheeLocal -Args $args
    }
    else {
        Write-Host "Link check requires either Docker (to run lycheeverse/lychee) or a local 'lychee' install." -ForegroundColor Yellow
        Write-Host "- Option A: Start Docker Desktop and rerun this script" -ForegroundColor Yellow
        Write-Host "- Option B: Install Lychee locally and rerun (https://github.com/lycheeverse/lychee)" -ForegroundColor Yellow
        exit 1
    }
}
