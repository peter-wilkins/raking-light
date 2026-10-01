param(
    [string]$BlenderPath,
    [switch]$RenderOnly
)

$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path $PSScriptRoot -Parent

try {
    if (-not $BlenderPath) {
        $command = Get-Command blender.exe -ErrorAction SilentlyContinue
        if ($command) {
            $BlenderPath = $command.Source
        } else {
            $installRoot = Join-Path $env:ProgramFiles 'Blender Foundation'
            $candidates = @(Get-ChildItem $installRoot -Filter blender.exe -Recurse -ErrorAction SilentlyContinue |
                Sort-Object FullName -Descending)
            if ($candidates.Count -gt 0) { $BlenderPath = $candidates[0].FullName }
        }
    }
    if (-not $BlenderPath -or -not (Test-Path -LiteralPath $BlenderPath -PathType Leaf)) {
        throw 'Install Blender 4.5 LTS from https://www.blender.org/download/lts/4-5/ or pass -BlenderPath with the path to blender.exe.'
    }

    $scriptPath = Join-Path $projectRoot 'spikes\botanical_vbit_study.py'
    $outputPath = Join-Path $projectRoot 'artifacts\botanical-vbit-study'
    & $BlenderPath --background --python-exit-code 1 --python $scriptPath -- --output-dir $outputPath
    if ($LASTEXITCODE -ne 0) { throw "Blender failed with exit code $LASTEXITCODE." }

    $modelPath = Join-Path $outputPath 'botanical-vbit-study.blend'
    if (-not (Test-Path -LiteralPath $modelPath)) { throw 'Blender did not produce the expected model.' }
    Write-Host "Studio outputs: $outputPath"
    if (-not $RenderOnly) {
        Start-Process -FilePath $BlenderPath -ArgumentList ('"' + $modelPath + '"')
    }
} catch {
    Write-Host $_.Exception.Message -ForegroundColor Red
    exit 1
}
