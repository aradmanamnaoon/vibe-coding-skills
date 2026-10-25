param(
    [string]$Since = "2025-10-25",
    [int]$LimitPerQuery = 20,
    [string]$OutputPath = "research/raw/github-issues.json"
)

$ErrorActionPreference = "Stop"

$searches = @(
    @{ repo = "openai/codex"; query = "stuck"; tag = "agent-loop" },
    @{ repo = "openai/codex"; query = "context"; tag = "context" },
    @{ repo = "openai/codex"; query = "MCP"; tag = "mcp" },
    @{ repo = "openai/codex"; query = "sandbox"; tag = "sandbox" },
    @{ repo = "openai/codex"; query = "Windows"; tag = "cross-platform" },
    @{ repo = "openai/codex"; query = "test"; tag = "testing" },
    @{ repo = "cline/cline"; query = "context"; tag = "context" },
    @{ repo = "cline/cline"; query = "checkpoint"; tag = "recovery" },
    @{ repo = "cline/cline"; query = "terminal"; tag = "terminal" },
    @{ repo = "cline/cline"; query = "MCP"; tag = "mcp" },
    @{ repo = "cline/cline"; query = "loop"; tag = "agent-loop" },
    @{ repo = "cline/cline"; query = "edit file"; tag = "editing" },
    @{ repo = "RooCodeInc/Roo-Code"; query = "loop"; tag = "agent-loop" },
    @{ repo = "RooCodeInc/Roo-Code"; query = "context"; tag = "context" },
    @{ repo = "RooCodeInc/Roo-Code"; query = "checkpoint"; tag = "recovery" },
    @{ repo = "RooCodeInc/Roo-Code"; query = "terminal"; tag = "terminal" },
    @{ repo = "RooCodeInc/Roo-Code"; query = "MCP"; tag = "mcp" },
    @{ repo = "RooCodeInc/Roo-Code"; query = "completion"; tag = "completion-claims" },
    @{ repo = "Aider-AI/aider"; query = "benchmark"; tag = "benchmarking" },
    @{ repo = "Aider-AI/aider"; query = "test"; tag = "testing" },
    @{ repo = "Aider-AI/aider"; query = "edit format"; tag = "editing" },
    @{ repo = "Aider-AI/aider"; query = "context"; tag = "context" },
    @{ repo = "Aider-AI/aider"; query = "lint"; tag = "quality-gates" },
    @{ repo = "continuedev/continue"; query = "context"; tag = "context" },
    @{ repo = "continuedev/continue"; query = "indexing"; tag = "indexing" },
    @{ repo = "continuedev/continue"; query = "tool"; tag = "tool-use" },
    @{ repo = "continuedev/continue"; query = "MCP"; tag = "mcp" },
    @{ repo = "continuedev/continue"; query = "edit"; tag = "editing" },
    @{ repo = "microsoft/vscode-copilot-release"; query = "agent"; tag = "agent-reliability" },
    @{ repo = "microsoft/vscode-copilot-release"; query = "terminal"; tag = "terminal" },
    @{ repo = "microsoft/vscode-copilot-release"; query = "context"; tag = "context" },
    @{ repo = "microsoft/vscode-copilot-release"; query = "edit"; tag = "editing" },
    @{ repo = "microsoft/vscode-copilot-release"; query = "test"; tag = "testing" }
)

$all = [System.Collections.Generic.List[object]]::new()
$failures = [System.Collections.Generic.List[object]]::new()

foreach ($search in $searches) {
    $args = @(
        "search", "issues", $search.query,
        "--repo", $search.repo,
        "--created", ">=$Since",
        "--limit", "$LimitPerQuery",
        "--json", "number,title,url,createdAt,updatedAt,state,body,labels"
    )
    $json = & gh @args
    if ($LASTEXITCODE -ne 0) {
        $failures.Add([pscustomobject]@{
            repository = $search.repo
            query = $search.query
            tag = $search.tag
            reason = "gh search issues exited with code $LASTEXITCODE"
        })
        continue
    }

    $items = $json | ConvertFrom-Json
    foreach ($item in $items) {
        $all.Add([pscustomobject]@{
            repository = $search.repo
            search_tag = $search.tag
            search_query = $search.query
            number = $item.number
            title = $item.title
            url = $item.url
            created_at = $item.createdAt
            updated_at = $item.updatedAt
            state = $item.state
            body = $item.body
            labels = @($item.labels | ForEach-Object { $_.name })
        })
    }
}

$deduped = $all |
    Group-Object url |
    ForEach-Object {
        $first = $_.Group[0]
        [pscustomobject]@{
            repository = $first.repository
            search_tags = @($_.Group.search_tag | Sort-Object -Unique)
            number = $first.number
            title = $first.title
            url = $first.url
            created_at = $first.created_at
            updated_at = $first.updated_at
            state = $first.state
            body = $first.body
            labels = $first.labels
        }
    } |
    Sort-Object repository, number

$resolvedOutput = Join-Path (Get-Location) $OutputPath
$parent = Split-Path -Parent $resolvedOutput
New-Item -ItemType Directory -Force -Path $parent | Out-Null
$payload = [pscustomobject]@{
    collected_at = (Get-Date).ToUniversalTime().ToString("o")
    since = $Since
    unique_issues = @($deduped)
    failed_queries = @($failures)
}
$payload | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $resolvedOutput -Encoding UTF8

$sanitizer = Join-Path (Split-Path -Parent $PSScriptRoot) "scripts\\sanitize_research_archive.py"
if (Test-Path -LiteralPath $sanitizer) {
    & py -3.10 $sanitizer $resolvedOutput
    if ($LASTEXITCODE -ne 0) {
        throw "Research archive sanitizer failed."
    }
}

Write-Output "Collected $($all.Count) search hits and $($deduped.Count) unique issues."
Write-Output "Failed queries: $($failures.Count)"
Write-Output $resolvedOutput
