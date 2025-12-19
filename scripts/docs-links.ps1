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

try {
    $null = docker version 2>$null
}
catch {
    Write-Host 'Docker is required to run Lychee for link checking. Start Docker Desktop and rerun.' -ForegroundColor Yellow
    exit 1
}

if ($DumpOnly) {
    Write-Host 'Lychee (dump links only)...' -ForegroundColor Cyan
    docker run --rm -w /input -v "${PWD}:/input" lycheeverse/lychee:latest --config lychee.toml --no-progress --dump $patternsJoined
}
else {
    Write-Host 'Lychee (validate links)...' -ForegroundColor Cyan
    docker run --rm -w /input -v "${PWD}:/input" lycheeverse/lychee:latest --config lychee.toml --no-progress $patternsJoined
}
