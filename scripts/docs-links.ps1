param(
    [switch]$DumpOnly
)

# Run Lychee link checker in Docker. Uses lychee.toml config.
$patterns = @(
    'README.md',
    'docs/**/*.md',
    '.github/**/*.md'
)

function Invoke-LycheeDocker {
    param(
        [string[]]$Args
    )
    docker run --rm -w /input -v "${PWD}:/input" lycheeverse/lychee:latest @Args
}

function Invoke-LycheeLocal {
    param(
        [string[]]$Args
    )
    lychee @Args
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
    $args = @('--config', 'lychee.toml', '--no-progress', '--dump') + $patterns

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
    $args = @('--config', 'lychee.toml', '--no-progress') + $patterns

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
