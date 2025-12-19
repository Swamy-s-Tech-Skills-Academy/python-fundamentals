param(
    [switch]$DumpOnly
)

# Run Lychee link checker in Docker. Uses lychee.toml config.
$root = $PWD.Path

function Get-LycheeInputs {
    $files = New-Object System.Collections.Generic.List[string]

    $readmePath = Join-Path $root 'README.md'
    if (Test-Path $readmePath) {
        $files.Add('README.md')
    }

    $docsPath = Join-Path $root 'docs'
    if (Test-Path $docsPath) {
        Get-ChildItem -Path $docsPath -Recurse -File -Filter '*.md' | ForEach-Object {
            $relative = $_.FullName.Substring($root.Length).TrimStart('\','/')
            $files.Add(($relative -replace '\\','/'))
        }
    }

    $githubPath = Join-Path $root '.github'
    if (Test-Path $githubPath) {
        Get-ChildItem -Path $githubPath -Recurse -File -Filter '*.md' | ForEach-Object {
            $relative = $_.FullName.Substring($root.Length).TrimStart('\','/')
            $files.Add(($relative -replace '\\','/'))
        }
    }

    return $files
}

function New-LycheeInputsFile {
    $inputs = Get-LycheeInputs
    if ($inputs.Count -eq 0) {
        Write-Host 'No Markdown inputs found for Lychee.' -ForegroundColor Yellow
        exit 1
    }

    $tempName = ".lychee-inputs.$PID.txt"
    $tempPath = Join-Path $root $tempName
    $inputs | Set-Content -Path $tempPath -Encoding UTF8
    return $tempPath
}

function Invoke-LycheeDocker {
    param(
        [string[]]$Args
    )
    $dockerArgs = @(
        'run',
        '--rm',
        '-w',
        '/input',
        '-v',
        "${PWD}:/input",
        'lycheeverse/lychee:latest'
    ) + $Args

    docker @dockerArgs
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

    $inputsFile = New-LycheeInputsFile
    try {
        $args = @('--config', 'lychee.toml', '--no-progress', '--dump', '--files-from')

        if (Test-DockerAvailable) {
            $args += "/input/$(Split-Path -Leaf $inputsFile)"
            Invoke-LycheeDocker -Args $args
        }
        elseif (Test-LycheeLocalAvailable) {
            $args += (Split-Path -Leaf $inputsFile)
            Invoke-LycheeLocal -Args $args
        }
        else {
            Write-Host "Link check requires either Docker (to run lycheeverse/lychee) or a local 'lychee' install." -ForegroundColor Yellow
            Write-Host "- Option A: Start Docker Desktop and rerun this script" -ForegroundColor Yellow
            Write-Host "- Option B: Install Lychee locally and rerun (https://github.com/lycheeverse/lychee)" -ForegroundColor Yellow
            exit 1
        }
    }
    finally {
        Remove-Item -Force -ErrorAction SilentlyContinue $inputsFile
    }
}
else {
    Write-Host 'Lychee (validate links)...' -ForegroundColor Cyan

    $inputsFile = New-LycheeInputsFile
    try {
        $args = @('--config', 'lychee.toml', '--no-progress', '--files-from')

        if (Test-DockerAvailable) {
            $args += "/input/$(Split-Path -Leaf $inputsFile)"
            Invoke-LycheeDocker -Args $args
        }
        elseif (Test-LycheeLocalAvailable) {
            $args += (Split-Path -Leaf $inputsFile)
            Invoke-LycheeLocal -Args $args
        }
        else {
            Write-Host "Link check requires either Docker (to run lycheeverse/lychee) or a local 'lychee' install." -ForegroundColor Yellow
            Write-Host "- Option A: Start Docker Desktop and rerun this script" -ForegroundColor Yellow
            Write-Host "- Option B: Install Lychee locally and rerun (https://github.com/lycheeverse/lychee)" -ForegroundColor Yellow
            exit 1
        }
    }
    finally {
        Remove-Item -Force -ErrorAction SilentlyContinue $inputsFile
    }
}
