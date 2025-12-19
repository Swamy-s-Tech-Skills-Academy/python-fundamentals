param(
    [switch]$Fix
)

# Run markdownlint-cli2 across repo docs. Use --fix if -Fix is supplied.
$patterns = @(
    'README.md',
    'docs/**/*.md',
    '.github/**/*.md'
)

Write-Host 'Running markdownlint-cli2...' -ForegroundColor Cyan
$args = @('markdownlint-cli2')

if ($Fix) {
    $args += '--fix'
}

$args += $patterns

npx --yes @args
